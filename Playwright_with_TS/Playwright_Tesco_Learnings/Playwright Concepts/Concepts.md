```Typescript title="example.test.ts"

page.unroute(url) // remove an earlier route handler previously registered for the matching URL. 

page.waitForResponse() // It resolves when the browser receives a response that matches the URL or predicate. It is a passive observation. it neither intecepts nor changes the request or response. 
// Use it when: the UI should make a request and you want to assert what actually came back or what URL is used.

```

```Typescript title="mytest.test.ts"
const fileterUsed = page.waitForResponse( (res) =>
	res.url().includes('/reviewCategory=AWAITING_FEEDBACK') && 
	! res.url().includes('/download')
);

await promotionsHomePage.clickApplyFilterBtn();
const filterResponse = await filterUsed;

expect (filterResponse.status()).toBe(200);  // asserting Did the request receive a successful response?

const filterUrl = new URL (filterResponse.url());
// Asserting Did the frontend construct the correct request?
expect(filterUrl.searchParams.get('page')).toBe('0');
expect(filterUrl.searchParams.get('size')).toBe('25');
expect(filterUrl.searchParams.get('reviewCategory')).toBe('AWAITING_FEEDBACK');

// others 
filterResponse.header(); // response headers as an object
filterResponse.request(); // The 'Request' that produced this response.

```

🔴 Difference between `ToBeAttached(), ToBeVisible(), ToBeInViewport(), toHaveCount()`
```Typescript title="example.test.ts"

toBeAttached() // To check - If The element exists in the DOM tree ?
toBeVisible() // To check - If the element is attached and visibly rendered
toBeInViewport() //To check - The element is visible and intersects the current browser viewport 
toHaveCount() // To check - The elment SHOULD NOT be present in DOM. // used to assert absence.
```

🔴 Difference between `waitForResponse(), page.route(), page.request() and route.request()`
```Typescript title="example.test.ts"
page.route() // control/intercept the app's traffic (write)
// When to use - When u need to mock the app's requests or you need to modify or alter its request.

page.waitForResponse() // observe traffic the app made (read)
// When to use - You want to assert a response created by the UI action without modifying it.

page.request // make your own API calls from the test
// When to use - You need to seed,reset or directly query an API outside the page UI. This call comes from the test , not from a button click in the browser page.

route.request() // inspect the request currently being intercepted.
// When to use - Your route handler needs the methond, URL, headers or body to chosse how to respond.
```

---
---

```Typescript title=example.test.ts
const headers = currentForecastTable.locator('table>thead>tr>th);
const expectedCells:[string, string][] = [
	['Base Sales', '100,000'],
	['Base Week', '170,000'],
];

for (const [headerText, expectedValue] of expectedCells) {
	const headerIndex =  await headers.evaluateAll(
		(headerElements, expectedHeader) =>
			headerElements.findIndex( (header) => (header.textContent || '').includes(expectedHeader)),
			headerText
	);
	 expect(headerIndex, `${headerText} column index`).toBeGreaterThan(-1);
	 await expect(currentForecastTable.locator('table>tbody>tr').nth(0).locator('td').nth(headerIndex)).toContainText(expectedValue);
}
```

Different ways to iterate in Typescript/Javascript
1. for loop
2. for... of loop
3. for...in loop
4. forEach loop
5. while/do while loop
6. map
7. filter
8. reduce
9. find/findIndex
10. some.every


---
---

## Playwright locators
1. Filtering by text:
```Typescript title="example.test.ts"
const tuna = page.locator('td', {hasText: 'AUTUMN'}); // find all <td> elements that contain the text 'AUTUMN'

```
2. Picking one match : first(), nth() and last()
3. Assertion of `toHaveCss()` // useful when you are checking if an element is highlighted or not.
4. Assertion using `toHaveAttribute()` // checks an HTML attribute
5. Assertion using `toHaveText()` // checks exact text
6. Assetion using `toContainText()` // checks text contains a smaller piece.
7. `locator().count()` // how many locators are there in DOM.
8. Narrowing an existing locator using `filter({hasText})`
```Typescript title="example.test.ts"
const autumnCells = table.locator('td').filter({hasText: 'tuna'});

const autumnCells2 = table.locator('td').filter({hasText: 'tuna'}).locator(':scope'); // :scope means "the element matched so far"
```

Checking if a table has highlighted the locator
```Typescript title="example.test.ts"
const usedAutumnCells = promotionsHomePage
.getUsedForecastMatch()
.locator('td', {hasText:'Autumn});

const count = await usedAutumnCells.count();
expect(count).toBeGreaterThanOrEqual(2);

for(let i=0; i < count; i++){
	await expect(usedAutumnCells.nth(i))
	.toHaveCSS('background-color','rgb(224,239,245)');
}
```