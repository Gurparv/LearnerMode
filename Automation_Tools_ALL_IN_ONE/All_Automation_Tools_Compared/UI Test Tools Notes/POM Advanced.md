Good. This is where **elite SDETs separate themselves from average automation engineers.** 🚀

Most people only know **Page Object Model (POM)**.  
But **large-scale automation frameworks (Google, Netflix, Shopify, Uber)** evolve beyond it.

The three patterns used in **advanced frameworks** are:

1️⃣ **Page Object Model (Basic)**  
2️⃣ **Page Component Model (Modern)**  
3️⃣ **Screenplay Pattern (Elite / scalable)**

I'll explain each with **Playwright examples** because that's the **modern industry stack**.

---

# 1️⃣ Traditional Page Object Model (POM)

### Structure

```
tests
pages
   login.page.ts
   dashboard.page.ts
```

### Example

`login.page.ts`

```ts
export class LoginPage {

  constructor(private page){}

  async login(user, password){
    await this.page.fill('#username', user);
    await this.page.fill('#password', password);
    await this.page.click('#login');
  }

}
```

### Test

```ts
test('login test', async ({page}) => {

 const login = new LoginPage(page);

 await login.login("admin","pass");

});
```

---

### Problem with POM

As application grows:

```
LoginPage = 2000 lines
DashboardPage = 4000 lines
```

Huge **God classes** appear.

This is why **modern companies rarely use pure POM anymore.**

---

# 2️⃣ Page Component Model (Modern Industry Approach)

Instead of page-only abstraction, we break **UI into reusable components**.

Example:

```
Navbar
Sidebar
LoginForm
ProductCard
Modal
Table
```

### Structure

```
tests
pages
   login.page.ts

components
   navbar.component.ts
   login-form.component.ts
   sidebar.component.ts
```

---

### Component Example

`login-form.component.ts`

```ts
export class LoginForm {

 constructor(private page){}

 async login(user:string, password:string){

   await this.page.fill('#username', user);
   await this.page.fill('#password', password);
   await this.page.click('#login');

 }

}
```

---

### Page uses Components

`login.page.ts`

```ts
import { LoginForm } from "../components/login-form.component";

export class LoginPage {

 constructor(private page){}

 loginForm = new LoginForm(this.page);

}
```

---

### Test

```ts
test('login', async ({page}) => {

 const loginPage = new LoginPage(page);

 await loginPage.loginForm.login("admin","password");

});
```

---

### Advantages

|Advantage|Why|
|---|---|
|Reusable UI|navbar used everywhere|
|Smaller classes|easier maintenance|
|Team scaling|multiple engineers|
|Test stability|less duplication|

---

# 3️⃣ Screenplay Pattern (Elite / scalable)

Used in **Serenity BDD, advanced Playwright frameworks, Netflix style testing**.

Concept:

Instead of:

```
Test -> Page
```

We do:

```
Actor -> Tasks -> Interactions -> UI
```

---

### Structure

```
tests
actors
tasks
interactions
pages
```

Example:

```
actors
   user.actor.ts

tasks
   login.task.ts

interactions
   click.ts
   type.ts
```

---

### Actor

`user.actor.ts`

```ts
export class Actor {

 constructor(private page){}

 async attemptsTo(task){
   await task.performAs(this.page)
 }

}
```

---

### Task

`login.task.ts`

```ts
export class LoginTask {

 constructor(private user, private password){}

 async performAs(page){

   await page.fill('#username', this.user)
   await page.fill('#password', this.password)
   await page.click('#login')

 }

}
```

---

### Test

```ts
test('login', async ({page}) => {

 const user = new Actor(page);

 await user.attemptsTo(
     new LoginTask("admin","password")
 );

});
```

---

### Advantages

|Advantage|Why|
|---|---|
|Highly readable|business language|
|Reusable tasks|login reused everywhere|
|Test abstraction|UI changes don't break tests|
|Scales to 10000+ tests|large systems|

---

# 4️⃣ What FAANG SDET frameworks actually look like

Most mature frameworks combine:

```
Page Components
+
Screenplay Tasks
+
Fixtures
+
Test Data Factories
```

Structure example:

```
tests
fixtures
pages
components
tasks
interactions
data
utils
```

Example flow:

```
Test
 ↓
Actor
 ↓
Task
 ↓
Component
 ↓
Locator
```

---

# 5️⃣ Real framework architecture used by elite teams

```
tests
   checkout.spec.ts

fixtures
   auth.fixture.ts

pages
   checkout.page.ts

components
   cart.component.ts
   navbar.component.ts

tasks
   login.task.ts
   add-product.task.ts

utils
   api.client.ts
   data.factory.ts
```

---

# 6️⃣ Interview Killer Answer ⭐

If interviewer asks:

**"How do you structure scalable automation frameworks?"**

Answer:

> "I start with Page Object Model but evolve it using Page Components to avoid large page classes. For large frameworks I introduce the Screenplay pattern where actors perform reusable tasks composed of interactions. This makes the framework scalable, readable, and maintainable for thousands of tests."

---

# 7️⃣ What most engineers still don't know

The **real power of modern frameworks is not POM**.

It's:

### 🔥 Test Data Factories + Parallel Isolation

Without that:

```
1000 parallel tests
= data collision
= flaky tests
```

This is **the #1 problem elite SDETs solve.**

---

✅ If you want, I can also show you something **very valuable for interviews**:

**"The architecture of a FAANG-level Playwright framework capable of running 10,000 parallel tests safely."**

Most SDETs **completely fail this interview question.**