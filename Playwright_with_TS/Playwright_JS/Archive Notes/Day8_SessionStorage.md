### When login into an web-app is more complex in terms of details it stores in browser eg cookies, storage, token etc.
- Solution in playwright.
	1. Login once with UI
	2. Then once login, store everything in which is present in browser like tokens, cookies, storage in a .json file using playwright.
	3. Then inject that .json file directly into a browser
```example.spec.js
const {test} = require(`@playwright/test`);
const {expect} =  require(`@playwright/test`);
const {request} =  require(`@playwright/test`);

let webContext;

test.beforeAll( async( {browser} )=>

	{
		const context = await browser.newContext();
		const page = await context.newPage();

		await page.goto("https://rahulshettyacademy.com/client");
		await page.locator("#userEmail").fill("anshika@gmail.com");
		await page.locator("#userPassword").type("Iamking@000");
		await page.locator("[value='Login']").click();
		await page.waitForLoadState('networkidle');

		await context.storageState({path: 'state.json'}) //It will create a .json file with all the Storage info present in the browser

		webContext = await browser.newContext({storageState:'state.json'}); //Injecting that .json file content into browser

	}

)

test.only ('First Playwright TestCase', async ({})=> 
	{
		const page = await webContext.newPage(); //dynamically created page , hence no need to pass as argument in anonymous function
		await page.goto("https://rahulshettyacademy.com/client");
	}

);
```
### Debugging NPM script for api testing inside VSCode 
- Watch video (small section, skipping for now)
### Debugging API calls code using Trace
- Watch video (small section, skipping for now)

