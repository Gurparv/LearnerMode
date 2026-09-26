# Advanced Selectors and Handling Dynamic Content

Key Topics:
1. [[#Prioritizing Playwright’s getBy* locators for accessible tests]] 
2. [[#Using fallback selectors (CSS, XPath, text-based) for complex or unsupported cases]] 
3. [[#Managing dynamic elements with auto-wait and custom waits]] 
4. [[#Handling alerts and confirmation dialogs]] 
5. [[#Interacting with iframes and nested frames]] 
6. [[#Handling shadow DOM component]]

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
`waitForResponse` waits for a network response and allows you to verify the response’s URL, status, or other properties.

Here’s an example:
```Typescript title="example.spec.ts"
await page.waitForResponse(response => response.url().includes('api/orders') && response.status() === 200);
```
This waits for a response to the /api/orders endpoint with a 200 status code.

```Text
Note -> 
waitForRequest and waitForResponse are both used to monitor network activity, but they serve distinct purposes. waitForRequest waits for a specific HTTP request to be initiated by the browser, which matches criteria such as URL or request method. It’s useful for verifying that a request is sent (such as an API call triggered by a user action). In contrast, waitForResponse waits for the server’s response to a specific request, and allows you to inspect the response status, headers, or body (such as confirming a successful API response). In short, waitForRequest watches what’s going out, and waitForResponse watches what’s coming back. Together, they give you great control over network behavior in your tests.
```

#### 3. page.waitForLoadState(state)
This method waits for the page to reach a specific load state.
Here’s an example:

```Typescript title="example.spec.ts"
await page.waitForLoadState('networkidle');
```

You usually won’t need to call this method yourself, since Playwright automatically waits for elements before performing actions.

#### 4. page.waitForFunction(pageFunction, arg, options)
You can use this method to wait until a JavaScript function (`pageFunction`) returns a truthy value when executed in the browser context.
Here’s an example:
```Typescript title="example.test.ts"
await page.waitForFunction('document.querySelector(".my-element") !== null');
```
Here, we’re telling Playwright to wait until an element with class my-element exists.

#### 5. page.waitForEvent(event, options)
Take advantage of this method when you need to wait for a specific event (such as a popup, download, or websocket) to occur on the page.
Here’s an example:
```Typescript title="example.test.ts"
const popup = await page.waitForEvent('popup');
```

This code waits for a new browser window/tab to open and returns the popup page.

#### 6. page.waitForURL(url, options)
This is a method used to pause the script execution until the page’s URL matches a specified value or pattern.
Here’s an example:
```Typescript title="example.test.ts"
await page.waitForURL('**/newpage.html');
```

This is particularly useful for handling page redirects, waiting for navigation to complete, or managing dynamic URL changes during single-page app transitions.

#### 7. page.waitForTimeout(milliseconds)
This method pauses test execution for a specified number of milliseconds. This method is considered an anti-pattern because it introduces hardcoded delays, which can make tests flaky. Playwright encourages using more robust waiting mechanisms that wait for specific conditions rather than arbitrary time intervals.

Here’s an example:
```Typescript title="example.test.ts"
await page.waitForTimeout(3000);
```
Use it only as a last resort for debugging or when no other reliable wait condition exists.

#### 8. page.waitForSelector(selector, options)
This method waits for an element that matches the given selector to show up in the DOM. However, it’s generally not recommended, since Playwright already takes care of waiting for elements to be ready before interacting with them. Using locator objects and web-first assertions helps your code run smoothly without needing to use waitForSelector.
Here’s an example:
```Typescript title="example.spec.ts"
await page.waitForSelector('#submit-button', { state: 'visible', timeout: 5000 });
```

This waits up to 5 seconds for the `#submit-button` element to become visible. You can specify the desired state (such as `'visible', 'hidden'`) and a custom timeout to control how long to wait.

#### 9. page.waitForNavigation(options)
You can use this method to wait for the page to navigate to a new URL, often triggered by actions such as form submissions or link clicks. You can specify the expected URL and timeout.
Here’s an example:
```Typescript title="example.spec.ts"
await page.getByRole('link', { name: 'Dashboard' }).click();
await page.waitForNavigation({ url: 'https://example.com/dashboard', timeout: 10000 });
```

As of Playwright’s recent versions, page.waitForNavigation is considered outdated. Instead, Playwright recommends using page.waitForURL or simply relying on the promise returned by navigation methods such as page.goto(). For instance, when you use await page.goto(url), it already waits for the navigation to finish. So, in most cases, there’s no need to call waitForNavigation separately. If you’re looking to wait for more specific navigation events, you can use something such as page.waitForEvent('navigated') instead.

NOTE ->
Remember, Playwright’s auto-wait feature takes care of most standard cases for you. Try using custom waits only when you’re dealing with something that falls outside of the norm. It’s best to avoid fixed delays such as await page.waitForTimeout(5000). They can slow your tests down; instead, stick with auto-waits or smart custom waits that pause just long enough. Don’t forget: all waiting methods let you set a timeout.

## Handling alerts and confirmation dialogs 

Working with browser dialogs like - alerts, confirmations and prompts is easy. thanks to its event-driven API.
In web applications, these dialogs usually pop up when JavaScript functions such as `window.alert()`, `window.confirm()`, or `window.prompt()` are called. These modal windows pause JavaScript execution until the user responds.

Playwright lets you handle these by listening for the `'dialog'` event on the page. When a dialog shows up, Playwright emits the event and hands you a dialog object you can use to understand what kind of dialog it is. You can use the following:

- `dialog.type()` to find out whether it’s an alert, confirm, or prompt 
- `dialog.message()` to read the message shown in the dialog 
- `dialog.defaultValue()` to see the default input text if it’s a prompt

It also allows you to interact with the dialog:
- `dialog.accept()` is like clicking OK. For prompts, you can pass in a string to simulate user input. 
- `dialog.dismiss()` is like clicking Cancel, which is especially useful with confirm dialogs.

Just make sure to set up your dialog handler before triggering the action that causes the dialog; otherwise, you might miss it.

Suppose the page you are testing may show multiple dialogs. In this case, you can write the following:

```Typescript title="example.spect.ts"
import { test } from '@playwright/test';

test('handle all dialogs', async ({ page }) => {
  page.on('dialog', async dialog => {
    console.log(`Dialog type: ${dialog.type()}, 
                 message: ${dialog.message()}`);
    if (dialog.type() === 'prompt')
      await dialog.accept('some answer');
    else if (dialog.type() === 'confirm')
      await dialog.accept();      // clicks “OK”
    else
      await dialog.dismiss();     // clicks “Cancel”
  });

  await page.goto(' https://testpages.eviltester.com/styled/alerts/alert-test.html');
  await page.getByRole('button', {name: 'Show alert box'}).click();
  await page.getByRole('button', {name: 'Show confirm box'}).click();  
});
```

Here we are using the `page.on()` method because multiple dialogs appear
during the test run. But you can also use `page.once()` if you expect only one
dialog (replace `page.on()` with `page.once()` to see the effect). This prevents
handlers from unintentionally affecting unrelated parts of your test.

To make sure your dialog displays the correct message, you can grab it using dialog.message() and check it against the expected text. This comes in handy when you’re testing things such as error messages, confirmation boxes, or instructional alerts in your app.

---

## Interacting with iframes and nested frames

#### Accessing an iframe
An `<iframe>` element creates an inline frame that loads another HTML
document. It operates as a separate browsing context, meaning elements
inside an iframe are isolated from the parent page.

```Typescript title="example.test.ts"
import { test, expect } from '@playwright/test';

test('Interact with iframe', async ({ page }) => {
  await page.goto('https://testpages.eviltester.com/styled/iframes-test.html');

  // Locate the iframe
  const frame = page.frameLocator('#thedynamichtml');

  // Interact with elements inside the iframe
  await expect(frame.getByRole('heading', { name: 'iFrame' }))
    .toBeVisible();
});

```

Another way to work with iframes is to first get the iframe element using `locator`, then retrieve the actual `Frame` object with `contentFrame()`, and afterward interact with elements inside it:

```Typescript title="example.test.ts"
import { test, expect } from '@playwright/test';

test('Interact with iframe', async ({ page }) => {
  await page.goto('https://testpages.eviltester.com/styled/iframes-test.html');

  // Interact with elements inside the iframe
  await expect(page.locator('#thedynamichtml')
                   .contentFrame()
                   .getByRole('heading', { name: 'iFrame' })
              ).toBeVisible();
});
```

Note-> If your iframes are sourced from a different origin, browser security policies (such as the same-origin policy) might limit what you can do. Playwright does a great job handling many cross-origin situations, but it’s always good to keep potential restrictions in mind.

---

##  Handling shadow DOM component

In web development, the Shadow DOM lets you encapsulate parts of the DOM (such as custom components) so their styles and elements don’t accidentally interfere with the rest of the page. This makes it a bit tricky to access or interact with those nested elements using traditional DOM selectors. Let’s take a look at ways to pierce through this boundary and interact with these encapsulated elements.

### Locating the host element
This is often the most direct way to access elements within a Shadow DOM. You first locate the host element that has the Shadow DOM. From this root locator, you can then query for elements within it using standard Playwright locators.

Let’s imagine you have a custom web component like this:
```html
<my-widget>
 #shadow-root
 <div class="internal-button">Click me!</div>
<style>
.internal-button { color: blue; }
 </style>
</my-widget>
```

```Typescript title="example.test.ts"
import { test, expect } from '@playwright/test';
test('interacting with shadow dom component', async ({ page }) => {
  await page.goto('webpage.html');

  // Locate the host element
  const widget = page.locator('my-widget');

  // Now you can locate elements within the shadow root
  const internalButton = widget.locator('.internal-button');

  // Perform actions on the internal element
  await internalButton.click();
  const buttonText = await internalButton.innerText();
  console.log(buttonText);

  // You can add assertions here to verify the behavior
  // For example, if clicking the button changes something 
  // on the page:
  // await expect(page.locator('#some-indicator')).toHaveText('Button Clicked!');
});
```

In this example, `page.locator('my-widget')` gives us a new locator that is
scoped to the shadow root of the `<my-widget>` element. We can then use
familiar locator strategies such as`.locator(".internal-button")` on
`shadow_root` to find the button

### Using the >>> combinator

Playwright also provides a piercing selector syntax that makes it
straightforward to target elements within an open shadow DOM. The key
operator here is the `>>>` symbol, which tells Playwright to traverse the
shadow boundaries.

Let’s say we use the same HTML structure as before:
```Typescript title="example.test.ts"
import { test } from '@playwright/test';

test('interacting with shadow dom using deprecated combinators', async ({ page }) => {
  await page.goto('webpage.html');

  const internalButton = page.locator('my-widget >>> .internal-button');

  await internalButton.click();
  const buttonText = await internalButton.innerText();
  console.log(buttonText);
});

```

`>>>` acts as an instruction to pierce into any open shadow root. This syntax is
also effective for nested shadow DOM components. If you have multiple
layers, you can chain the selectors:

```Typescript title="example.test.ts"
// Chaining through multiple shadow boundaries:
await page.click('parent-component >>> child-component >>> button');
```

Here, Playwright automatically handles crossing into each shadow boundary defined by the custom elements. 
Keep in mind that this code would also work without the `>>>` symbol. Modern versions of Playwright automatically traverse open shadow roots, so you can use regular CSS, text, or role-based locators without any special syntax (though XPath selectors do not pierce by default).

Note-> Closed Shadow DOMs aren’t accessible from outside the component. That means Playwright locators won’t work in those cases. This isn’t a limitation of Playwright specifically. It’s part of the web standard for encapsulation.
For a deeper dive into the Shadow DOM, see Faraz’s article, Understanding Shadow DOM:
https://blog.logrocket.com/understandingshadow-dom-v1-fa9b81ebe3ac/ 
It explains the core ideas behind the Shadow DOM specification and explores practical use cases.