## ✅ How Beginners Try to Fix

### 1. Replace sleeps with waits

**Selenium**

```java
WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
wait.until(ExpectedConditions.visibilityOf(element));
```

**Playwright**
```ts
await page.locator('#login').waitFor();
```

---

### 2. Use stable selectors

- Avoid XPath like `//div[3]/span[2]`
- Prefer:
```ts
data-testid="login-button"
```

### 🔑 My go-to locator priority (most stable → least)

1. **Dedicated test attributes (BEST)**
    - `data-testid`, `data-test`, `data-qa`
    - Example: `//button[@data-testid='login-btn']`
    - ✅ Explicit, immune to UI/style changes
    - ✅ My default 90% of the time
2. **Accessible attributes**
    - `aria-label`, `role`, `name`
    - Example: `//input[@aria-label='Email']`
    - ✅ Stable + improves accessibility
    - ✅ Great fallback if test IDs missing
3. **Unique IDs (only if truly stable)**
    - `#loginButton`
    - ⚠️ Avoid dynamic/generated IDs
4. **Relative XPath / CSS (anchored to stable parent)**
    - Example: `//form[@data-testid='login-form']//button[@type='submit']`
    - ✅ Good when no direct identifier exists
    - ❌ Never use absolute XPath
5. **Text-based locators (controlled usage)**
    - Example: `//button[normalize-space()='Login']`
    - ⚠️ Breaks with localization/content tweaks
6. **Class-based locators (last resort)**
    - ❌ Classes change often (CSS refactors, frameworks)

### 🔍 What are `data-testid`, `data-test`, `data-qa`?

They are **custom HTML attributes** added **specifically for testing purposes**.

---

### 3. Retry mechanism (basic)

- Test retry (JUnit/TestNG / Playwright retries)
    

---

### 4. Basic Page Object Model (POM)

```ts
class LoginPage {
  async login(user, pass) {
    await this.user.fill(user);
    await this.pass.fill(pass);
    await this.submit.click();
  }
}
```

---

## 🚫 Limitation

- Still flaky at scale
- No CI awareness
- No isolation
- No system-level thinking


---




