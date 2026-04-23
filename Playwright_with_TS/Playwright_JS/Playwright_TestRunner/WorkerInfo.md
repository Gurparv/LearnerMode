Perfect ending — this is the **execution backbone** of Playwright.

---

# 🧠 What is **WorkerInfo**?

> **`WorkerInfo` provides metadata about the worker process executing your test.**

---

## 🔍 Where you access it

Inside a test:

```ts
import { test } from '@playwright/test';

test('example', async ({}, testInfo) => {
  console.log(testInfo.workerIndex);
});
```

👉 This comes from **WorkerInfo internally**

---

## 🧩 Key properties

### 1️⃣ `workerIndex`

```ts
testInfo.workerIndex
```

- Unique ID of the worker
    
- Starts from `0`
    

---

### 2️⃣ `parallelIndex`

```ts
testInfo.parallelIndex
```

- Index within parallel execution group
    
- Useful in sharding/parallel runs
    

---

### 3️⃣ `project`

```ts
testInfo.project
```

- Project assigned to this worker
    

---

## ⚙️ What is a "worker"?

> A **worker = a separate Node.js process running tests**

- Each worker:
    
    - runs tests independently
        
    - has its own browser instance
        
    - has isolated fixtures
        

---

## 🔄 How it works

```text
Test run starts
   ↓
Playwright creates workers (based on CPU/workers setting)
   ↓
Each worker gets:
   - tests
   - project
   - fixtures
   ↓
Worker executes tests
```

---

## 🧠 Example

```ts
test('demo', async ({}, testInfo) => {
  console.log(`Running on worker: ${testInfo.workerIndex}`);
});
```

Output:

```text
Running on worker: 0
Running on worker: 1
```

---

## 💡 Real SDET use cases

### 1️⃣ Avoid data collision

```ts
const user = `user-${testInfo.workerIndex}`;
```

---

### 2️⃣ Unique test data per worker

- DB users
    
- temp files
    
- ports
    

---

### 3️⃣ Debug parallel issues

- identify flaky tests per worker
    

---

## ⚠️ Important distinction

|Concept|Meaning|
|---|---|
|Worker|Process running tests|
|Test|Individual execution unit|
|Project|Environment config|

---

## 🔥 Key insight

> Workers enable **true parallelism with isolation**

---

## ❗ Note

You don’t directly use a `WorkerInfo` object like:

```ts
workerInfo ❌
```

👉 Instead, it’s exposed via:

```ts
testInfo.workerIndex
testInfo.parallelIndex
```

---

## 🎯 Final takeaway

> **WorkerInfo represents the execution context (worker process) running your test, mainly used for parallelism control and isolation via `workerIndex`.**

---

That’s the full Playwright runtime model — from config → execution → metadata → parallelism.