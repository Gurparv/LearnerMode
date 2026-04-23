### Navigate Back and Forward in WebBrowser pages.
```example.spec.js
const {test} = require(`@playwright/test`);
const {expect} =  require(`@playwright/test`);


test.only ('First Playwright TestCase', async ({browser,page})=> 
	{
		await page.goto("https://rahulshettyacademy.com/loginpagePractise/");
		await page.goto("https://google.com");

		await page.goBack();
		await page.goForward();
	}
);
```
<br>
<br>
### How to handle Java/Javascript pop ups (or in Playwright terminalogy its called Dialog) 
```example.spec.js
const {test} = require(`@playwright/test`);
const {expect} =  require(`@playwright/test`);


test.only ('First Playwright TestCase', async ({browser,page})=> 
	{
		await page.goto("https://rahulshettyacademy.com/AutomationPractice");

		page.on('dialog',dialog => dialog.accept());
		await page.locator("#confirmbtn").click();
	}
);
```
### How to hover on webelments 
```example.spec.js 
const {test} = require(`@playwright/test`);
const {expect} =  require(`@playwright/test`);

test.only ('First Playwright TestCase', async ({browser,page})=> 
	{
		await page.goto("https://rahulshettyacademy.com/AutomationPractice");

		await page.locator("#mousehover").hover();
	}
);
```
### 'Useful tip' -> Debug mode and pause btn
- If you run playwright in debug mode then it will start debug from Line 1 but ,
- if you put `await page.pause()` in your script and run in normal mode then the script will pause that particular line , hence saving your time
<br>
<br>
### How to handle iFrames in playwright
```example.spec.js
const {test} = require(`@playwright/test`);
const {expect} =  require(`@playwright/test`);


test.only ('First Playwright TestCase', async ({browser,page})=> 
	{
		await page.goto("https://rahulshettyacademy.com/AutomationPractice/");
		
		const framesPage = await page.frameLocator("#courses-iframe"); //handling iframes 
		await console.log("--> frame found");
		//await framesPage.locator("li a[href*='lifetime-access']:visible").click(); //here css trick to click the webelement which is in visible mode only
	}
);
```
