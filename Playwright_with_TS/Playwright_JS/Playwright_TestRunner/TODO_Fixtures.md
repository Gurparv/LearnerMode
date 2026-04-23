Useful to establish environment for each test, giving the test everything it needs and nothing else.

https://playwright.dev/docs/test-fixtures#without-fixtures
https://playwright.dev/docs/api/class-fixtures
## Playwright's Build-In Fixtures

Built in Fixtures are 
- browser
- browsername
- page
- context
- request

```Typescript title='test1.spec.ts'
import {test} from '@playwright/test'

test('How to use fixture',async({page})=>
     {
	console.log('Open page');
	await page.goto("https://playwright.dev/docs/api/class-fixtures");
     }
    );

```

## Customizing Playwright's Build-In Fixtures


## Custom Fixtures