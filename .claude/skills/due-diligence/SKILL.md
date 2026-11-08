---
name: due-diligence
description: Use when clarifying or planning a new product, feature, or script. Ask focused questions, identify constraints and dependencies, and get explicit approval before installing anything.
---

# Due Diligence

Clarify the intended outcome and constraints for a new project before implementation or planning. Do not treat an arbitrary “96% understanding” threshold as measurable; stop when the important decisions are clear enough to proceed.

## Understanding questions take priority

If the user's prompt says they do not understand, are confused, or want something explained or worked through (for example, “I don't understand,” “can you help me understand this,” “I'm confused,” “explain,” or similar phrasing), address that first in a natural, conversational response. This applies even when the same prompt later asks to plan or build something: explain the missing information without starting this skill's interview, plan, or implementation, then wait for the user to confirm they understand and ask to continue in planning or build mode. On that follow-up, resume this skill using the context the user already provided. If they only asked for an explanation and did not ask to plan or build, answer normally without starting the due-diligence workflow.

## When to use

- The user is starting a new product, feature, app, or script.
- The user asks for help planning a new technical initiative.
- The goal or requirements need clarification before useful work can begin.

## When not to use

- The user asks a clear, routine question about an existing project.
- The user requests debugging or a narrowly scoped change to existing code.
- The user has already provided enough information to proceed with a specific task.

If it is unclear whether the user wants a discovery interview or direct help, ask whether they want to answer clarifying questions first.

## Procedure

1. Read the user's initial request and identify the objective, intended users, expected deliverable, and any stated constraints.
2. Identify only the important unanswered questions. Ask one concise question at a time; use answer choices when they make the decision easier, and allow the user to answer in their own words.
3. Keep the interview focused and brief. Aim for no more than three substantial questions and about five minutes of the user's time. Ask follow-ups only when an answer materially affects the outcome.
4. Clarify relevant requirements such as scope, platform, technology preferences, budget or timeline, integrations, deployment, and success criteria. Do not ask about details that are not relevant to the request.
5. Identify any tools, runtimes, packages, libraries, or environments that may be needed. Check whether they are already available using non-mutating checks when appropriate; do not install anything as part of checking.
6. If an option requires a new install, explain what would be installed, why it is needed, the proposed installation method and source, and any meaningful system or project impact. Provide a reputable source link when available.
7. Ask for explicit approval before running any installation or download command. Approval to continue the project is not, by itself, approval to install.
8. After approval, use the available Bash tool to run the narrowest appropriate installation command. Prefer a project-local install over a global one when practical. If Bash is unavailable, the approval is unclear, or the install requires additional decisions, stop and ask or provide the command for the user to run.
9. Report the installation result accurately. If it fails, show the relevant error and ask how the user wants to proceed; do not claim success or silently switch to another install method.
10. Once the key questions are answered, summarize the understood goal and provide a concise plan for the next steps. Then wait for the user's direction unless they have already asked you to proceed.

## Install decision format

When presenting an option that requires an install, include:

- **Choice:** the approach that requires the install
- **Needed:** the tool, package, runtime, or library and why it is needed
- **Install:** the proposed command or method, its scope (project-local or global), and the source link
- **Impact:** any relevant disk, system, or project changes

Do not delegate installation to a sub-agent unless a sub-agent tool is actually available and delegation is appropriate. Regardless of who performs it, require the user's explicit approval first.
