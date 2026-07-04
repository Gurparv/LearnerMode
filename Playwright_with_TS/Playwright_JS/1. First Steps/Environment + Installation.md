## Introduction

Playwright Test is an end-to-end test framework for modern web apps. It bundles test runner, assertions, isolation, parallelization and rich tooling. Playwright supports Chromium, WebKit and Firefox on Windows, Linux and macOS, locally or in CI, headless or headed, with native mobile emulation for Chrome (Android) and Mobile Safari.

Q. Whats the difference between Typescript and Javascript?

| JavaScript                                                      | TypeScript                                        |
| --------------------------------------------------------------- | ------------------------------------------------- |
| Plain scripting language that runs directly in browsers/Node.js | Superset of JavaScript with **static typing**     |
| No type checking                                                | **Types catch errors before running code**        |
| Files: `.js`                                                    | Files: `.ts`                                      |
| Runs directly                                                   | Must be **compiled to JavaScript** first          |
| Easier to start                                                 | Better **tooling, autocomplete, maintainability** |
### Simple Examples

**JavaScript**
```javascript
function add(a, b) {
  return a + b;
}
```

TypeScript
```Typescript
function add(a: number, b: number): number {
  return a + b;
}
```

TypeScript ensures `a` and `b` are numbers **before runtime**.
### For Playwright

Both work, but:
- **JavaScript** → simpler setup
- **TypeScript** → better **IDE autocomplete + safer tests**

### Practical advice

If you're learning **Playwright seriously → use TypeScript**. Most modern test repos use it.

✅ Better editor hints  
✅ Fewer runtime bugs  
✅ Easier large test suites

---

### ## Installing Playwright
```Bash
npm init playwright@latest 
```


![[Pasted image 20260305110042.png]]
![[Pasted image 20260305110304.png]]

## Some CLI commands 

1. To Run all tests(Headless mode) -> `npx playwright test`
2. To Run all tests(Headed mode) -> `npx playwright test --headed`
3. To show last HTML report run: `npx playwright show-report`
4. Start the UI interactive UI mode: `npx playwright test --ui`
5. Runs the tests only on Desktop Chrome: `npx playwright test --project=chromium`
6. Run tests on different browsers:
	 `npx playwright test --project webkit --project firefox`
7. Runs the tests in specific file:`npx playwright test landing-page.spec.ts`
8. Run set of test files from different directories, pass in the directory names that you want to run the tests in.`npx playwright test tests/todo-page/ tests/landing-page/`
9. Run files that have *landing* and *login* in the file name
	`npx playwright test landing login`
10. To run a test with a specific title, use the `-g` flag followed by the title of the test.
	`npx playwright test -g "add a todo item`
11. Runs the test in debug mode:`npx playwright test --debug`
12. Auto generate tests with Codegen:`npx playwright codegen`
13. To run only the tests that failed in the last test run, first run your tests and then run them again with the `--last-failed` tag
	`npx playwright test --last-failed`

## Note
And check out the following files:
- .\tests\example.spec.ts - Example end-to-end test
- .\playwright.config.ts - Playwright Test configuration

![[Pasted image 20260305120256.png]]

The [playwright.config](https://playwright.dev/docs/test-configuration) centralizes configuration: target browsers, timeouts, retries, projects, reporters and more. In existing projects dependencies are added to your current `package.json`.

`tests/` contains a minimal starter test.

---

Q. Why do we even need `package-lock.json` when we have `package.json`?
**Short summary:**
- **`package.json`** → defines **dependency ranges** your project needs.
- **`package-lock.json`** → locks the **exact versions installed**.

**Why both?**
`package.json`
```
"@playwright/test": "^1.42.0"
```
means **1.42.0 or newer minor versions**.

`package-lock.json`

```
"@playwright/test": "1.42.3"
```

ensures **everyone installs exactly 1.42.3**.

✅ Result: **consistent installs and stable Playwright tests.**

---

## Running the Example Test

By default tests run headless in parallel across Chromium, Firefox and WebKit (configurable in [playwright.config](https://playwright.dev/docs/test-configuration)). Output and aggregated results display in the terminal.