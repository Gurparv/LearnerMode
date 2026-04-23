
| [[#Simple Web Browser opening and assertion]] | [[#Multi Tab]]        | Multi Windows         | API Testing               |
| --------------------------------------------- | --------------------- | --------------------- | ------------------------- |
| [[#Data Driven Testing]]                      | [[#Device Emulation]] | Diff browser test     | Visual Test               |
| [[#Authentication]]                           | Multi User test       | Accessibility Test    | Serial / Parallel testing |
| Locators                                      | Mock APIs             | Mock Browser APIs     | Events                    |
|                                               | Network               | Evaluating Javascript | Handles                   |

---

## Simple Web Browser opening and assertion

```typescript title="demo1.spec.ts"
import {test,expect} from '@playwright/test';

test('RahulShettyTest1',async({page})=>{
	console.log("hello");
	await page.goto("https://rahulshettyacademy.com/AutomationPractice/");
	await console.log(page.url());
	await expect(page).toHaveURL('https://rahulshettyacademy.com/AutomationPractice/');
	await page.pause();
	//Dispose the page.
	await page.close();
});
```

To run it.
```Bash
npx playwright test demo1.spec.ts --headed
```

---

## Multi Tab

```typescript title="demo2.spec.ts"
import {test,expect} from 'playwright/test';

test('multi-tab testing',async({context,browserName})=>{
	await console.log("Test starting");
	await console.log(browserName);
	//Page 1.
	const page1 = await context.newPage();
	await page1.goto("https://rahulshettyacademy.com/AutomationPractice/");
	const page2 = await context.newPage();
	await page2.goto("https://www.saucedemo.com/");
	await page1.pause();
	expect(page2).toHaveTitle("Swag Labs");
	await page1.pause();
	await context.close();

});

```

To run it.
```Bash
npx playwright test demo2.spec.ts --headed
```

---

## Device Emulation

https://playwright.dev/docs/emulation

```typescript title="demo3.spec.ts"
import {test,expect} from '@playwright/test';
import {chromium,devices} from 'playwright';

test('iphone testing',async()=>{

	const browser = await chromium.launch();
	const iphone14 = devices['iPhone 14'];
	const lang = 'es-ES';
	const context = await browser.newContext({...iphone14,locale: lang});
	const page = await context.newPage();
	await page.goto("https://www.bing.com");
	await page.pause();
	await context.close();
});
```

```Bash
npx playwright test demo3.spec.ts --headed
```

---

## Data Driven Testing

https://playwright.dev/docs/test-parameterize

```typescript title="demo4.spec.ts"
import {test,expect} from '@playwright/test';

test.describe.configure({mode:'parallel'});

[
	{username:`standard_user` , password:`secret_sauce` },
	{username:`problem_user` , password:`secret_sauce` },
	{username:`visual_user` , password:`secret_sauce` },
].forEach( ({username, password})=>{
test(`parametrize testing with ${username}`,async({page})=>{
	await console.log(`${username} and ${password}`);

	await page.goto("https://www.saucedemo.com/");
	await page.locator('[data-test="username"]').click();
	//await page.pause();
  	await page.locator('[data-test="username"]').fill(username);
  	await page.locator('[data-test="password"]').click();
  	await page.locator('[data-test="password"]').fill(password);
  	await page.locator('[data-test="login-button"]').click();
	
	await expect(page).toHaveURL("https://www.saucedemo.com/inventory.html",{timeout:10_000});

	//await page.pause();
	page.close();
});
});
```

---

## Authentication

Getting Authentication details
```typescript title=demo5.spec.ts"
import {test,expect} from '@playwright/test';

test('getting auth details',async({page})=>{
	await page.goto('https://www.saucedemo.com/');
  	await page.locator('[data-test="username"]').click();
  	await page.locator('[data-test="username"]').fill('standard_user');
  	await page.locator('[data-test="password"]').click();
  	await page.locator('[data-test="password"]').fill('secret_sauce');
  	await page.locator('[data-test="login-button"]').click();

	await expect(page).toHaveTitle("Swag Labs",{timeout:5_000});

	//To get auth user details
	console.log("saving user logged in state...");
	await page.context().storageState({path: "./user-auth.json"});
});
```
To run
```Bash
npx playwright test demo5.spec.ts --headed
```

Use the saved auth details
```typescript title="demo6.spec.ts"
import {test,expect} from '@playwright/test';

test.use({storageState: './user-auth.json'});

test('Using saved logged in state',async({page})=>{
	console.log(await page.context().storageState());
	await page.goto("https://www.saucedemo.com/inventory.html");
	await expect(page).toHaveURL("https://www.saucedemo.com/inventory.html",{timeout:10_000});
});

```

To run
```Bash
npx playwright test demo6.spec.ts --headed
```

---

