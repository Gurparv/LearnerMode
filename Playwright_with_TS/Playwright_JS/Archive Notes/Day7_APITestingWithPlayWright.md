### Scenario - Why we should login each time when we can just have login token through API and use it in new browser to login easily.
- In the below example we will use the 'request' method to hit API and grab response.
```example.spec.js
const {test} = require(`@playwright/test`);
const {expect} =  require(`@playwright/test`);
const {request} =  require(`@playwright/test`);


test.beforeAll( async()=> {
		
		const apiContext = await request.newContext(); //Just like for browser we used to open its context similarly for API testing we will use 'request'
		const loginPayLoad = {userEmail : "anshika@gmail.com", userPassword : "Iamking@000"} ;
		const loginResponse = await apiContext.post("https://rahulshettyacademy.com/api/ecom/auth/login",
			{data: loginPayLoad}
			);
		expect(loginResponse.ok()).toBeTruthy();
		const loginResponseJson = await loginResponse.json();
		const token = loginResponseJson.token;
		console.log("-->"+token);
	}
);

test.beforeEach( ()=> {
		
	}
);

test.only ('First Playwright TestCase', async ({browser,page})=> 
	{
		//testcase goes here
	}
);
```
### Once we have response - Now passing token to browser
```example.spec.js
const {test} = require(`@playwright/test`);
const {expect} =  require(`@playwright/test`);
const {request} =  require(`@playwright/test`);

let token;

test.beforeAll( async()=> {
		
		const apiContext = await request.newContext(); //Just like for browser we used to open its context similarly for API testing we will use 'request'
		const loginPayLoad = {userEmail : "anshika@gmail.com", userPassword : "Iamking@000"} ;
		const loginResponse = await apiContext.post("https://rahulshettyacademy.com/api/ecom/auth/login",
			{data: loginPayLoad}
			);
		expect(loginResponse.ok()).toBeTruthy();
		const loginResponseJson = await loginResponse.json();
		token = loginResponseJson.token;
		console.log("-->"+token);
	}
);

test.beforeEach( ()=> {
		
	}
);

test.only ('First Playwright TestCase', async ({browser,page})=> 
	{
		page.addInitScript(value => {
			window.localStorage.setItem('token',value);	
		},token);

		await page.goto("https://rahulshettyacademy.com/client/");
		await page.pause();
	}

);
```
### Now automate placing an order with API calls
```example.spec.js
const {test} = require(`@playwright/test`);
const {expect} =  require(`@playwright/test`);
const {request} =  require(`@playwright/test`);

let token;
let orderId;

test.beforeAll( async()=> {
		
		//Login api call
		const apiContext = await request.newContext(); //Just like for browser we used to open its context similarly for API testing we will use 'request'
		const loginPayLoad = {userEmail : "anshika@gmail.com", userPassword : "Iamking@000"} ;
		const loginResponse = await apiContext.post("https://rahulshettyacademy.com/api/ecom/auth/login",
			{data: loginPayLoad}
			);
		expect(loginResponse.ok()).toBeTruthy();
		const loginResponseJson = await loginResponse.json();
		token = loginResponseJson.token;
		console.log("-->"+token);

	console.log("/////////////////////");
		//Create order api call
		const orderPayLoad = {orders:[{country:"India",productOrderId:"62023a7616fcf72fe9dfc619"}]};
		const orderResponse = await apiContext.post("https://rahulshettyacademy.com/api/ecom/order/create-order",
			{
				data: orderPayLoad,
				headers: {
					'Authorization' : token,
					'Content-Type' : 'application/json'
				},
			});
	const orderResonseJson = await orderResponse.json();
	console.log("OrderResponse --> " +orderResonseJson);
	orderId = await orderResonseJson.orders[0];
	console.log("OrderId => "+orderId);
});

test.beforeEach( ()=> {
		
	}
);

test.only ('First Playwright TestCase', async ({browser,page})=> 
	{
		page.addInitScript(value => {
			window.localStorage.setItem('token',value);	
		},token);

		await page.goto("https://rahulshettyacademy.com/client/");
		await page.pause();
	}

);
```
### Manage the folders so that code looks cleaner and maintainable
- Create a folder 'utils' in 'tests/'
	- Inside it create another folder 'ApiUtils'
```ApiUtils.js
class APiUtils{

	constructor(apiContext){
		this.apiContext = apiContext;
		}

	async getToken(){
			//code goes here.
			const loginResponse = await this.apiContext.post("https://rahulshettyacademy.com/api/ecom/auth/login",
				{data: loginPayLoad}
				);
			expect(loginResponse.ok()).toBeTruthy();
			const loginResponseJson = await loginResponse.json();
			token = loginResponseJson.token;
			console.log("-->"+token);
			return token;
			}

	async createOrder(orderPayLoad){
		//code goes here.
		}
	}
module.exports{ApiUtils}; //makes this class globally accessible to all the other classes in 'test/'
```
