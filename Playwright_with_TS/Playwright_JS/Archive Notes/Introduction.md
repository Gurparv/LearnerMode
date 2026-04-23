## How to install Playwright?
 This below command when run on terminal will download all the playwright dependencies and also will create the folder structure
`npm init playwright`

These will be files and directories which will be automatically created on running the above command
`
	node_modules/
	tests/
	tests-examples/
	package-lock.json
	package.json
	playwright.config.js
`

*playwright.config.js* is the main test runner file and *tests/* directory contains all the tests with naming convention as `example.spec.js`

##### Sample Test case script in playwright.
```
const {test} = require(`@playwright/test`);

test ('First Playwright TestCase', async ({browser})=>
	{
		const my_browser = await browser.newContext();
		const page= await my_browser.newPage();
		await page.goto("https://www.google.com");
	}
);

test ('Second Playwright TestCase', async ({browser,page})=>
	{
		await page.goto("https://www.google.com");
	}
);
```

##### Sample playwright.config.js
```
// @ts-check
const { devices } = require('@playwright/test');

const config = {
  testDir: './tests',
  /* Maximum time one test can run for. */
  timeout: 30 * 1000,
  expect: {
    /**
     * Maximum time expect() should wait for the condition to be met.
     * For example in `await expect(locator).toHaveText();`
     */
    timeout: 5000
  },
  reporter: 'html',
  /* Shared settings for all the projects below. See https://playwright.dev/docs/api/class-testoptions. */
  use: {
	  browserName : 'chromium'
  },

};

module.exports = config;

```

#### To run the playwright test
`npx playwright test`
or 
`npx playwright test --headed`

<br>

----
----
----
### Test script with assertion example
```example.spec.js
const {test} = require(`@playwright/test`);
const {expect} =  require(`@playwright/test`);

test ('First Playwright TestCase', async ({browser})=>
	{
		const my_browser = await browser.newContext();
		const page= await my_browser.newPage();
		await page.goto("https://www.google.com");
	}
);

test ('Second Playwright TestCase', async ({browser,page})=>
	{
		await page.goto("https://www.google.com");
		await expect(page).toHaveTitle('Google'); //assertion here
	}
);
```
<br>
### How to run in different browser 
```playwright.config.js

// @ts-check
const { devices } = require('@playwright/test');

const config = {
  testDir: './tests',
  timeout: 30 * 1000,
  expect: {
    timeout: 5000
  },
  reporter: 'html',
  use: {
	  browserName : 'chromium' //change browserName here to 'firefox', 'webkit' or 'chromium'
  },

};

module.exports = config;

```
<br>
<br>
### How to control running 'Headless' or 'Headed' Mode
```playwright.config.js

// @ts-check
const { devices } = require('@playwright/test');

const config = {
  testDir: './tests',
  timeout: 30 * 1000,
  expect: {
    timeout: 5000
  },
  reporter: 'html',
  use: {
	  headless : true //Now runs in headless mode
	  browserName : 'chromium' //change browserName here to 'firefox', 'webkit' or 'chromium'
  },

};

module.exports = config;

```
