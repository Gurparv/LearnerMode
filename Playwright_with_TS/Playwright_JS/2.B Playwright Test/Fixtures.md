- [[#Introduction]]
- [[#Built-in fixtures]]


## Introduction
Playwright Test is based on the concept of test fixtures. Test fixtures are used to establish the environment for each test, giving the test everything it needs and nothing else. Test fixtures are isolated between tests. With fixtures, you can group tests based on their meaning, instead of their common setup.

## Built-in fixtures
Here is a list of the pre-defined fixtures that you are likely to use most of the time.

|Fixture|Type|Description|
|---|---|---|
|page|[Page](https://playwright.dev/docs/api/class-page "Page")|Isolated page for this test run.|
|context|[BrowserContext](https://playwright.dev/docs/api/class-browsercontext "BrowserContext")|Isolated context for this test run. The `page` fixture belongs to this context as well. Learn how to [configure context](https://playwright.dev/docs/test-configuration).|
|browser|[Browser](https://playwright.dev/docs/api/class-browser "Browser")|Browsers are shared across tests to optimize resources. Learn how to [configure browsers](https://playwright.dev/docs/test-configuration).|
|browserName|[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")|The name of the browser currently running the test. Either `chromium`, `firefox` or `webkit`.|
|request|[APIRequestContext](https://playwright.dev/docs/api/class-apirequestcontext "APIRequestContext")|Isolated [APIRequestContext](https://playwright.dev/docs/api/class-apirequestcontext) instance for this test run.|

```Javascript title="demo.spec.ts"
import { test, expect } from '@playwright/test';

test('basic test', async ({ page }) => {
  await page.goto('https://playwright.dev/');

  await expect(page).toHaveTitle(/Playwright/);
});
```

---

