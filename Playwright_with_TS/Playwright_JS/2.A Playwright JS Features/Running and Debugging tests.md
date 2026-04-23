1. [[#Introduction]]
2. [[#Running Tests]]
3. [[#Debugging Tests]]
## Introduction

With Playwright you can run a single test, a set of tests, or all tests. Tests can be run on one browser or multiple browsers using the `--project` flag. Tests run in parallel by default and in headless mode, meaning no browser window opens while running the tests and results appear in the terminal. You can run tests in headed mode using the `--headed` CLI argument, or run your tests in [UI mode](https://playwright.dev/docs/test-ui-mode) using the `--ui` flag to see a full trace of your tests.


---

## Running Tests

| **Topic**                                                                              | **Command**                                                |
| -------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| CLI command to run tests (Headless and parallel by default)                            | `npx playwright test`                                      |
| Run tests in Headed Mode                                                               | `npx playwright test --headed`                             |
| Run tests in UI Mode                                                                   | `npx playwright test --ui`                                 |
| Run tests in different browsers                                                        | `npx playwright test --project webkit --project firefox`   |
| Run single test file                                                                   | `npx playwright test landing-page.spec.ts`                 |
| Run test files from diff directories                                                   | `npx playwright test tests/todo-page/ tests/landing-page/` |
| Run test files with name 'landing' or 'login' in the filename                          | `npx playwright test landing login`                        |
| Run a test with a specific title, use the `-g` flag followed by the title of the test. | `npx playwright test -g "add a todo item"`                 |
| Run last failed tests                                                                  | `npx playwright test --last-failed`                        |
####  Run tests in VS Code
Tests can be run right from VS Code using the [VS Code extension](https://marketplace.visualstudio.com/items?itemName=ms-playwright.playwright). Once installed you can simply click the green triangle next to the test you want to run or run all tests from the testing sidebar. Check out our [Getting Started with VS Code](https://playwright.dev/docs/getting-started-vscode) guide for more details.


---

## Debugging Tests

Since Playwright runs in Node.js, you can debug it with your debugger of choice, e.g. using `console.log`, inside your IDE, or directly in VS Code with the [VS Code Extension](https://playwright.dev/docs/getting-started-vscode). Playwright comes with [UI Mode](https://playwright.dev/docs/test-ui-mode), where you can easily walk through each step of the test, see logs, errors, network requests, inspect the DOM snapshot, and more. You can also use the [Playwright Inspector](https://playwright.dev/docs/debug#playwright-inspector), which allows you to step through Playwright API calls, see their debug logs, and explore [locators](https://playwright.dev/docs/locators)
#### Debug tests in UI mode

We highly recommend debugging your tests with [UI Mode](https://playwright.dev/docs/test-ui-mode) for a better developer experience where you can easily walk through each step of the test and visually see what was happening before, during, and after each step. UI mode also comes with many other features such as the locator picker, watch mode, and more.

[[Running Tests in UI Mode]]

####  Debug tests with the Playwright Inspector

| **Heading**                                                                                                                                                                             | **Command**                                      |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| Debug all tests                                                                                                                                                                         | `npx playwright test --debug`                    |
| Debug one test file                                                                                                                                                                     | `npx playwright test example.spec.ts --debug`    |
| To debug a specific test from the line number where the `test(..` is defined, add a colon followed by the line number at the end of the test file name, followed by the `--debug` flag. | `npx playwright test example.spec.ts:10 --debug` |
Check out our [debugging guide](https://playwright.dev/docs/debug) to learn more about debugging with the [VS Code debugger](https://playwright.dev/docs/debug#vs-code-debugger), UI Mode, and the [Playwright Inspector](https://playwright.dev/docs/debug#playwright-inspector) as well as debugging with [Browser Developer tools](https://playwright.dev/docs/debug#browser-developer-tools).

