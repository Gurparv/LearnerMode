- [[#Selenium]]
- [[#Playwright (Python)]]
- [[#Playwright (TS)]]

## Selenium

# 1️⃣ Selenium + Java (Industry Framework Skeleton)

Most companies use **Maven + TestNG + Selenium + POM + utilities**.
```
selenium-java-framework/
│
├── pom.xml
├── testng.xml
├── Jenkinsfile
├── README.md
│
├── src
│   ├── main
│   │   └── java
│   │       └── framework
│   │           ├── base
│   │           │    └── BaseTest.java
│   │           │
│   │           ├── driver
│   │           │    └── DriverFactory.java
│   │           │
│   │           ├── pages
│   │           │    └── LoginPage.java
│   │           │
│   │           ├── utils
│   │           │    ├── WaitUtils.java
│   │           │    ├── ScreenshotUtils.java
│   │           │    └── ConfigReader.java
│   │           │
│   │           └── constants
│   │                └── FrameworkConstants.java
│
│   └── test
│        └── java
│            └── tests
│                 ├── LoginTest.java
│                 └── CheckoutTest.java
│
├── testdata
│    └── users.json
│
├── config
│    └── config.properties
│
└── reports
     └── extent-reports
```

### Key design

- **POM (Page Object Model)**
- **ThreadLocal WebDriver for parallel tests**
- **TestNG lifecycle control**
- **Extent Reports / Allure**
- **CI integration (Jenkins/GitHub)**

---

## Playwright (Python)
# 2️⃣ Playwright + Python Framework Skeleton

Used in modern **backend / API / UI automation stacks**.
```
playwright-python-framework/
│
├── playwright.config.py
├── requirements.txt
├── pytest.ini
├── Jenkinsfile
│
├── framework
│   ├── base
│   │     └── base_test.py
│   │
│   ├── pages
│   │     └── login_page.py
│   │
│   ├── fixtures
│   │     └── browser_fixture.py
│   │
│   ├── utils
│   │     ├── config_reader.py
│   │     ├── logger.py
│   │     └── screenshot.py
│   │
│   └── api
│         └── api_client.py
│
├── tests
│   ├── ui
│   │    └── test_login.py
│   │
│   └── api
│        └── test_user_api.py
│
├── testdata
│    └── users.json
│
└── reports
     └── allure-results
```
### Key design

- **pytest fixtures**
- **Playwright built-in parallelism**
- **Allure reporting**
- **Page object abstraction**

---

## Playwright (TS)

# 3️⃣ Playwright + TypeScript Framework Skeleton (Most modern)

Most **big tech companies** prefer this.
```
playwright-ts-framework/
│
├── playwright.config.ts
├── package.json
├── tsconfig.json
├── Jenkinsfile
│
├── tests
│   ├── ui
│   │    └── login.spec.ts
│   │
│   └── api
│        └── user.spec.ts
│
├── pages
│    └── login.page.ts
│
├── fixtures
│    └── custom-fixtures.ts
│
├── utils
│    ├── config.ts
│    ├── logger.ts
│    └── test-data.ts
│
├── test-data
│    └── users.json
│
└── reports
     └── playwright-report
```

### Key design

- **Playwright test runner**
- **worker scoped fixtures**
- **storageState authentication**
- **parallel test isolation**

