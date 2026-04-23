
- [[#Introduction]]
- [[#Selenium + Java (POM Example)]]
- [[#Playwright + Python (POM Example)]]
- [[#Playwright + TypeScript (POM Example)]]
## Introduction

I'll show **minimal but real-world style POM implementations** for:

1️⃣  **Selenium + Java**  
2️⃣  **Playwright + Python**  
3️⃣  **Playwright + TypeScript**

Each will include:
- **Page class**
- **Test class**
- **Explanation**

These are the **same patterns used in production frameworks**, just simplified.

---

## 1️⃣ Selenium + Java (POM Example)

### Page Object
```java title="LoginPage.java"
package framework.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class LoginPage {

    private WebDriver driver;

    private By username = By.id("username");
    private By password = By.id("password");
    private By loginBtn = By.id("login");

    public LoginPage(WebDriver driver){
        this.driver = driver;
    }

    public void enterUsername(String user){
        driver.findElement(username).sendKeys(user);
    }

    public void enterPassword(String pass){
        driver.findElement(password).sendKeys(pass);
    }

    public void clickLogin(){
        driver.findElement(loginBtn).click();
    }

    public void login(String user,String pass){
        enterUsername(user);
        enterPassword(pass);
        clickLogin();
    }
}
```

### Test
```Java title="LoginTest.java"
package tests;

import framework.pages.LoginPage;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.*;

public class LoginTest {

    WebDriver driver;

    @BeforeMethod
    public void setup(){
        driver = new ChromeDriver();
        driver.get("https://example.com/login");
    }

    @Test
    public void testLogin(){

        LoginPage loginPage = new LoginPage(driver);
        loginPage.login("admin","password");

    }

    @AfterMethod
    public void teardown(){
        driver.quit();
    }
}
```


## Key Idea

```
Test -> calls -> Page Object -> interacts with UI
```

Test **never directly touches locators**.

---

## 2️⃣ Playwright + Python (POM Example)

### Page Object

```python title="login_page.py"
class LoginPage:

    def __init__(self, page):
        self.page = page
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.login_btn = page.locator("#login")

    def login(self, user, password):
        self.username.fill(user)
        self.password.fill(password)
        self.login_btn.click()
```

### Test
```python title="test_login.py"
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage


def test_login():

    with sync_playwright() as p:

        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://example.com/login")

        login_page = LoginPage(page)
        login_page.login("admin", "password")

        browser.close()

```

## Key Idea

```
Test → Page class → locator abstraction
```

Page class **owns the UI logic**.

---

## 3️⃣ Playwright + TypeScript (POM Example)

This is **most common in modern SDET stacks**.

### Page Object

```Typescript title="login.page.ts"
import { Page } from '@playwright/test';

export class LoginPage {

  readonly page: Page;

  constructor(page: Page) {
    this.page = page;
  }

  async login(username: string, password: string) {

    await this.page.fill('#username', username);
    await this.page.fill('#password', password);
    await this.page.click('#login');

  }
}
```

### Test
```typescript title="login.spec.js"
import { test } from '@playwright/test';
import { LoginPage } from '../pages/login.page';

test('login test', async ({ page }) => {

  await page.goto('https://example.com/login');

  const loginPage = new LoginPage(page);

  await loginPage.login('admin', 'password');

});
```


---

## Final Thoughts
# 4️⃣ How Elite Frameworks Improve This POM

Real frameworks usually add:

|Improvement|Why|
|---|---|
|BasePage class|common actions|
|Locator centralization|maintainability|
|Wait utilities|stability|
|API abstraction|faster setup|
|Test data factories|isolation|
|reusable components|modularity|
# 5️⃣ Interview One-liner

If interviewer asks **"What is POM?"**

Answer:

> "Page Object Model is a design pattern where each page of the application is represented as a class containing locators and page actions, separating test logic from UI interactions to improve maintainability and reusability."


✅ If you want, I can also show you something **extremely important most SDETs miss**:

**How FAANG companies structure POM differently from the traditional Page Object Model (they use Page Components + Screenplay pattern).**

This can **instantly make you stand out in interviews.**