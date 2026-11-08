"""Canvas deadlines MCP server (15-114 HW 8).

Gives an agent one tool, get_deadlines, that looks up upcoming assignments.
It asks Canvas when an access token is saved, and otherwise reads the sample
file deadlines.json.
"""

import json
import logging
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

import httpx
from mcp.server.mcpserver import MCPServer

# Stdout carries the messages between Claude Code and this server, so anything
# printed there breaks the connection. Log to stderr instead.
logging.basicConfig(stream=sys.stderr, level=logging.INFO)
log = logging.getLogger("canvas-deadlines")
logging.getLogger("httpx").setLevel(logging.WARNING)  # don't log every Canvas request

# Full path next to this file, because Claude Code starts the server from a different folder.
DEADLINES_FILE = Path(__file__).resolve().parent / "deadlines.json"

# Canvas settings. The token is saved outside this repo so it never ends up on GitHub.
CANVAS_URL = os.environ.get("CANVAS_URL", "https://canvas.cmu.edu").rstrip("/")
TOKEN_FILE = Path.home() / ".config" / "canvas-deadlines" / "token"

mcp = MCPServer("canvas-deadlines")


@mcp.tool()
async def get_deadlines(course: str | None = None, days_ahead: int = 7) -> str:
    """Look up the user's upcoming assignment deadlines from Canvas: homework, projects, essays and exams.

    Use this whenever the user asks what's due, what homework or assignments are coming up,
    when something is due, or what they should work on next, even if they don't say
    "deadline". You can't know the user's assignments yourself, so call this tool instead
    of guessing. It only has titles, due dates, group or individual work, and Canvas
    links. It doesn't have assignment instructions, grades or class times.

    Args:
        course: Optional course number or part of a course name, like "15-114" or
            "calculus". Leave it out to get every course.
        days_ahead: How many days ahead to look, starting now. Defaults to 7 (the next
            week). Use 1 for "today", 2 for "tomorrow" and about 30 for "this month".

    Returns:
        First, a line saying whether the data came from Canvas or from the sample file.
        Then one line per assignment, soonest first, with the course, title, due date
        and time, and if the assignment specifies if it is groupwork or individual. Also include a link to the assignment's page on Canvas that the user can click on to open canvas in their browser and land on the assignment page.  If nothing matches, a sentence saying nothing is due.
    """
    token = read_canvas_token()
    if token:
        try:
            assignments = await load_from_canvas(token)
        except httpx.HTTPStatusError as err:
            if err.response.status_code == 401:
                return (
                    "Canvas rejected the saved access token. It may have expired or been "
                    "deleted. Make a new token in Canvas and save it again."
                )
            return f"Canvas returned an error (HTTP {err.response.status_code}). Try again in a minute."
        except httpx.HTTPError:
            return "Couldn't reach Canvas. Check the internet connection and try again."
        source = "Source: Canvas (live)."
    else:
        try:
            assignments = json.loads(DEADLINES_FILE.read_text()).get("assignments", [])
        except FileNotFoundError:
            return f"Couldn't find the deadlines file at {DEADLINES_FILE}."
        except json.JSONDecodeError as err:
            return f"The deadlines file isn't valid JSON: {err}"
        source = (
            "Source: the sample file deadlines.json, because no Canvas token is saved. "
            "These are not real deadlines."
        )

    days = max(days_ahead, 1)
    now = datetime.now().astimezone()
    end = now + timedelta(days=days)

    upcoming = []
    for item in assignments:
        try:
            # Canvas dates are in UTC and the sample file's are local time.
            # astimezone() turns both into local time so they can be compared.
            due = datetime.fromisoformat(item["due"]).astimezone()
        except (KeyError, TypeError, ValueError):
            log.warning("Skipping an assignment with a missing or bad due date: %r", item.get("title"))
            continue
        if not now <= due <= end:
            continue
        course_names = f"{item.get('course', '')} {item.get('course_code', '')}".lower()
        if course and course.lower() not in course_names:
            continue
        upcoming.append((due, item))

    upcoming.sort(key=lambda pair: pair[0])
    log.info("get_deadlines(course=%r, days_ahead=%r) found %d", course, days_ahead, len(upcoming))

    if not upcoming:
        where = f" for {course}" if course else ""
        return f"{source}\nNothing is due{where} in the next {days} days."

    return source + "\n" + "\n".join(format_assignment(due, item) for due, item in upcoming)


def format_assignment(due: datetime, item: dict) -> str:
    """Turn one assignment into a single line of text for the agent."""
    line = (
        f"{item.get('course', 'Unknown course')}: {item.get('title', 'Untitled')}, "
        # Day and hour are built by hand because "%-d" and "%-I" don't work on Windows.
        f"due {due:%a %b} {due.day} at {due.hour % 12 or 12}:{due:%M %p}"
    )
    # Only say group or individual when the assignment specifies it.
    if item.get("group") is True:
        line += " (group work)"
    elif item.get("group") is False:
        line += " (individual)"
    if item.get("url"):
        line += f". Canvas link: {item['url']}"
    return line


def read_canvas_token() -> str | None:
    """Return the Canvas token from CANVAS_TOKEN or the token file, or None if neither is set."""
    token = os.environ.get("CANVAS_TOKEN", "").strip()
    if token:
        return token
    try:
        return TOKEN_FILE.read_text().strip() or None
    except FileNotFoundError:
        return None


async def load_from_canvas(token: str) -> list[dict]:
    """Get future assignments from every active Canvas course, in the same shape as deadlines.json."""
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient(headers=headers, timeout=20) as client:
        courses = await get_all_pages(client, "courses", {"enrollment_state": "active", "per_page": 100})
        assignments = []
        for course in courses:
            if "name" not in course:
                continue  # Canvas lists courses you can't open yet without a name
            try:
                items = await get_all_pages(
                    client,
                    f"courses/{course['id']}/assignments",
                    {"bucket": "future", "order_by": "due_at", "per_page": 100},
                )
            except httpx.HTTPStatusError as err:
                if err.response.status_code == 401:
                    raise
                log.warning(
                    "Skipping course %s: Canvas returned HTTP %s",
                    course.get("course_code"),
                    err.response.status_code,
                )
                continue
            for item in items:
                if not item.get("due_at"):
                    continue  # no due date, so it can't be "coming up"
                assignments.append(
                    {
                        "course": course["name"],
                        "course_code": course.get("course_code", ""),
                        "title": item.get("name", "Untitled"),
                        "due": item["due_at"],
                        # Canvas sets group_category_id only on group assignments.
                        "group": item.get("group_category_id") is not None,
                        "url": item.get("html_url"),
                    }
                )
    log.info("Canvas: %d courses, %d assignments with future due dates", len(courses), len(assignments))
    return assignments


async def get_all_pages(client: httpx.AsyncClient, path: str, params: dict) -> list[dict]:
    """GET a Canvas list, following its "next page" links until there are none."""
    url: str | None = f"{CANVAS_URL}/api/v1/{path}"
    results: list[dict] = []
    while url:
        response = await client.get(url, params=params)
        response.raise_for_status()
        results.extend(response.json())
        url = response.links.get("next", {}).get("url")
        params = None  # the next-page link already includes the settings
    return results


if __name__ == "__main__":
    mcp.run()  # stdio: Claude Code talks to the server through stdin and stdout
