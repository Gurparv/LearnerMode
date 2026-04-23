Perfect final topic — this is a small but **very telling API** if you understand it properly.

---

# 🧠 What is **TestInfoError** in Playwright?

> **`TestInfoError` represents an error associated with a test run, exposed via `testInfo.errors`.**

---

## 🔍 Where you see it

Inside a test:

```ts
import { test } from '@playwright/test';

test('example', async ({}, testInfo) => {
  console.log(testInfo.errors);
});
```

👉 `testInfo.errors` = array of **TestInfoError objects**

---

## 🧩 Structure (conceptual)

A `TestInfoError` looks like:

```ts
{
  message: string;
  stack?: string;
  value?: string;
}
```

---

## 📦 What it contains

Each error includes:

- **message** → what failed
    
- **stack** → stack trace
    
- **value** → optional (actual error object/value)
    

---

## 🔥 When is it populated?

### 1️⃣ Assertion failures

```ts
await expect(page).toHaveTitle('Wrong Title');
```

---

### 2️⃣ Runtime errors

```ts
throw new Error('Something broke');
```

---

### 3️⃣ Fixture failures

- setup/teardown issues
    
- browser/context crashes
    

---

## ⚠️ Important behavior

### ✅ It’s an ARRAY

```ts
testInfo.errors.length
```

👉 A test can have **multiple errors**

---

### ✅ Available during test execution

```ts
test('demo', async ({}, testInfo) => {
  try {
    throw new Error('fail');
  } catch {}

  console.log(testInfo.errors); // may already contain failures
});
```

---

### ❗ Not all failures throw immediately

Playwright may:

- collect errors
    
- report them at the end
    

---

## 🧠 Real use cases (SDET level)

### 1️⃣ Custom logging

```ts
if (testInfo.errors.length > 0) {
  console.log('Test failed with:', testInfo.errors);
}
```

---

### 2️⃣ Conditional cleanup

```ts
if (testInfo.errors.length) {
  await page.screenshot({ path: 'failure.png' });
}
```

---

### 3️⃣ Debug flaky tests

- inspect multiple failure points
    
- correlate with retries
    

---

## ❌ Common misunderstanding

> “TestInfoError is a class I can import”

👉 Not really useful directly

You usually interact with:

```ts
testInfo.errors
```

---

## 🧠 Key distinction

|Concept|Meaning|
|---|---|
|`Error`|JS runtime error|
|`TestInfoError`|Playwright-wrapped test error|
|`testInfo.errors`|collected errors for the test|

---

## 🔥 Final takeaway

> **`TestInfoError` is Playwright’s structured representation of test failures, accessible via `testInfo.errors` for inspection, logging, and debugging.**

---

That’s the last missing puzzle piece in the `testInfo` ecosystem.


----
---

==tell me in concise the difference between testInfo.errors and testInfo.error==

### ✅ Concise difference

|Property|Meaning|
|---|---|
|**`testInfo.errors`**|👉 **Array of all errors** that occurred in the test|
|**`testInfo.error`**|👉 **First (primary) error only**|

---

## 🔑 In one line

> **`errors` = everything, `error` = main failure**

---

## 🧠 Example

```ts
test('demo', async ({}, testInfo) => {
  console.log(testInfo.error);   // single error (or undefined)
  console.log(testInfo.errors);  // array of all errors
});
```

---

## ⚠️ Important nuance

- `testInfo.error` is basically:
    

```ts
testInfo.errors[0]
```

- If no failure:
    

```ts
testInfo.error === undefined
testInfo.errors.length === 0
```

---

## 🔥 When to use what

- Use **`testInfo.error`** → quick check / main failure
    
- Use **`testInfo.errors`** → debugging, logging, multiple failures
    

---

## 🎯 Final takeaway

> **`error` is a shortcut; `errors` is the full truth.**