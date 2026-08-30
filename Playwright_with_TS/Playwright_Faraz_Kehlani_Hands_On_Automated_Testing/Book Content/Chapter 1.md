Quick Setup Refresher, serves as an entry point for you and offers a concise refresher on setting up Playwright and writing basic tests. It ensures you can quickly get a testing environment running and understand Playwright’s core structure.

## Playwright biggest strengths
- Automate Multiple browsers with Single API
- Auto Wait mechanism which reduces flaky tests
- Support in multiple languages such has JS, Python and C# etc

## Key Topics 
1. [[#Installing Playwright and dependencies]]
2. [[#Understanding difference between Playwright Test and Playwright Library]]
3. [[#Writing and Running your first test]]
4. [[#Configuring Test environments]]
5. [[#Understanding Playwright test runner basics]]

## Understanding difference between Playwright Test and Playwright Library
A common question among newcomers is: What is the difference between Playwright Test and the Playwright Library? Although they have the same capabilities, each is suitable for different use cases

Imagine you’re building a data extraction pipeline that scrapes content from multiple sites every night. You don’t need full test reports or assertions. You just want reliable browser automation. In that case, the Playwright Library fits perfectly. You can plug it into your existing Node.js workflow, schedule it with cron, and keep things lightweight.

Now, suppose you’re developing a web application and want to ensure your login, checkout, and dashboard workflows remain reliable across Chrome, Firefox, and Safari. Playwright Test handles the orchestration: running tests, generating reports, and making debugging easier without additional setup.

To be more exact, the Playwright Library gives you a set of APIs to automate browser tasks. You can use it to do the following:
- Launch browsers in headless or headed mode
- Interact with web pages by clicking, filling in forms, and capturing screenshots
- Execute JavaScript in the browser’s context.
This API can be combined with any test runners, such as Jest or Mocha, or even used in custom scripts. The design focuses on browser automation and leaves test orchestration and reporting up to you

On the other hand, Playwright Test builds on top of the core library but adds features for making writing tests easier. It has features such as the following: 
- Built-in test runner to recognize test files automatically, run them in parallel, and support multiple browsers 
- Generate visual reports and debug test failures via the CLI 
- Command-line options to run tests, record videos for debugging failures, and more

So, use the Playwright Library if you already work within another test framework that you trust or need to integrate browser automation into a larger process. If your focus is on quickly writing tests and using an all in one solution, Playwright Test is a better option.

## Installing Playwright and dependencies

laywright is built on top of Node.js, so verifying that Node and npm (or yarn) are available is the first step
### 1. Installing Node.js
```Shell
node --version
npm --version
```

### 2. Initializing your project

Create a new project directory and initialize it as an npm project:
```shell
mkdir playwright-quick-setup 
cd playwright-quick-setup 
npm init -y
```
This command creates a package.json file, which is needed to manage your project’s dependencies.

### 3. Installing Playwright
As we discussed earlier in this chapter, there are two main ways to install Playwright: Playwright Library and Playwright Test.

#### A) To install the Playwright Library, you can use the following command:
```shell
npm install playwright
```
This installs the core Playwright library, which gives you the browser automation API. It’s suitable if you want to use Playwright’s automation capabilities programmatically or integrate it with other testing frameworks.

#### B) If you prefer an integrated testing solution, install the following:
```shell
npm install --save-dev @playwright/test
```

This installs the Playwright Test package, which includes a built-in test runner, assertions, and features like parallel execution.

### Note : 
Note that the preceding command only installs the @playwright/test package as a dev dependency in your existing project. It does not create configuration files or example tests or initialize any project structure. Also, it does not install browser binaries automatically (you need to run npx playwright install separately).

##### A) Use this approach when you’re adding Playwright Test to an existing project that already has a testing setup or if you prefer to configure Playwright manually. You will also need to set up the `playwright.config.ts` file and organize the test structure on your own.

#### B) If you want a guided setup with configuration and examples, or want to save time by letting Playwright scaffold the project for you, use the following:
```shell
npm install playwright@latest
```

This command initializes a new Playwright project with the Playwright Test framework. It sets up a complete testing environment, including the following:
- Installing @playwright/test as a dev dependency 
- Creating a sample configuration file (playwright.config.ts) 
- Generating example test files (such as tests/example.spec.ts) 
- Optionally installing browser binaries (if you choose to do so during the setup prompts)

---
## Writing and Running your first test

#### 1. Setting up a simple test file
```Typescript title="example.spec.ts"

import {test, expect} from '@playwright/test';
test('homepage has Playwright in title', async({page}) => {
	// Navigate to the playwright homepage
	await page.goto("http://playwright.dev");
	
	// Fetch the title of the page.
	const title = await page.title();
	
	// Assert that the title contains 'Playwright'
	expect(title).toContain('Playwright');
});
```

This simple test uses Playwright Test’s API to define a new test, then launches a browser page and navigates to the Playwright home page. Next, it retrieves the page title and asserts that it contains the Playwright keyword.

#### 2. Running the test
To run your test, execute the following command in your terminal:
```shell
npx playwright test
```
The test runner will scan your project directory, find your test file, launch the appropriate browser, execute the test, and then output a report.

You can also tell Playwright to run a specific test like this:
```shell
npx playwright test tests/example.spec.ts
```

In addition, you can enable debugging mode with the following:
```shell
npx playwright test --debug
```

This command opens an interactive inspector to help you troubleshoot any issues that might arise during test execution

==We’ll dive deeper into debugging in Chapter 8, Headless Testing and Debugging.==

By default, Playwright runs tests in headless mode, meaning the browser UI is not shown. In headed mode, the browser UI is displayed during test execution. This is useful for debugging or when visual confirmation is necessary

You can enable it with the following:
```shell
npx playwright test --headed
```

You can also do so by modifying the test config (`playwright.config.ts`):
```Typescript
use: {
	headless: false,
}
```

Playwright supports multiple browser engines: 
- Chromium (used in Chrome and Edge) 
- Firefox 
- WebKit (used in Safari)

To run tests in a specific browser, you can use CLI flags like this:
```shell
npx playwright test --project=chromium 
npx playwright test --project=firefox 
npx playwright test --project=webkit
```

Alternatively, you can define projects in `playwright.config.ts`:
```Typescript
projects: [ 
{ name: 'chromium', use: { browserName: 'chromium' } },
 ],
```
This code tells Playwright to run the test on Chromium only

#### Interpreting test results 
After running the tests, you will be able to see an informative summary by running the npx playwright show-report command. This summary includes the total number of tests executed, the browser(s) used for testing, and the execution time, which helps you determine whether parallelization or test optimization is needed (we’ll dive deeper into this in Chapter 6, Test Parallelization and Performance Optimization).

You’ve just gone from zero to executing an end to end test in just a few commands! Now, let’s take things further by configuring your test environments, which is an important step in building reliable end-to-end tests.

---
## Configuring Test environments

In this part, we look at configuring the Node.js environment and your Integrated Development Environment (IDE) for an effective Playwright development experience.

### 1. Setting up the Node.js environment
Make sure you’re using a stable version of Node.js, ideally the LTS version, and consider using tools such as `nvm` to manage different Node versions, which can be helpful when working on multiple projects.

It’s also important to keep your project structure organized so everything stays clear and easy to navigate. While there isn’t one perfect way to organize a Playwright project, here’s an example layout to give you some inspiration:

```text
my-playwright-project/
│
├── tests/                           // Test files
│   ├── example.spec.ts              // Test files for different scenarios
│   ├── logged-in/
│   │   ├── api.spec.ts
│   │   ├── login.setup.ts
│   │   └── ...
│   └── logged-out/
│       ├── api.spec.ts
│       ├── auth.spec.ts
│       └── ...
│
├── src/
│   ├── pages/
│   │   ├── BasePage.ts              // Common page functions and elements
│   │   ├── DashboardPage.ts         // Page Object Model for the dashboard
│   │   └── ...
│   │
│   └── utils/
│       ├── apiHelper.ts              // Utility functions for API calls
│       ├── stringUtils.ts            // Additional helpers
│       └── ...
│
├── fixtures/
│   └── testData.json                // Sample data used for tests
│
├── auth/
│   └── credentials.json             // Holds credentials and session data
│
├── helpers/
│   └── list-test.ts                 // Helper functions
│
├── test-results/                    // Stores test execution results
├── playwright-report/               // Directory for Playwright test reports
│
├── playwright.config.ts             // Playwright configuration settings
├── package.json                     // NPM package manifest
├── tsconfig.json                    // TypeScript configuration
├── .gitignore                       // Files to exclude from version control
└── README.md                        // Project overview and documentation
```


Let’s dive a bit deeper: 
- Configuration lives in `Root`: your TS compiler options, `playwright.config.ts`, environment variables, plus your `package.json` and `.gitignore`. Docs and top-level scripts belong here too. 
- In `tests/`, we’ve grouped `logged-in` and `logged-out` scenarios into subfolders so you can share setup logic (such as `login.setup.ts`) and keep related specs together. 
- `src/` is the heart of your Page Object Model (POM). `pages/` holds individual page classes, while `utils/` is home to low-level helpers and shared API logic. 
- `fixtures/` holds static or semi-static test data (JSON, CSV, etc.) that your tests can load. 
- `auth/` contains credentials, session dumps, tokens, or anything sensitive or environment-specific you don’t want scattered through your code. 
- `helpers/` holds one-off or cross-cutting functions that don’t fit neatly in `utils/`, such as list generators or custom matchers. 
- Finally, auto-generated output, such as raw JSON logs, HTML reports, screenshots, and videos, is stored in `test-results/` and `playwrightreport/`. 

 This organization keeps your test code, helpers, and configuration clearly separated, so when the project grows, you always know where to look, and more importantly, where to add new files.

### 2. Setting up your IDE
Using a modern IDE such as **Visual Studio Code (VS Code)** can improve your coding experience. Start by installing helpful extensions such as the official Playwright Test extension, which provides syntax highlighting, code completion, and inline test results:

![[Pasted image 20260830105913.png]]

You can also add `ESLint` and `Prettier` for code formatting, which help keep your code consistent. Setting them up is pretty similar to how you installed Playwright Test for VS Code.

### 3. Configuring Playwright settings

Playwright allows you to customize how your tests run by using the `playwright.config.ts` file. In this file, you can set global preferences, tweak browser behavior, and fine-tune how your tests are executed. This section will guide you through the key settings to help you get started.

First, go to your project directory. If you don’t have a `playwright.config.ts` file yet (maybe you’re working with an existing project), you can create the config file manually.

The following is an example of a minimal configuration:
```Typescript title="playwright.config.ts"
import { defineConfig } from '@playwright/test';
export default defineConfig ({
	testDir: './tests', // Directory where tests are located
	timeout: 30_000, // Test timeout in milliseconds
	use: {
		browserName: 'chromium', //Default browser
		headless: true, // Run tests in headless mode
		viewport: {width: 1280, height: 720}, // Default viewport size
		},
});
```

Once the initial configuration is in place, you can begin customizing it to better suit your project’s specific testing needs.

The configuration file supports a variety of options to customize test execution. When you’re setting things up, it’s best to keep it simple at first. Start with the basic settings, and only add complexity if you need it later. Also, make sure to document your choices by adding comments in the config file. This way, you can easily remember why certain settings were made, and it’ll be clearer for anyone else who works on it later.

The following are the most commonly used settings. We’ll come back to many of these in later chapters, so no worries if you’re not totally sure how they work just yet.

#### 1. Test directory and file matching

Use these options to control which files Playwright includes or excludes when discovering tests:
- `testDir`: Specifies the directory containing your test files. By default, Playwright looks for tests in the `./tests` folder. 
- `testMatch`: Defines a pattern to match test files (such as `*.spec.ts` or `/*.test.ts`). 
- `testIgnore`: Excludes files or directories from test discovery (such as `/*.setup.ts`).

The following is an example:
```Typescript title="playwright.config.ts"
export default defineConfig({ 
testDir: './tests', 
testMatch: '/*.spec.ts', 
testIgnore: '/*.unit.ts', 
});
```

#### 2. Timeouts
These settings define how long Playwright should wait before timing out at different stages of the test run:
- `timeout`: Maximum time (in milliseconds) for a test to complete
- `globalTimeout`: Maximum time for the entire test suite to run
- `actionTimeout`: Timeout for individual Playwright actions (such as `page.click()`)

The following is an example:
```Typescript title="playwright.config.ts"
export default defineConfig({
 timeout: 30000, // 30 seconds per test 
 globalTimeout: 1800000, // 30 minutes for the entire suite 
 use: { actionTimeout: 10000, // 10 seconds per action 
 }, 
 });
```

#### 3. Browser and context options
The `use` property defines default browser and context settings for all tests:
- `browserName`: Specifies the browser (Chromium, Firefox, or WebKit)
- `headless`: Runs browsers in headless (`true`) or headed (`false`) mode
- `viewport`: Sets the default viewport size
- `locale`: Configures the browser’s language (such as `en-US`)
- `timezoneId`: Sets the browser’s timezone (such as `America/New_York`)
- `device`: Emulates a specific device from Playwright’s device list (such as `iPhone 16`)

The following is an example:
```Typescript title="playwright.config.ts"
export default defineConfig({
 use: {
	 browserName: 'firefox',
	 headless: false,
     viewport: { width: 1920, height: 1080 },
	 locale: 'en-GB',
     timezoneId: 'Europe/London',
     device: 'Desktop Firefox',
     },
});
```

### 4. Parallelism and workers
These options manage how tests are executed in parallel and across CPU resources:
- `workers`: Number of parallel test workers. Set to a number (such as `4`) or `'50%'` to use half the CPU cores.
- `fullyParallel`: Enables (`true`) or disables (`false`) running tests in parallel within a single file.

The following is an example:
```Typescript title="playwright.config.ts"
export default defineConfig({ 
	workers: 3, // Run 3 tests in parallel 
	fullyParallel: true, 
});
```

### 5. Retries and failure handling
These settings help control test retries and when the test run should stop after failures:
- `retries`: Controls how many times a failed test will be retried before it’s marked as failed
- `max failures`: Sets a global threshold for how many test failures are allowed before Playwright stops the entire test run

The following is an example:
```Typescript title="playwright/comfig.ts"
export default defineConfig({ 
	retries: 2, // Retry failed tests twice 
	maxFailures: 10, // Stop after 10 failures 
});
```

### 6. Reporters
Now we come to reporter. Playwright supports multiple reporters for test output. Options include `list`, `dot`, `line`, `json`, `junit`, `html`, or custom reporters.

The following is an example:
```Typescript title="playwright.config.ts"
export default defineConfig({ 
	reporter: [ 
		['list'], // Console output 
		['html', { outputFolder: 'playwright-report' }], // HTML report 
		['json', { outputFile: 'test-results.json' }], // JSON report 
		], 
	});
```

To view the HTML report, run the following:
```shell
npx playwright show-report
```

==Note== When Playwright runs in a CI/CD pipeline (which is usually headless), the command to open a browser may hang, which causes the entire pipeline job to get stuck and eventually time out. When running in CI/CD, explicitly set the `open` option to `'never'` for the HTML reporter in the configuration file:

```Typescript title="playwright.config.ts"
export default defineConfig({ 
	reporter: [
		['list'],
		['html', { outputFolder: 'playwright-report', open: 'never' }],
		['json', { outputFile: 'test-results.json' }],
		]
});
```

### 7. Projects for multi-browser testing
The `projects` property allows you to define multiple test configurations (such as for different browsers or devices). Each project inherits global settings but can override them.

The following is an example:
```Typescript title="playwright.config.ts"
export default defineConfig({ 
	projects: [ 
		{ 
			name: 'Chromium', use: { browserName: 'chromium' }, 
		}, 
		{ 
			name: 'Firefox', use: { browserName: 'firefox' }, 
		}, 
		{ 
			name: 'Mobile Safari', use: { device: 'iPhone 16' }, 
		}, 
		], 
});
```

Run tests for a specific project:
```shell
npx playwright test --project=Chromium
```

### 8. Debugging configuration issues
- If your tests fail because of a configuration issue. Start by checking the syntax to make sure your configuration file is correct in TypeScript.
- Next, check the logs by running the tests with the `--debug` flag using the `npx playwright test --debug` command to get a closer look at Playwright’s behavior.
- If you’re still stuck, try temporarily reverting to the default settings to help isolate the problem.
- Lastly, make sure you’re using the latest version of Playwright by running `npm install @playwright/test@latest` to stay up to date.

With your development and testing environments properly configured, you’re now ready to dive into the core functionality of Playwright.

## Understanding Playwright test runner basics
The Playwright test runner manages your tests, provides diagnostic utilities, and ensures that your testing script runs in various environments.

Playwright automatically detects files that follow its naming conventions (such as `*.spec.js` or `*.test.ts)`. This means that once your tests are in place, running the test runner will automatically aggregate them.

In this section, we’ll briefly explore key features of the test runner, such as built-in hooks, fixtures, and support for parallel execution.

#### 1. Using parallel execution and test isolation
Out of the box, Playwright’s test runner distributes your test files across multiple worker processes (typically one per CPU core) to take advantage of the full power of modern multicore systems. This concurrency cuts down the overall testing time, especially for large projects, by running several tests at the same time instead of waiting for one test to finish before starting the next.

Playwright lets you control the number of workers through configuration in your `playwright.config.ts`:
```Typescript title="playwright.config.ts"
import { defineConfig } from '@playwright/test'; 
export default defineConfig({
 workers: 4, 
 // … other settings 
});
```

Test isolation is important to ensure that the outcome of one test never affects another. In Playwright, isolation is achieved by using a fresh browser context for each test. Because each test gets its own browser context, any state (such as cookies, session data, or local storage) that is set by one test remains confined to that test alone.

This separation is done automatically by Playwright’s test runner. Even if one test logs in to an application, manipulates local storage, or alters cookies, these changes are within that specific context, which is important for avoiding flaky test outcomes.

#### 2. Using built-in hooks and fixtures
Playwright’s built-in hooks and fixtures are two features that make writing isolated tests much easier. Let’s explore them!

##### Hooks
Hooks are functions that run at specific moments during your test process. You can use them to initialize resources such as opening a database connection or getting your test data ready before your tests begin. When the tests are finished, hooks help you wrap things up: closing connections, cleaning up data, or logging useful info for next time.

Common hooks include the following:
- `test.beforeAll`: Runs once before all tests in a file or a group. This is the place for expensive setup tasks that need to happen only once. 
- `test.beforeEach`: Executes before each individual test. Perfect for things such as navigating to a starting page or ensuring a fresh state. 
- `test.afterEach`: Runs after every test and allows you to clean up resources or reset certain configurations. 
- `test.afterAll`: Runs once after all tests in a file or group, typically used for final cleanup.

For example, let’s say you want a script that logs in to a site and then runs two tests: one to confirm the inventory page’s title, and another to confirm that the shopping cart link is visible. Here’s how you can use the beforeEach hook to write this script:
```Typescript title="example.spec.ts"
import { test, expect } from '@playwright/test';

test.beforeEach(async ({ page }) => {
  await page.goto('https://www.saucedemo.com/');
  await page.getByPlaceholder('Username').fill('standard_user');
  await page.getByPlaceholder('Password').fill('secret_sauce');
  await page.getByRole('button', { name: 'Login' }).click();
  await expect(page).toHaveURL(/inventory.html/);
});

test('Check inventory page title', async ({ page }) => {
  await expect(page).toHaveTitle('Swag Labs');
});

test('Check shopping cart link is visible', async ({ page }) => {
  const cartLink = page.locator('.shopping_cart_link');
  await expect(cartLink).toBeVisible();
});
```

##### Fixtures
A fixture, on the other hand, is a pre-configured helper that sets up everything you need for your tests. It takes care of creating, configuring, and cleaning up resources. This means you don’t have to write the same setup code over and over.

When you define a test, you can specify the resources you need (such as page, browser, or custom ones), and Playwright will automatically provide them by running the necessary fixture functions.

For example, the `request` fixture gives you an `APIRequestContext` instance, which makes it easy to make HTTP requests and do API testing alongside your web interactions in the same test suite. You can use methods such as `request.get()`, `request.post()`, and `request.fetch()` to interact with APIs. It’s isolated for each test, so there’s no worry about shared state.

Here’s an example using the `request` fixture in Playwright:
```Typescript title="example.spec.ts"
import { test, expect } from '@playwright/test'; 
test('check API response', async ({ request }) => { 
	const response = await request.get('https://api.github.com');
	expect(response.status()).toBe(200); 
});
```

This code uses the `request` fixture to make a `GET` request to a public API endpoint. It then checks whether the response status is `200`, which means the request was successful.

For a web app with a backend API, you might use the `request` fixture to authenticate a user via an API call, then use the `page` fixture to verify that the UI reflects the logged-in state.

We’ll dive deeper into fixtures in Chapter 5, Crafting Scalable Tests with the Fixture System.

So, hooks help you handle setup and cleanup without repeating yourself, and fixtures let you share common test data or browser contexts in an organized way. Once you get the hang of them, you’ll find your tests much easier to manage.

