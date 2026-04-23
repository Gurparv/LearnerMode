### Select Dropdowns and Radio Buttons and Their Assertions
```example.spec.js
const {test} = require(`@playwright/test`);
const {expect} =  require(`@playwright/test`);


test.only ('First Playwright TestCase', async ({browser,page})=> 
	{
		await page.goto("https://rahulshettyacademy.com/loginpagePractise/");

		const dropdown = await page.locator("select.form-control");
		await dropdown.selectOption('teach'); //selecting dropdown value 'Teacher'
		await page.pause(); //pauses page for a while

		await page.locator(".checkmark").last().click(); //selects the radio btn option
		await page.pause(); //pauses page for a while

		await expect(page.locator(".checkmark").last()).toBeChecked(); //checks if radio button is checked or not
		await page.locator(".checkmark").last().uncheck(); //uncheck the selected radio btn

		await expect(page.locator(".checkmark").last()).toBeFalsy(); //expects it to be false to pass the assertion
		await page.locator(".checkmark").last().isChecked(); //returns boolean true or false
	}
);
```
<br>
<br>
### Using 'await' approriately
- It is used when action is performed and not needed when assigning value to dropdown.
```
Eg of correct usage
		const dropdown = await page.locator("select.form-control");
		await dropdown.selectOption('teach'); //selecting dropdown value 'Teacher'
		expect(await page.locator(".checkmark").last()).toBeFalsy(); //expects it to be false to pass the assertion
```
<br>
<br>
### Assertions based on attributes values
```example.spec.js
const {test} = require(`@playwright/test`);
const {expect} =  require(`@playwright/test`);


test.only ('First Playwright TestCase', async ({browser,page})=> 
	{
		await page.goto("https://rahulshettyacademy.com/loginpagePractise/");

		const documentLink = page.locator("[href*='documents-request']");
		await expect(documentLink.toHaveAttribute("class","blinkingText"); //here is the attribute assertion
	}
);
```
<br>
<br>
### Handling New Tabs
```example.spec.js

const {test} = require(`@playwright/test`);
const {expect} =  require(`@playwright/test`);


test.only ('First Playwright TestCase', async ({browser})=> 
	{
		const context = await browser.newContext();
		const page = await context.newPage();
		await page.goto("https://rahulshettyacademy.com/loginpagePractise/");

		const documentLink = page.locator("[href*='documents-request']");

		/*
		 * Here we are telling playwright that after click , a new page will open 
		 * so return the list of newPages to use.
		 */

		const [newPage] = await Promise.all(
			[
				context.waitForEvent('page'),
				documentLink.click(),
			]

		)
		const text = await newPage.locator(".red").textContent();
		console.log(text);
		page.locator("#username").type(text); //filling text found on 'newPage' to 'page'

	}
);
```
