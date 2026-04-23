```Bash

selenium-framework
│
├── pom.xml
├── testng.xml
│
├── src
│   │
│   ├── main
│   │   └── java
│   │       │
│   │       ├── base
│   │       │   └── BaseTest.java
│   │       │
│   │       ├── pages
│   │       │   └── LoginPage.java
│   │       │
│   │       ├── utils
│   │       │   ├── DriverFactory.java
│   │       │   ├── ConfigReader.java
│   │       │   └── WaitUtils.java
│   │       │
│   │       └── constants
│   │           └── FrameworkConstants.java
│   │
│   └── test
│       └── java
│           └── tests
│               └── LoginTest.java
│
└── resources
    └── config.properties

```


## **Selenium framework structure explained in a clean tabular format** for better readability.

|**File / Folder**|**Type**|**Use**|**Why We Use It**|
|---|---|---|---|
|**selenium-framework**|Root Folder|Main project directory containing all framework files|Organizes the entire automation project|
|**pom.xml**|Maven Configuration File|Manages dependencies like Selenium, TestNG, WebDriverManager|Automatically downloads and manages required libraries|
|**testng.xml**|TestNG Suite File|Controls which tests run, groups tests, enables parallel execution|Allows flexible test execution without modifying code|
|**src**|Source Folder|Contains all framework and test code|Standard Maven project structure|
|**src/main/java**|Framework Code Folder|Stores reusable framework components|Separates reusable framework code from test scripts|
|**base**|Package|Contains base setup classes|Centralizes browser setup and teardown logic|
|**BaseTest.java**|Java Class|Initializes WebDriver and handles test setup/cleanup|Prevents repeating setup code in every test|
|**pages**|Package|Stores Page Object Model classes|Separates page logic from test logic|
|**LoginPage.java**|Page Class|Contains web elements and actions for the login page|Improves code reuse and maintainability|
|**utils**|Package|Contains helper/utility classes|Provides reusable functions across the framework|
|**DriverFactory.java**|Utility Class|Creates and manages WebDriver instances|Central place to handle browser initialization|
|**ConfigReader.java**|Utility Class|Reads values from configuration files|Avoids hardcoding values like URL or browser|
|**WaitUtils.java**|Utility Class|Handles explicit waits and synchronization|Prevents test failures due to timing issues|
|**constants**|Package|Stores constant values used across framework|Keeps common values centralized|
|**FrameworkConstants.java**|Constants Class|Contains framework-level constants (timeouts, paths, etc.)|Makes maintenance easier|
|**src/test/java**|Test Code Folder|Contains actual test cases|Separates test logic from framework logic|
|**tests**|Package|Stores test classes|Organizes different test scenarios|
|**LoginTest.java**|Test Class|Executes login test scenarios|Validates application functionality|
|**resources**|Resource Folder|Stores configuration and external files|Keeps environment data separate from code|
|**config.properties**|Properties File|Stores configuration like browser, URL, credentials|Allows easy environment changes without code updates|

