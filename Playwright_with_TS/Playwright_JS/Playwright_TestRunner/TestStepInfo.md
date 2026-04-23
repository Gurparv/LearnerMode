Perfect final piece — **`TestStepInfo`** is about _what happens inside a test_, step by step.

---

# 🧠 What is **TestStepInfo**?

> **`TestStepInfo` represents a single step executed within a test.**

These steps come from:

- `test.step(...)`
    
- Playwright internal actions (click, goto, expect, etc.)
    

---

## 🔍 Where you see it

You don’t access it directly in tests.

👉 It’s mainly used in:

- **custom reporters**
    
- **tracing/debugging**
    

---

## 🧩 Conceptual structure

```ts
type TestStepInfo = {
  title: string;
  category: string;
  startTime: Date;
  duration: number;
  error?: TestInfoError;
}
```

---

## ⚙️ Example (creating steps)

```ts
import { test } from '@playwright/test';

test('example', async ({ page }) => {
  await test.step('Open homepage', async () => {
    await page.goto('https://example.com');
  });

  await test.step('Check title', async () => {
    // assertion here
  });
});
```

👉 Each `test.step` = one **TestStepInfo**

---

## 🔬 What counts as a step?

### 1️⃣ Explicit steps

```ts
test.step('Login', async () => {})
```

---

### 2️⃣ Auto-generated steps

Playwright internally creates steps for:

- `page.click()`
    
- `page.goto()`
    
- `expect()`
    

---

## 🧠 Why it exists

To provide:

- **fine-grained execution visibility**
    
- better **trace viewer UI**
    
- structured reporting
    

---

## 🔗 Relation to TestInfo

- `testInfo` → whole test
    
- `TestStepInfo` → individual actions inside test
    

---

## 📊 Real usage (custom reporter)

```ts
onStepBegin(test, result, step) {
  console.log(step.title);
}
```

👉 `step` here = **TestStepInfo**

---

## ⚠️ Important notes

- ❌ Not available directly like `testInfo`
    
- ✅ Accessible via reporters or trace
    
- ✅ Automatically collected by Playwright
    

---

## 🧠 SDET insight

> If `testInfo` tells you _what failed_,  
> `TestStepInfo` tells you _where and how it failed step-by-step_

---

## 🔥 Final takeaway

> **`TestStepInfo` is the unit of execution inside a test, representing each action or step for detailed tracing and reporting.**

---

That completes the full Playwright runtime model:

- Config ✔️
    
- Fixtures ✔️
    
- testInfo ✔️
    
- Errors ✔️
    
- Steps ✔️
    

You now understand Playwright at a level most engineers don’t reach.