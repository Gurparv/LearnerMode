🎭 Playwright has TWO MCP servers. Most people only know one.  
  
As someone neck-deep in QA automation, this distinction matters a lot. Let me break it down:  
  
-----------  
🔵 @playwright/mcp — The Browser Automation MCP (Install separately · npx @playwright/mcp@latest)  
  
Uses structured accessibility snapshots to let LLMs interact with web pages — no screenshots, no vision models needed.  
  
✅ Use this when:  
-You need an AI agent to browse, fill forms, scrape, or navigate the web  
-You're building coding agents that verify their own work in a browser  
-You want GitHub Copilot's Coding Agent to interact with your localhost app  
-You need lightweight, token-efficient browser control  
  
This is the general-purpose browser automation layer. Think of it as giving your AI a browser.  
  
  
-------------  
🟠 Playwright Test MCP — The Testing-Native MCP (No install needed · built into Playwright test itself)  
  
This one starts running when you use the Playwright Agents — Planner, Generator, and Healer. It has similar tools to the browser MCP but also includes testing-specific ones you'd only need when actually testing. Currently supports TypeScript/JavaScript only.  
  
✅ Use this when:  
- You're using playwright test with AI agents  
- You want to auto-generate, plan, or heal Playwright test code  
- You need the Healer Agent to fix broken selectors automatically  
- You're in a pure test authoring + maintenance workflow  
  
This is the test-aware layer. It knows the difference between a page action and a test assertion.  
  
  
My take:  
You can use one or the other depending on your needs — and the Playwright Test MCP handles its own setup, so you don't need to worry about conflicts with other MCP servers.  
  
  
Two tools, two jobs. Know which one you're reaching for.