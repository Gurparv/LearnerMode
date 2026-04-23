# Install Playwright Library only

```Bash
npm install playwright
```

Documentation -> https://playwright.dev/docs/api/class-playwright

```javascript title="demo.js"
import {chromium} from 'playwright';
import assert from 'assert';

const browser = await chromium.launch({headless: false})
const context = await browser.newContext();
const page = await context.newPage();
await page.goto('https://www.saucedemo.com');
const title = await page.title();

assert.equals(title, 'Swag Labs');
console.log("passed");
```

Another example
Explanation to this below code in [[Javascript basics to know 2]]

```javascript title="demo2.js"
import {firefox} from 'playwright';
import assert from 'assert';

(async ()=>{
        const browser = await firefox.launch({headless: false});  // Or 'firefox' or 'webkit'.
        const page = await browser.newPage();
        await page.goto('http://example.com');
        // other actions...
        await browser.close();
})();
```

## Difference between CommonJS and ES Modules
In our case we used ES Modules.

|Feature|CommonJS|ES Modules|
|---|---|---|
|Import|`require()`|`import`|
|Export|`module.exports`|`export`|
|Loading|synchronous|asynchronous|
|Browser support|❌|✅|
|Modern standard|❌|✅|
