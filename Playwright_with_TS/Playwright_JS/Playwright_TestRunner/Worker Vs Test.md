Totally fair — **`scope` is the one concept that trips almost everyone initially**. Let’s make it click quickly.

---

# 🧠 What is `scope` in Playwright fixtures?

> **`scope` defines how often a fixture runs**

---

## 🔑 Two types only

|Scope|Runs when|Lifetime|
|---|---|---|
|**`test` (default)**|for every test|short-lived|
|**`worker`**|once per worker|shared across tests|

---

## 🔥 Visual (this is the key)

```text
Worker (process)
  ├── Test 1
  ├── Test 2
  └── Test 3
```

- `test` scope → runs **3 times**
    
- `worker` scope → runs **1 time**
    

---

## ✅ Example (side-by-side)

### 1️⃣ Default (`test` scope)

```ts
const test = base.extend({
  myFixture: async ({}, use) => {
    console.log('runs every test');
    await use();
  }
});
```

👉 Output:

```
runs every test
runs every test
runs every test
```

---

### 2️⃣ Worker scope

```ts
const test = base.extend({
  myFixture: [
    async ({}, use, workerInfo) => {
      console.log('runs once per worker');
      console.log(workerInfo.workerIndex);

      await use();
    },
    { scope: 'worker' }
  ]
});
```

👉 Output:

```
runs once per worker
```

---

## 🎯 When to use what

### ✅ Use `test` scope (default)

- clean state per test
    
- page setup
    
- login flows
    

---

### ✅ Use `worker` scope

- DB connection
    
- test users per worker
    
- expensive setup (once)
    

---

## 🔍 Where is this documented?

👉 Official docs:  
**Fixtures → Execution scope**

Check:  
[https://playwright.dev/docs/test-fixtures](https://playwright.dev/docs/test-fixtures)

(Search: _“scope: 'worker'”_)

---

## 🧠 Why `workerInfo` only works here

Because:

```text
workerInfo belongs to the worker
```

So Playwright only provides it where it makes sense:  
👉 **worker-scoped fixtures**

---

## 🔥 Ultra-simple mental model

```text
test scope   = per test
worker scope = per machine (worker process)
```

---

## ⚡ Final takeaway

> **`scope` controls fixture lifetime — and `workerInfo` is only available when the fixture lives at worker level.**

---

If you want, I can give you a **real-world pattern (DB/user management using worker scope)** — that’s where this becomes super practical.