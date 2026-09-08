# Advanced Selectors and Handling Dynamic Content

Key Topics:
1. [[#Prioritizing Playwright’s getBy* locators for accessible tests]] 
2. [[#Using fallback selectors (CSS, XPath, text-based) for complex or unsupported cases]] 
3. [[#Managing dynamic elements with auto-wait and custom waits]] 
4. Handling alerts and confirmation dialogs 
5. Interacting with iframes and nested frames 
6. Handling shadow DOM components

## Prioritizing Playwright’s getBy* locators for accessible tests
Playwright’s `getBy*` locators are designed to reflect how real users, including those using assistive tech, interact with your site. By leaning on these locators, you’re not only making your tests easier to maintain but you’re also building a more inclusive experience.

### Why getBy* locators beat CSS and XPath
One of the biggest advantages of using these `getBy*` locators is their ability to handle changes in the DOM gracefully. Unlike CSS or XPath, which rely on the layout or style of the page, these locators target the meaning behind the elements (things such as roles, labels, and visible text). That means even if the HTML or styling gets reworked, your tests are more likely to keep running as long as those accessibility attributes stay the same.

For example, instead of writing a complicated CSS selector to target a button, you can just use the following:
```Typescript title="example.spec.ts"
test('Submits the form on button click', async ({ page }) => { const submitButton = await page.getByRole('button', { name: /submit/i }); await submitButton.click(); });
```

Here, `getByRole('button', { name: /submit/i })` tells Playwright to find a button element whose accessible name (such as its visible label or arialabel) matches the case-insensitive regular expression `/submit/i`. 
`/submit/` is the pattern itself: it matches the exact word submit. i is a flag that makes the match case-insensitive, so it will match Submit, submit, SUBMIT, and so on.

### What Is ARIA? 
ARIA (short for Accessible Rich Internet Applications) plays an important role in making websites more inclusive and user-friendly for people who use assistive technologies such as screen readers. It helps by adding extra information to elements on a page (especially custom buttons, pop-ups, sliders, or anything built with JavaScript) that might not be easily understood by default. ARIA roles, states, and properties tell assistive tools what each part of the page is for and how it behaves, so users can navigate and interact with it more easily

The available getBy* locators include the following: 
1. `getByLabel`: Targets elements by their associated label, such as form inputs linked to `<label>` tags
2. `getByRole`: Finds elements by their ARIA role, such as button or dialog, with optional name filtering 
3. `getByPlaceholder`: Locates inputs by their placeholder text 
4. `getByText`: Matches elements by their visible text content 
5. `getByAltText`: Targets images by their alt text 
6. `getByTitle`: Finds elements by their title attribute 
7. `getByTestId`: Locates elements by a custom test ID attribute

### Locator Chaining
In complex scenarios, you may need to narrow down the selection by combining locators. For example, to target a specific button within a form, you can use
```Typescript
page.locator('form').getByRole('button', { name: 'Submit' }).
```

The second test in the script uses page.locator('.shopping_cart_link') instead of a getBy* method, such as getByRole or getByTestId, because of how the element is defined in the HTML of the page.
The target element is as follows:
```Html
<a class="shopping_cart_link" data-test="shopping-cart-link"></a>
```

This tag has no inner text, no accessible role override, and no ARIA label. Playwright’s `getByRole()` or `getByText()` cannot match it without those. Similarly, `getByLabel()`, `getByPlaceholder()`, and so on all depend on accessible attributes or labels, which this element lacks. When accessible labels or roles aren’t available, it’s important to fall back on more general selectors. This leads us to the next section.

---

## Using fallback selectors (CSS, XPath, text-based) for complex or unsupported cases

### CSS selectors
In Playwright, you can use CSS selectors with the `page.locator()` method. Playwright automatically assumes you’re using a CSS selector unless you specify otherwise with something such as `xpath=` at the start. 
For example, if you want to click the first button on a page, you can simply write the following: 
```Typescript title="example.test.ts"
await page.locator('button').click();
```
### Xpath Selectors
XPath is a query language for selecting nodes in an XML or HTML document.
In Playwright, XPath selectors are also supported via `page.locator()`, with any selector starting with // or .. automatically treated as an XPath expression.
To use an XPath selector, pass it to `page.locator()`. For example, here’s how to click a submit button:

```Typescript title="example.spec.ts"
await page.locator('//button[@type="submit"]').click();
```
XPath comes in especially handy when CSS selectors fall short, such as when you need to select elements based on their text content or how they’re nested within other elements:

Playwright also supports explicit XPath prefixes for clarity:
```Typescript title="example.test.ts"
await page.locator('xpath=//button[@type="submit"]').click();
```

### Text-based selectors
If your target element has text content, using page.getByText() can be a more readable and straightforward option compared to CSS or XPath selectors. For example, if you’re looking for a welcome message, you might write the following:

```Typescript title="example.test.ts"
await expect(page.getByText('Welcome, John')).toBeVisible();
```

By default, page.getByText() matches substrings and also normalizes whitespace. This means it treats multiple spaces as one and ignores any leading or trailing spaces. If you need a more precise match, you can finetune your query using options such as exact matching or regular expressions.

For an exact match, you can do something like this:


```Typescript title="example.test.ts"
await page.getByText('Welcome, John', { exact: true }).click();
```

Or, if you’d like to match using a regular expression (for example, if the name might change), try the following:

```Typescript title="example.spec.ts"
await page.getByText(/welcome, [A-Za-z]+$/i).click();
```

```Note
/ and / denote the start and end of the regex; the i flag makes the match case-insensitive. The [A-Za-z]+ pattern matches one or more letters (uppercase or lowercase), and $ asserts that this is the end of the string. So, it would match something such as "Welcome, John" or " welcome, alice", but not "welcome, John123" or "hi, John".
```

You can also use text-based selectors to filter other locators. Suppose you want to click a button that contains the text Submit. Instead of searching by role alone, you can filter by text:
```Typescript title="example.spec.ts"
await page.getByRole('button').filter({ hasText: 'Submit' }).click();
```

Text-based selectors are not always the best fit for every situation. If the text changes frequently (as with localization or dynamic content) your tests might break more often than you’d like.

Besides filtering by text, you can filter locators by child/descendant, not having text, or not having child/descendant.
To learn more, check out https://playwright.dev/docs/locators#filtering-locators.

### Integrating with test IDs
If you find yourself relying on fallback selectors often, it might be a sign that your application lacks sufficient accessibility attributes or stable identifiers. A great way to improve this is by adding test IDs, which give you a more dependable way to target elements.
Playwright makes this easy with `page.getByTestId()`, which looks for elements with a `data-testid` attribute (or another custom attribute if you’ve set one up in your test config).

Here’s an example:
```Typescript
// HTML: Submit await page.getByTestId('submit-button').click();
	await page.getByTestId('submit-button').click();
```

`data-testid is used by default. To use a custom test ID attribute, you can configure it in the Playwright config:
```Typescript title="playwright.config.ts"
import { defineConfig } from '@playwright/test'; 
export default defineConfig({ 
use: { testIdAttribute: 'data-pw' } 
});
```

Test IDs are usually more reliable than CSS or XPath selectors because they’re designed with testing in mind and tend to stay stable even as the code changes.

---

## Managing dynamic elements with auto-wait and custom waits

In this section, we’ll look at how to make your tests more reliable by using Playwright’s smart auto-wait features and adding custom waits when needed.

### How Playwright ensures actions happen at the right time
When you perform actions such as clicking a button or filling in a text field, Playwright automatically ensures that an element is as follows:
- Visible: The element is rendered and visible on the page 
- Stable: The element is not moving or resizing (no ongoing animations) 
- Enabled: The element is not disabled and can be interacted with 
- Receivable: The element can receive input or clicks (not obscured by other elements) 
This built-in waiting eliminates the need for arbitrary pauses (such as fixed delays)

### Using custom waits for specific scenarios
While Playwright’s auto-waiting does a great job in most situations, there are times when you’ll want more control. Custom waits come in handy when you need to wait for something specific.

For example, maybe you’re waiting for a network response, an animation to finish, or a state change in your app that Playwright doesn’t automatically catch. In these cases, custom wait logic helps keep your tests reliable. Luckily, Playwright offers several ways to build custom waits.

#### 1.  page.waitForRequest(urlOrPredicate)
This method waits for a specific network request to be initiated. You can provide a URL or a predicate function to match the request.
Here’s an example:
```Typescript title="example.spec.ts"
await page.waitForRequest('https://example.com/api/data');
```
This is particularly useful for testing API-driven applications.

#### 2. page.waitForResponse(urlOrPredicate)

