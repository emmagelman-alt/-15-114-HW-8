On the upside, my skill worked and claude was able to read and invoke it. Onthe downside, it used it at the wrong time. I was unsure about how to proceed with the MCP portion of the assignment so I asked claude to help me understand the instructions (pasing some of the writeup into claude_  and what was required, as well as plan out what I wanted to execute. Claude responded by calling the skill I had just written and immedietly moving on to the planning and building questions, gearing up for install, and suggesting what to build and that it would build it for me. In this instance, I first wanted help understanding the instructions and how to execute.  I think this was a problem on both my end and on my skill's end. When I pasted the instructions and asked for help planning, claude matched a part of my prompt to the requirnments for applying the skill. While this issue could be resolved with better prompt engineering or switching my skill to be manually called instead of auto, I wanted to tweak the skill to be foolproof for others who may not have a technical background or arent experienced with prompt engineering, and auto. 

To resolve this, I worked with VS code to add in a clause about order of operations. The majority of the skill remains the same as befoere, however if the user mentions the need for help understanding or clarifying or explanation of any sort in addition to the ask for planning or executing in the same prompt, the skill instructs the agent ot first deal with the issue of the user's understanding and explantion in a conversational manner before acting on the planning/executing step. THis way, the user is nto immedietly overhwlemed by choices they dont undrstand how to make or they receive an answer they didnt ask for and the skill makes the gaent a burden instead of being helpful. 

here is what was added to due diligence. I wrote out exactly what I wanted in vs copilot and then had copilot rephrase and spell check to make it as clear a spossible for the agent ot understand how to proceed. 

"## Understanding questions take priority 
If the user's prompt says they do not understand, are confused, or want something explained or worked through (for example, “I don't understand,” “can you help me understand this,” “I'm confused,” “explain,” or similar phrasing), address that first in a natural, conversational response. This applies even when the same prompt later asks to plan or build something: explain the missing information without starting this skill's interview, plan, or implementation, then wait for the user to confirm they understand and ask to continue in planning or build mode. On that follow-up, resume this skill using the context the user already provided. If they only asked for an explanation and did not ask to plan or build, answer normally without starting the due-diligence workflow."

After I implemented this change, I opened a new session in claude code and fed it the same prompt as I did the first time "i am a little confused on the second part of the hw which is to build/ make an mcp server. i am including a portion of the instructions, can you help me work through and plan what i need to do? 

----
"Step 4: Build your MCP server (75 minutes)
Start from a quickstart in the [MCP docs](https://modelcontextprotocol.io/) and get a single tool returning something, anything, before you wire in real data. Run it standalone first and confirm it starts without errors.
Write the tool's docstring with as much care as the skill's description. Remember that this is what the agent reads when deciding whether to call it.
Step 5: Register it and confirm your agent calls it (30 minutes)
Add your server to your client's config, restart the client, and verify the tool appears in the agent's available actions. Then ask a question that should make it call your tool, and confirm it actually did rather than answering from its own knowledge.
The format differs by client, so check your tool's current docs. For Codex, the CLI and the VS Code extension share one file at `~/.codex/config.toml`, and a stdio server is three lines:
```
[mcp_servers.my-notes]
command = "python"
args = ["C:/full/path/to/my_notes_server.py"]
```
In the extension you can open that file from the gear menu under MCP settings → Open config.toml. Use forward slashes even on Windows, since backslashes need escaping in TOML. Claude Code, Cursor, and the rest use JSON instead, but they all want the same three things: a name, a command, and the arguments to pass it.
This is the step most likely to go wrong. Common causes: a JSON or TOML typo, a relative path where an absolute one was needed, the wrong Python interpreter, or a server that writes to stdout and corrupts the protocol (log to stderr instead)."

-------

This time, claude explained how mcps work, what I needed to do, gave me definitions. Then it gave me a setp by step plan , what I would nee dot install to make sure the process went smoothly, and the option for proceeding to build phase and deciding the project. 
