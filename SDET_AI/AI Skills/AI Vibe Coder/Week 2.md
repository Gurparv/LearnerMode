Vibe Coding
1. AGENTS.md
2. SKILLS.md
3. MCP
4. PLAN.md
5. DB_MODEL.md

Be descriptive about debugging and remember the rules.

- The context of our interaction when using Agents gets filled as we continue to talk to it. SO be obsessed with fixing it. one of the best ways is to clear the chat and start afresh.
- Git clean and git checkpoints

Claude commands
1. /init - to make claude write its own CLAUDE.md
2. Note - Instructor suggests to write your own CLAUDE.md instead of letting Claude write it
3. /context - tells you how much of context you have left.
4. Ask Claude to read PLAN.md
	1. /compact -> compacts your context for efficiency
5. /status
6. /models 
7. /help
8. /stats
9. /permissions -> .claude folder permission
10. You can link docs in CALUDE.md file by using @docs/PLAN.md: this will insert content of PLAN.md inside the CLAUDE.md

Flexible Workflows
2 levels of granularity within CLAUDE Code.
	-Session (/resume)
	-Checkpoint(/rewind)
	And Git commits (the gold standard)

- /rename -> renames the session so you can /resume the session anytime you want
- Ctrl+O -> to see extra information of what claude did behind the scenes

---

Claude code plugins -> Ralph Loops

3 Ways to give Claude Code new abilities
1. MCP -> Connect Claude code to someone else tools
2. SKills -> Add expertise and capabilities
3. Plugins -> Convinient bundles of MCP, Skills and More
This innovation comes from the 'Tools' part of 4 pillars which we discussed at the start of the course
Earlier people used to use LangChain but then claude noticed that if we have more tools we can add more functionality to Claude hence they come up with 'MCP' to give Claude more abilities by connecting to Tools in a easy general way by passsing LangChain
Now think about Playwright MCP //project idea to create an MCP for a tool I created,

MCP Technicalities
1. MCP Host eg CLaude Code
2. MCP Client eg Inside Claude Code
3. MCP server eg the Tools written by someone else eg Playwright MCP offers Connection to playwright (The Tool)
They can run in 2 way (transport) 
- Local (downlaod Playwright locally)
- Remote(some Atlassian MCP running on their server)

MCP guide=
1. Install MCP from the marketplace
2. Just to be sure that LLM, use your tool .. Once installed, instruct Claude to use it-> Eg 'use context7 to summarize the right way ti use OpenAI Agents SDK'

/mcp -> shows installed MCPs

Skills was introduced after MCP ; primarily focussed on instructions as Markdown files rather than tools. Its 
- Lightweight
- 'Progressive Disclosure' reduces context overload
- Support running scripts locally; this provides an alternative type of tools

TODO-> Lecture 49 : 3 levels of progressive Disclosure'
Anthropic has its Guide to make Skills,md on Github
skills.sh

Plugins:
The highest level cosntruct. A bundle of features that can include MCP servers, skills, commands along with other Claude Code features not yet covered.
Only availavble in Claude Code,
Instructior suggest to 'Start with Plugin instead of MCP and skills.md'
/plugin=> shows installed plugins

day2-

What is Issue Tab in Github?
Try to identify your general high level workflow and try to find ways to incorporate AI into it.
- 'Feature-dev' Claude plugin
Instructor used Github mcp, and used feature-dev of claude to build softwares using these.From jira creation in claude to github that too in claude.
```
Read jira issue (Atlassian MCP) --> Implement (feature-dev-plugin) --> create PR (Github MCP) ====> All this from inside Calude code terminal.
```

/feature-dev: feature-dev please implement jira issue TCT-11 with a NextJs application in a directory called frontend, then raise a PR when done.

Debugging Stragtegy:
1. Do a git commit (so you can go back if claude starts hallucinating)
2. paste the stack trace and ask calude/LLm to fix it
3. Guide with debug.md
	1. Ask it to reproduce the issue consistently
	2. Ask it to Investigate and hypothesis
	3. Ask it demonstrate root cause
	4. Ask it to fix and prove
	5. lessons learned in claude.md
4. Use diff LLm to review or test as it has fresh pair of eyes
5. Or consider skills.md like this -> skills.sh/obra/superpowers/systematic-debugging

Claude.md in home directory - lecture 59, 60
Lecture-62 -> notice instructor asks changes to be updated in claude.md so that it gets better along the way. he used it when /context is 70% full so he modified the claude.md which compresses things and then clear the context to 0 and start with 0 token again.so we pick from where we left last time.
'Cerebras' is fast doesnt need streaming. Google it
Project idea -> build your own SaaS product.

---

































