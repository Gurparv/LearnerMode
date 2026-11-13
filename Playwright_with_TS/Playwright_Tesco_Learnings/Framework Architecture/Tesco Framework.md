```Folder structure
src/
cypress/
azure-pipelines/
public/
playwright/
	- e2e/
		  - colleagueForecastMatches.test.ts
	- support/
		- fixtures/
				- UserProfiles/
					  - colleagueUserProfle.ts
				- filterOptions.ts
				- actions.ts
				- comments.ts
		- pages/
			- BasePage.ts
			- PromotionsHomePage.ts
		- apiRoutes.ts
		- fixtures.ts
	- playwright.config.ts
	- tsconfig.json
package.json
package-lock.json
.gitignore
.env
Dockerfile
README.md
tsconfig.json
```

```Typescript title=playwright.config.ts
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
	testDir: './e2e',
	outputDir : './test-results',
	fullyParallel: true,
	forbidOnly: !! process.env.CI,
	retries: process.env.CI ? 2 : 0,
	workers: process.env.CI ? '50%' : undefined,
	reporter : [
	// allure
	// html
	['html', {outputFolder: './report', open: 'never'}],
	// Github actions inline annotations - only active on CI
	],
	use: {
		baseURL : 'http://localhost:3000',
		...devices['Desktop Chrome'],
		viewport : {width: 1920, height:1000},
		locale: 'en-GB',
		trace: 'on-first-retry',
		screenshot: 'only-on-failure',
		video: 'retain-on-failure'm
	},
	projects: [
		{
			name: 'chromium',
			use: {...devices['Desktop Chrome'] },
		},
	],
	
	webServer: {
		command: 'npm run start',
		url: 'http://localthost:3000',
		reuseExistingServer: !process.env.CI,
		stdout: 'ignore',
		stderr: 'pipe',
	},
});
```

```Typescript title=fixtures.ts
import {test as base, type Page} from '@playwright/test';
import {API_ROUTES} from './apiRoutes';
import { colleagueUserProfile} from './fixtures/UserProfiles/colleagueUserProfile';

export interfact MockApi {
	intercept:  (pattern: string, data: unknown, method?: string, status?: number) => Promise<void>;
	error : (pattern: string, status: number) => Promise<void>;
	abort : (pattern: string) => Promise<void>;
}

export interface AppFixtures {
	mockApi : MockApi;
	authenticatedPage: Page;
}

export const test = base.extend<AppFixtures>({
	mockApi: async({page}, use) => {
		const api: MockApi = {
			intercept: async (pattern, data, method?: string, status=200) => {
				await page.route(pattern, (route) => {
					if (method && route.request().method() !== method.toUpperCase()){
						return route.fallback(); //not my method -> let another handler take it
					}
					return route.fulfill({status, json: data as Record <string, unknown>});
					});
				},
			error: async(pattern, status) => {
				await page.route(pattern, (route) => 
					route.fulfill({status, contentType: 'application/json', body: '{}'}),
					);
			},
			abort: async (pattern) => {
				await page.route(pattern, (route)) =>route.abort();
			},
		};
	await use(api);
	},
	
	authenticatedPage: async ({page}, use) => {
		const token = 'CYPRESS_TEST_TOKEN'
		await page.context().addCookies([
			{
				name: 'SCA.AccessToken',
				value: token,
				domain: 'localhost',
				path: '/',
			},
		]);
		await page.route(API_ROUTES.userProfile, (route) -> 
			route.fulfill( {json: colleagueUserProfile}),
		);
		await use (page);
	},
});

export {expect} from '@playwright/test';


```

```Typescript title=apiRoutes.ts
export const APP_BASE = '/connect/promo';
const PROMOTION_SERVICE = '**/connect/promotions-service';

export const API_ROUTES = {
	userProfile: `${PROMOTION_SERVICE}/v2/user-profiles/user-profile**`,
	comments: `${PROMOTION_SERVICE}/v1/promotions/comments/89119/10/111111/1212/UK`,
	promotionForecast : `${PROMOTION_SERVICE}/v1/promotions/forecast/product/899102/period/10/country/GBR**`
} as const;
```

```Typescript title='BasePage.ts'
import {type Page} from '@playwright/test';
import { API_ROUTES, APP_BASE} from '../apiRoutes';
import {type MockApi} from '../fixtures';
import {actions} from '../fixtures/actions';
import {comments} from '../fixtures/comments';

export abstract class BasePage {
	constructor (protected readonly page: Page) {}
	
	async goto(path='', params?: Readonly<Record<string, string>>)	{
		const qs = params ? `?${new URLSearchParams(params).toString()}` : '';
		await this.page.goto(`${APP_BASE}${path}${qs}`);
	}
	
	async setupRoutes(mockApi: MockApi, overrides?: {UserProfile ?: unknown}) {
		if (overrides?.userProfile)	{
			await this.page.unroute(API_ROUTES.userProfile);
			await mockApi.intercept(API_ROUTES.userProfile, overrides.userProfile);
		}
		mockApi.intercept( API_ROUTES.comments, comments);
		mockApi.intercept ( API_ROUTES.displayActions, actions);
	}
	
}

```

```typescript title='PromotionsHomePage.ts
import { BasePage} from './BasePage';
import {Page} from '@playwright/test';

export class PromotionsHomePage extends BasePage{
	readonly reviewPromotionBtn;
	readonly commentInputBox;
	
	constructor(page: Page){
		super(page);
		this.reviewPromotionBtn = this.page.getByRile('button', {name: 'Review Promotion'}):
		this.commentInputBox = this.page.locator('#commentInputBox');
	}
	
	getPage(){
		return this.page;
	}
	
	async clickReviewPromotionBtn(){
		await this.reviewPromotionBtn.click();
	}
}
```

```Typescript title="colleagueForecastMatches.test.ts
import {expect, test, type AppFixtures } from '../support/fixtures';

test.describe('Colleague Forecast Matches tests', () =>{
	let promotionsHomePage : PromotionsHomePage;
	
	test.beforeEach(async({authenticatedPage, mockApi}: AppFixtures))=>{
		promotionsHomePage = new PromotionsHomePage(authenticatedPage);
		await promotionsHomePage.setupRoutes(mockApi);
		await mockApi.intercept(API_ROUTES.promotionsForecast, forecastMatches);
		await promotionsHomePage.goto();
	});
	
	test('The Forecast matches is disabled when the Week 1 Sales < 1', async()=>{
		await promotionHomePage.clickReviewPromotionBtn();
		// code
	});
		
	test('When the forecast matches option is clicked, I should see the forecast panel', async({mockApi}: AppFixtures)=>{
		mockApi.intercept( API_ROUTES.comments, someOtherComments);
		await promotionsHomePage.clickReviewPromotionBtn();
		// code
	});
});
```

```Typescript title="comments.ts"
export const comments = 
[] as const;
```

```Typescript title="colleagueUserProfle.ts"
export const colleagueUserProfile = {
"userId" : "Tom Hardy",
"name" : "Bond",
"assumedRole" : null,
"userAuthorisationRules": [
	{"resourceId": "DEMAND",
		"Action": "UPDATE"
	},
	{"resourceId": "IAM",
		"Action": "READ"
	},
]
} as const;
```

```Typescript title="tsconfig.json"
{
	"extends": "../tsconfig.json",
	"compilerOptions" : {
		"target": "ES2022",
		"lib": ["ES2022", "DOM"],
		"types": ["node", "@playwright/test", "cypress"],
		"jsx": "react-jsx",
		"allowImportingTsExtensions": true,
		"isolatedModules": false,
		"noEmit": true,
		"noUnusedLocals": false,
		"noUnusedParameters": false
	},
	"include": ["**/*.ts", "../src/**/*.ts", "../src/**/*.tsx", "../global.d.ts"],
	"exclude": ["node_modules"]
}
```

```Typescript title=package.json
.
.
.
"scripts": {
"playwright": "playwright test --config playwright/playwright.config.ts",
"playwright:headed": "playwright test --config playwright/playwright.config.ts --headed",
"playwright:flaky": "playwright test --config playwright/playwright.config.ts --repeat-each=5",
"playwright:ui": "playwright test --config playwright/playwright.config.ts --ui",
"playwright:list-devices": "playwright test --list-devices",
"playwright:open-devtools": "playwright test --open-devtools",
"playwright:debug": "playwright test --config playwright/playwright.config.ts --debug",
"playwright:ci": "CI=true playwright test --config playwright/playwright.config.ts"
}
.
.
```

## Question on Framework
Q. How does `authenticatedPage` and `mockApi` affect the same browser page?
`mockApi` does not know about authenticatedPage. They are siblings. Both ask for the fixture named page. The auth fixture modifies it and yields that same reference. The page object stores it. The mock helper closes over it. Therefore cookie , profile route, app routes, locators and navigation all act through the same page.

