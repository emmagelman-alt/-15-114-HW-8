# -15-114-HW-8

prompts I found myself using multiple times across homeworks: 
"ask me 1 question at a time until you have 95% certainty you understand what I want to build, and then begin building"
"give me a link to play the game, give me a sharable link, it says it cant make a sharable link"
"(ask me any clarifying questions before acting)"

My most common ask was for Claude to ask me any questions it had before beginning so that it would have a better understanding of what I wanted to build. Some other common asks were for constant live previews of the frontend, explanations of what each part did, and how to share prototypes. I also noticed that I would get frustrated and stop runs and re-start them with modified asks if too much time had elapsed with no feedback about what was the holdup. 

I designed a skill called due-diligence that addresses all the common asks in my Claude flow. Due diligence tells claude to ask me any clarifying questions until 96% understanding as well as predict things that might need to be installed and to begin the installation once I approve. This saves me a lot of time during my setup when I have to manually ask for those questions and run into issues much later on when claude realizes that I don't actually have some of the needed libraries installed. Due diligence sets me up for success. Due diligence triggers after the first prompt in a new code space or in response to a prompt that concerns the development of a new feature/product. I wanted Due Diligence to be applicable to any project at any complexity level so it does not rely on any outside sources or files. 

My agent kept not knowing my setup for shipping. Claude was able to write the code wth little issue but when it came time to ship, I often ran into barriers. In the mosaic game prompt log, claude kept making private links that broke when I tried to share them despite my request for a shareable link, it failed to push because it could not read the username for GitHub as it has no GitHub login on my mac. In warp, claude would not specify where commands run so I was confused why certain things weren't showing up in the site ( it was because site was only showing main). In warp I was also signed into the wrong account and then to the wrong organization by accident so it failed 8 times without me knowing why. As someone that doesn't come from a technical heavy background, I am still learning how to ship things and what the proper pipelines look like which can be difficult for claude to work with as sometimes assumes certain things have already been handled or understood without explicit instruction. This is why I added the check for install requirnments secton to my skill so that I dont run into the issue of needing something I dont have AFTER I have already chosen how to proceed. By telling my skill to anticipate what setup I will need and making sure it is taken cae of before my agent can start actually coding, means that I can prevent the problem from occuring later on in the process and needing to change my plan or take additional 30 mins to fugre out the best course of action. 

I confirmed that the skill works in claude code. The skill lives at .claude/skills/due-diligence/SKILL.md in the repo. To get the skill on your own computer, Clone the repo and open it in claude code to automatically import the skill.  

This skill is also usable in Codex. To install in codex, run "mkdir -p ~/.agents/skills
cp -R ~/.claude/skills/due-diligence ~/.agents/skills/" in the terminal. Restart codex and then open a new workspace and type /skills to find due diligence. 

After reading through the documentation on MCP servers, I thought about what I would find helpful in my day to day life. I take a lot of courses and the only way for me to see all the assignments that I have due is to log in to canvas and navigate to the dashboard. Sometimes I have to go through the entire sign in process with my cmu login, DUO, and then finally get to the page. I also sometimes find the dahsboard overwhelming and tend to write down what is due in my notes app. I wanted a way to easily see what assignments I have and easly navigate to them. This is why I decided to build an MCP server that connects to my canvas via a access token and can easily list all my assignments, their due dates and times, group or individual status, link to their page, and what class they are for. 

AI USAGE:
- I had claude make me an outline for the skill.md file which I then pasted nto VS code and wrote/filled out by hand. I then had VS copilot check my writing and rephrase, restructure, and spell check where needed to make sure the skill was properly formated and the phrasing was understandable by my agent.
- For the skill.md iteration, I discovered the problem on my own, wrote the change into vs code by hand, and then had copilot rephrase and spellcheck the updated clause to ensure that my agent would use it correctly.
- For the MCP I worked with claude to plan out how to build it, claude took on most of the coding. I personally read through the docstring and edited it to add missing parameters and steps before having claude run tests.

---

## Installing the Canvas deadlines MCP server

> **Written by Claude:** The instructions in this section were written by Claude (Anthropic's AI assistant, through Claude Code), not by me. Claude helped me build and test this server.

`canvas-deadlines-mcp` gives an MCP client, such as Claude Code, one tool called `get_deadlines`. When you ask what's due, it looks up your upcoming Canvas assignments and returns each one's due date, whether it's group or individual work, and a link to its Canvas page. It asks Canvas fresh every time, so new assignments show up right away.

### What you need

- git
- An MCP client. These steps use Claude Code, and the end of this section covers other clients.
- A Canvas account that lets you make an access token. In Canvas, look for **+ New Access Token** under Account → Settings. Some schools turn this off for students. Without a token, the tool only shows made-up sample deadlines.

### Steps (Mac or Linux)

**1. Install uv.** It installs Python and the server's packages for you.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

After it finishes, open a new terminal window so the `uv` command is available.

**2. Download this repo** into a folder called `hw8`. The repo's real name starts with a dash, which confuses `cd`, so the simpler name avoids that.

```bash
git clone https://github.com/emmagelman-alt/-15-114-HW-8.git hw8
```

```bash
cd hw8/canvas-deadlines-mcp
```

**3. Install the server's packages.** This also downloads Python 3.12 if you don't have it.

```bash
uv sync
```

**4. Check that the server starts.** If it's working, it sits there silently, waiting. Press Ctrl+C to stop it.

```bash
uv run server.py
```

**5. Register it with Claude Code.** Run this from inside `canvas-deadlines-mcp`, so the full paths fill in automatically. It needs the `claude` command line tool. If you only have the Claude desktop app, use the "Other clients" section below with Claude Code's settings file, `~/.claude.json`.

```bash
claude mcp add --scope user canvas-deadlines -- "$(which uv)" --directory "$PWD" run server.py
```

The server uses CMU's Canvas (`https://canvas.cmu.edu`) unless you tell it otherwise. If your school's Canvas has a different address, add it right after the server name:

```bash
claude mcp add --scope user canvas-deadlines -e CANVAS_URL=https://canvas.yourschool.edu -- "$(which uv)" --directory "$PWD" run server.py
```

**6. Make and save your Canvas token.**

1. In Canvas, go to Account → Settings → **+ New Access Token**.
2. Enter a purpose, set an expiration date, and click **Generate Token**.
3. Copy the token. Canvas only shows it once.
4. On a Mac, run the command below. It saves the copied token to a private file without showing it on screen. On Linux, create the file `~/.config/canvas-deadlines/token` with the token as its only text.

```bash
(umask 077; mkdir -p ~/.config/canvas-deadlines && pbpaste > ~/.config/canvas-deadlines/token)
```

Never put the token inside the repo folder, and don't share it. Anyone with your token can act as you in Canvas. You can delete it at any time under Account → Settings → Approved Integrations.

**7. Test it.** Start a new Claude Code session and ask "What do I have due this week?"

- The transcript should show a call to `get_deadlines`.
- The first line of the result should say **Source: Canvas (live).**

### Windows

These steps haven't been tested on Windows. They should work with these changes:

- Install uv in PowerShell with `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`.
- Skip the `claude mcp add` command and follow "Other clients" below. Use `(Get-Command uv).Source` to find the full path to `uv`.
- Save the token as the only text in `%USERPROFILE%\.config\canvas-deadlines\token`.

### Other clients

Every MCP client needs the same three things: a name, the full path to `uv` as the command, and the arguments. `which uv` prints the uv path, and `pwd`, run inside `canvas-deadlines-mcp`, prints the folder path.

For Codex, add this to `~/.codex/config.toml`:

```toml
[mcp_servers.canvas-deadlines]
command = "/full/path/to/uv"
args = ["--directory", "/full/path/to/hw8/canvas-deadlines-mcp", "run", "server.py"]
```

Cursor (`~/.cursor/mcp.json`), Claude Code (`~/.claude.json`) and the Claude desktop chat app take the same values in JSON, under `"mcpServers"`:

```json
"canvas-deadlines": {
  "command": "/full/path/to/uv",
  "args": ["--directory", "/full/path/to/hw8/canvas-deadlines-mcp", "run", "server.py"]
}
```

To use a Canvas other than CMU's, add `"env": {"CANVAS_URL": "https://canvas.yourschool.edu"}` to the JSON entry. In Codex, use `env = { CANVAS_URL = "https://canvas.yourschool.edu" }`.

### Troubleshooting

- **"Source: the sample file…"** means the server couldn't find the token file, or the file is empty.
- **"Canvas rejected the saved access token"** means the token is wrong or has expired. Make a new one.
- **The tool doesn't appear** in the session. Check that every path in the config is a full path, not a shortened one. In Claude Code, `claude mcp get canvas-deadlines` shows whether the server connects.
- **An assignment is missing.** The tool only includes assignments with a due date inside the time window you asked about. Try asking "What's due this month?"
