
## Important Error/Warning to know.
#### The Error / Warning

```
Warning: To load an ES module, set "type": "module" in package.json
Reparsing as ES module because module syntax was detected.
```

#### Why It Happens

Node.js **defaults to CommonJS**, but your file uses **ES Module syntax (`import` / `export`)**.  
Node first tries **CommonJS**, detects ES syntax, then **reparses the file as an ES module**, which triggers the warning and adds a small performance cost.

### Simple Example

**File: `demo.js`**

```js
import { chromium } from "playwright";

console.log("Running Playwright");
```

Node expects **CommonJS**, but `import` is **ES module syntax**, so it shows the warning.

### Ways to Fix

**1️⃣ Tell Node to use ES Modules (recommended)**

```json
{
  "type": "module"
}
```

**2️⃣ Rename the file**

```
demo.mjs
```

**3️⃣ Use CommonJS syntax**

```js
const { chromium } = require("playwright");
```

✅ **Summary:** The warning happens because **Node expects CommonJS but detects ES module syntax**, so you must explicitly choose one module system.


---

## How to Import and use assert in Node.js (using ES modules and not CommonJS)

```javascript title="demo.js"
import {chromium} from 'playwright';
import assert from 'assert';

const text = "Swagg";

assert.equal(text, 'Swag Labs');
console.log("passed node.js assert");
```

## Promise in Javascript

A Promise = a future result of an async operation
3 states:
- Pending
- Resolved (success)
- Rejected (error)

#### Why this matters for Playwright

Most browser operations are **async**.
Example:
```Javascript
page.click()  
page.goto()  
page.locator()
```

These return **Promises**.

---

## `await` keyword

`await` **waits for a Promise to finish before moving forward**.
Must be inside an **async function**.

#### Example without await
```Javascript
page.goto("https://google.com");  
page.click("text=Login");
```

⚠️ Problem  
The click might happen **before page loads**.

---

#### Correct version
```Typescript
await page.goto("https://google.com");  
await page.click("text=Login");
```

Now execution becomes **sequential**.

---

### Example
```Typescript
async function login() {  
  await page.fill('#username', 'admin');  
  await page.fill('#password', '123');  
  await page.click('#login');  
}
```

### Mental Model
```
Promise = future result  
await = pause until result arrives
```

---

## Is `Annonymous` function same as `arrow` function?

**No.**  
An **arrow function is a type of anonymous function**, but **not all anonymous functions are arrow functions**.

#### 1️⃣ Anonymous function (traditional)

```js
const login = function () {
  console.log("login");
};
```

- No function name → **anonymous**
- Uses `function` keyword

---

#### 2️⃣ Arrow function (modern syntax)

```js
const login = () => {
  console.log("login");
};
```

- Also **anonymous**
- Uses `=>`

---

#### Key Difference (important)

Arrow functions **do NOT have their own `this`**, traditional functions do.

---

#### Playwright example

Anonymous function:

```ts
test('login test', async function ({ page }) {
});
```

Arrow function (more common):

```ts
test('login test', async ({ page }) => {

});
```

---

✅ **Simple rule**

```
Arrow function ⊂ Anonymous function
```

All arrow functions are anonymous, but not all anonymous functions are arrow functions.
