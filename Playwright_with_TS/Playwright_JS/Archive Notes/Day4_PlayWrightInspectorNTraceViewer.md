### How to run in debug mode in Playwright
`npx playwright test tests/example.spec.js --debug`
<br>
### How to record and create playback script
`npx playwright codegen <your_url>`
<br>
### How to take screenshot for all actions performed in Playwright.
- Once the below config script runs check `playwright-reports/` and `test-results`
```
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
	  browserName : 'chromium',
	  headless: false,
	  screenshot : 'on' //Enabling to take screenshot for every step
	  trace: 'on'	//Enabling trace/log for each step

  },

};

module.exports = config;
```
- Another cool trace property if you want to save traces only for failed testcases
```
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
	  browserName : 'chromium',
	  headless: false,
	  screenshot : 'on' 
	  trace: 'retain-on-failure'	//Enabling trace/log for only failed testcases

  },

};

module.exports = config;
```
