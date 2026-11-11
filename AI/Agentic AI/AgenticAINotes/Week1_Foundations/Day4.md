### Agentic AI frameworks
- No framework(where you make direct API calls to different LLMs) and MCP(Model Context Protocol )
- Lightweight frameworks : OpenAI Agents SDK and Crew AI 
- Heavy Weight framework : LangGraph and AutoGen

### Resources
- We can provide an LLM with resources to ==improve its expertise==.
- Basically, just means ==shoving data== relevant to the question into  the prompt
- There are techniques like RAG to get really smart at picking ==relevant content==

### "Tools" give LLMs autonomy
- Give an LLM the power to carry out actions like ==query a database== or ==message other LLMs==
- Sound spooky right, but its not the reality.. watch the below explanation 👇

In Theory
![[Pasted image 20250725120711.png]]
In Reality -
![[Pasted image 20250725120736.png]]

Example of this in real life -
![[Pasted image 20250725120859.png]]

---

## Pydantic (used for Multi-LLM Pipeline)

