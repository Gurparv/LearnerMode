1. [[#Day 1]]
2. [[#Day 2]]

# Day 1
## Cursor Tool

## Who is this for
1. Aspiring Engineer
2. Senior Staff Engineer

## By the end of this course you will be able to:
- Build , deploy and enhance software products at any scale.
- Take maximum advantage of Agentic Coding - respond to Karpathy
- Apply to roles that require Agentic Coding Skills

### Most of Ed Donner courser are about using code to make AI Agents But this course is about using AI agents to make Code.


---
## Syllabus
Week 1: Vibe Coding
Week 2: Vibe Engineering as a professional
Week 3: Agentic Engineering as an expert

![[Pasted image 20260428155616.png]]

---

## Setting the Scene
There are 3 interfaces to writing software with Agents
1. IDE (Cursor, Codex, Antigravity, Windsurf)
2. Plugin (Github copilot)
3. CLI (Claude Code, Cursor CLI, Codex CLI, Gemini CLI , OpenCode, Amp)

### Evolution of the Programmer in 2024-2026 by Steve Yegge
![[Pasted image 20260428155259.png]]

Instructor tip -> Everything is changing fast. Keep an eye on the resources for new updates.
Don't be distracted by the hype.  Remove noise from real information.

---
# Day 2

## Basic Knowledge
#### 1. LLM - 
- Predicts most likely text to follow an input.
- Its a pattern matcher that uses statistics based on vast training datasets.
- The input is a sequence of tokens and output is probability of next token.
- Called repeatedly to generate a token at a time.

#### 2. AI Application
- A product that uses an LLM to achieve a business goal
- Eg ChatGPT, Cursor Agent, Duolingo Max, Atlassian Rovo.

#### 3. Fancy Autocomplete with Tricks
![[Pasted image 20260428161402.png]]
![[Pasted image 20260428161638.png]]

#### 4. What is an AI Agent?
An Agent runs Tools in a Loop to achieve a goal.

#### 5. Context Engineering
The Output of an LLM is based entirely on its input (aka 'context')
Getting this right is everything !
Previously called `Prompt Engineering`, but as the inputs became more complex, this became `Context Engineering`

##### Components of the Input -
- System Prompt : overall framing.
- Tools : description of capabilities.
- Memory: resources that persist
- ==AGENTS.md==
- Conversation History/Messages
	1. User Messages
	2. LLM reasoning
	3. LLM replies
	4. Code generated
	5. Tools called
	6. Results of code and tools.

##### Context Window
An LLM has a limit to how many tokens it can examine in its input; input longer than this will fail.

![[Pasted image 20260428163118.png]]

`Compacting` is the feature built into these tools like Claude Code.
![[Pasted image 20260428163222.png]]

