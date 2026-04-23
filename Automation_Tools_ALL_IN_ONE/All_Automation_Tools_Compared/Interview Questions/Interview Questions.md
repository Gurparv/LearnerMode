Playwright concepts:  
1. Custom Test Fixtures & Global Setup/Teardown?  
• Use test.extend() for custom fixtures • Add globalSetup and globalTeardown in playwright.config.ts • Example: Login fixture that auto-authenticates before each test  
  
2. Multi-Tab Workflows & Browser Contexts?  
• browser.newPage() → Same context, multiple tabs • browser.newContext() → Isolated sessions for different users • Use cases: Testing multi-user scenarios, different roles  
  
3. Workers vs Sharding?  
• Workers: Parallel tests on single machine (CPU cores)  
• Sharding: Distribute tests across multiple machines  
• Choose workers for single machine, sharding for large CI/CD farms  
  
4. Network Interception for Testing?  
• Use page.route() to intercept requests  
• Performance: Block resources, mock slow responses  
• Fault injection: Abort requests, return 500 errors  
  
5. Manage Auth Sessions at Scale?  
• Login once in globalSetup, save to state.json  
• Reuse: browser.newContext({ storageState: 'state.json' })  
• Result: 10x faster test execution  
  
6. Visual Regression Testing?  
• Use toHaveScreenshot() assertion  
• First run: Creates baseline  
• Subsequent runs: Compares against baseline  
  
7. Handle Unpredictable Dynamic Elements?  
• locator.waitFor() with custom conditions  
• page.waitForFunction() for JavaScript-based waits  
• Goes beyond built-in auto-waiting  
  
8. Debug Flaky Tests?  
• Enable trace: 'on-first-retry' in config  
• Open Trace Viewer for step-by-step analysis  
• View: Screenshots, DOM, network, action logs  
  
9. CI/CD Integration & Reports?  
• Run: npx playwright test in pipeline  
• Built-in HTML reporter  
• Integrate Allure for interactive visualisations  
  
10. API Testing Alongside UI?  
• Use request fixture for API calls  
• Pattern: API for setup → UI interaction → API for validation  
• Example: Create user via API, test UI flow, verify via API  
  
11. Complex Locator Strategies?  
• Priority: getByRole(), getByText()  
• Regex: getByText(/partial/i)  
• Chain: page.locator('parent').locator('child')  
• Fallback: data-testid attributes  
  
12. Measure Page Performance?  
• Use page.evaluate() to access Performance API  
• TTFB: responseStart - requestStart  
• Analyze: performance.getEntries() for resource timing  
  
13. Playwright with Java/Python?  
• Same API concepts, different syntax  
• No await in Java/Python (synchronous calls)  
• Better type safety in Java/TypeScript  
  
14. Build Resilient Framework?  
• Implement Page Object Model (POM)  
• Create modular helpers for common actions  
• Use auto-waiting + explicit waits strategically  
• Keep tests isolated and independent  
  
15. Keep Tests Fast & Maintainable?  
• API testing for setup/validation  
• Parallel execution with workers  
• Reuse authenticated sessions  
• User-facing locators (avoid brittle selectors) • Regular refactoring