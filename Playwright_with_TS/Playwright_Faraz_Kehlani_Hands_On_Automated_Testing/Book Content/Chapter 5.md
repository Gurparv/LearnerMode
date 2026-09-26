# Crafting Scalable Tests with the Fixture System

Testing modern web applications can get complex if every test has to manage its own setup and cleanup.

This is where Playwright’s fixtures come in. Inspired by Python’s pytest framework, fixtures act as ==reusable building blocks== that handle essential resources.

In this chapter, you’ll discover how to use Playwright’s fixture system to its full potential. We’ll start with the built-in fixtures, then move on to creating your own and understanding how fixture scope and life cycle affect your tests. We’ll also cover more advanced topics such as nesting fixtures, integrating them with the page object model, and designing a scalable architecture that keeps your test suite easy to manage.

As such, we will cover the following topics in the chapter:
1. [[#Examining built-in fixtures]]
2. [[#Creating custom fixtures]]
3. [[#Understanding fixture scope and life cycle]]
4. Practical fixture examples

## Examining built-in fixtures
Built-in fixtures are handy tools that come ready-to-use with the Playwright Test framework. They are prepackaged helpers that take care of common tasks such as setting up and tearing down browsers, pages, and contexts.

You don’t have to do anything special to use fixtures. They’re available by default. Just declare them as parameters in your test functions, and Playwright will handle the rest.

The core mechanism is **dependency injection.** When you define a test, you list the fixtures you need as parameters in the `test` function. The Playwright test runner sees these parameters, initializes the corresponding objects behind the scenes before your test runs, and then passes them to your test. After the test finishes, it automatically cleans them up.

For example, let’s say you write a test like this:

```Typescript title="example.test.ts"
import { test, expect } from '@playwright/test';

test('my first test', async ({ page }) => {
  await page.goto('https://playwright.dev/');
  await expect(page).toHaveTitle(/Playwright/);
});
```

Here, you never wrote any code to launch a browser or create a new page. The `{ page }` argument tells the test runner, “Hey, I need a fresh browser page for this test.” The runner then performs these steps for you:
1. Sets up: Launches a browser, creates a new browser context, and creates a new page
2. Injects: Passes the page object into your test function
3. Executes: Runs your test code
4. Tears down: Closes the page, the context, and the browser automatically

The following is an overview of the main built-in fixtures, what they do, and how you can use them in your tests. Once you’re familiar with these Playwright fixtures, we’ll look at how you can create your own to handle reusable setup and teardown logic that’s tailored to your testing needs.

### The browser fixture
The `browser` fixture provides a new browser instance (Chromium, Firefox, or WebKit) for the test. The browser instance is launched when the test starts and closed when the test ends. You can use it when you need to control the browser directly, such as launching a new context or managing browser-level settings.

```Typescript title="example.test.ts"
import { test, expect } from '@playwright/test';

test('manage browser-level settings', async ({ browser }) => {
  // Create a new context with custom settings
  const context = await browser.newContext({
    userAgent: 'My Custom User Agent',
    locale: 'fr-FR',
    // other options like timezoneId, colorScheme, etc.
  });

  // Create a page inside this context
  const page = await context.newPage();
  await page.goto('url');

  // Your test actions and assertions here

  await context.close();
});
```

Another `browser` fixture is `browserName`, which is just a string indicating the name of the browser being used (`"chromium", "firefox", or "webkit"`). This is useful for conditional logic based on the browser type.

Here is an example:
```Typescript title="example.test.ts"
import { test } from '@playwright/test';

test('check browser', async ({ browserName }) => {
  if (browserName === "chromium") {
    console.log(`Running on ${browserName}`);
  }
});
```

### The page fixture
The `page` fixture provides a single, isolated browser page (tab) for a test, which is automatically created within a new browser context. It’s ideal for testing individual web pages or user flows, as it comes preconfigured with a context and is closed after the test. This is the most commonly used fixture because most tests interact with a single page.

Here is an example:
```Typescript title="example.test.ts"
import { test, expect } from '@playwright/test';

test('visit page', async ({ page }) => {
  await page.goto('https://www.google.com/');
  await expect(page).toHaveTitle(/Google/);
});
```

In contrast, the `browser` fixture we discussed previously provides a full browser instance (Chromium, Firefox, or WebKit), which gives you control over the entire browser, including the ability to create multiple contexts, manage browser-level settings, or launch multiple pages. But it requires manual context and page creation. Essentially, the `page` fixture is a higherlevel abstraction for simpler, single-page tests, while the browser fixture offers lower-level control for more complex scenarios. The `page` fixture is also automatically configured using the settings defined in your `playwright.config.ts` file, such as default browser type and viewport size (as we discussed in Chapter 1, Quick Setup Refresher), which makes it convenient for most tests.

### The context fixture
The `context` fixture provides a `BrowserContext` object. A context is like an incognito browser profile, with its own cookies and local storage. All pages created within the same context will share these. This is useful for tests where you need to manage login states across multiple tabs.

Here is the example
```Typescript title="example.test.ts"
import { test, expect } from '@playwright/test';

test('should share cookies between pages in the same context', async ({ context }) => {
  // Create two pages within the same context
  const page1 = await context.newPage();
  const page2 = await context.newPage();

  // Set a cookie on page1
  await page1.goto('https://playwright.dev/');
  await page1.context().addCookies([{
    name: 'test_cookie',
    value: 'test_value',
    domain: '.example.com',
    path: '/',
  }]);

  // Navigate to the same domain on page2
  await page2.goto('https://playwright.dev/');

  // Verify that page2 has access to the same cookie
  const cookies = await page2.context().cookies();
  const testCookie = cookies.find(cookie => cookie.name === 'test_cookie');
  expect(testCookie).toBeDefined();
  expect(testCookie.value).toBe('test_value');

  // Clean up
  await page1.close();
  await page2.close();
});
```

### The request Fixture
The `request` fixture gives you an `APIRequestContext` instance for making HTTP requests (such as `GET` or `POST`) to APIs or other endpoints. This fixture is useful for testing APIs or setting up test data via HTTP requests.

Here is an example.
```Typescript title="example.test.ts"
import { test, expect } from '@playwright/test';

test('API request', async ({ request }) => {
  const response = await request.get('https://jsonplaceholder.typicode.com/todos/1');
  expect(response.ok()).toBeTruthy();
```

Built-in fixtures come out of the box, but you can also create custom ones to tailor things perfectly for your application.

## Creating custom fixtures

Q. When to use fixture and when to use setup and teardown methods like beforeEach, afterEach etc?
Q Ask AI to give you simple challenges for you to create custom fixtures.

Without a centralized approach, you might end up writing the same setup steps (such as launching a browser, going to a URL, or logging in) and teardown steps (such as closing the browser) in multiple places, sometimes in every test file or even every single test.

This leads to duplicated code that’s harder to maintain and can create inconsistencies, which, in turn, can cause flaky tests. On top of that, making changes to the setup or teardown later means you’ll need to update it in many different spots. ==That’s where project-level fixtures really shine. They let you share things such as a browser instance across all tests in a given project.==

To set up your own custom fixtures in Playwright, you’ll start by extending the base test object. First, import the base test from `@playwright/test`. Then, use the `test.extend()` method to add your fixtures. Each fixture is just an `async` function that takes in any dependencies along with a `use` callback. This gives you a nice flow: do any setup work first, hand control back to the test with use, and then wrap things up with teardown once the test is finished.

For example, say you have many tests that require a logged-in user. You can define a custom fixture like this:
```Typescript title="myfixture.ts"
// fixtures/auth.ts
import { test as base } from '@playwright/test';

export const test = base.extend<{ loggedInPage: Page }>({
  loggedInPage: async ({ page }, use) => {
    // --- Setup: Log the user in ---
    await page.goto('https://www.saucedemo.com/');
    await page.getByPlaceholder('Username').fill('standard_user');
    await page.getByPlaceholder('Password').fill('secret_sauce');
    await page.getByRole('button', { name: 'Login' }).click();
    await page.waitForURL('https://www.saucedemo.com/inventory.html');
    
    console.log('User logged in!');

    // Provide the logged-in page to the test
    await use(page);

    // --- Teardown ---
    // Example: Log out if needed
    // await page.click('#logout-button');
    console.log('Test finished, loggedInPage fixture torn down.');
  },
});
```

Notice how we pass the fixture’s value to the `use` callback using `await use(value)`, which hands over the resource to the test for execution. At the end of the script, you can implement the teardown logic after the `use` call to clean up resources. This ensures test isolation and prevents side effects such as lingering data or open connections.

Now, you can use the fixture in your code:
```Typescript title="example.test.ts"
import { test } from '../fixtures/auth';
import { expect } from '@playwright/test';

test('should display shopping cart after login', async ({ loggedInPage }) => {
  const cartLink = loggedInPage.locator('.shopping_cart_link');
  await expect(cartLink).toBeVisible();
});
```
Using fixtures this way comes with lots of benefits:
- The login logic is defined once, so each test can focus on what it’s actually testing
- You can use the same fixture across many tests without repeating code
- Each test gets its own fresh `loggedInPage` fixture (default is test scope), which helps prevent one test from accidentally affecting another
- Setup and teardown behave the same way everywhere, which helps keep your tests reliable (we’ll go over this in the Fixture life cycle section)

If you need to reuse the same logged-in page across tests within a worker, consider defining your fixture with the `scope: 'worker'` option. This ensures the page is created once per worker and shared across its tests. For more details, see the Playwright docs on worker-scoped fixtures
https://playwright.dev/docs/test-fixtures#worker-scoped-fixtures

So far, we’ve looked at what fixtures are, how to use the built-in ones, and how to create your own for custom setups. But knowing what a fixture does is only half the story. To really use them effectively, you also need to understand how long they live, when they’re created, and when they’re torn down.

## Understanding fixture scope and life cycle

Fixture scope and life cycle concepts define the boundaries of a fixture’s existence: whether it’s spun up fresh for every test, or reused across multiple tests in the same worker. Getting this right can mean the difference between a slow, flaky suite and one that runs smoothly at scale.



