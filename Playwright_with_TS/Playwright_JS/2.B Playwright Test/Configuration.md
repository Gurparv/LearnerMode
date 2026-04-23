
Documentation -> https://playwright.dev/docs/test-configuration

- [[#Introduction]]
- [[#Basic Configuration Options]]
- [[#Filtering Tests using Regular Expressions Options]]
- [[#Advanced Configuration Options]]
- [[#Expect Options]]
## Introduction
Playwright has many options to configure how your tests are run. You can specify these options in the configuration file. Note that ==test runner options== are **top-level**, do not put them into the `use` section.

## Basic Configuration Options

|Option|Description|
|---|---|
|[testConfig.forbidOnly](https://playwright.dev/docs/api/class-testconfig#test-config-forbid-only)|Whether to exit with an error if any tests are marked as `test.only`. Useful on CI.|
|[testConfig.fullyParallel](https://playwright.dev/docs/api/class-testconfig#test-config-fully-parallel)|have all tests in all files to run in parallel. See [Parallelism](https://playwright.dev/docs/test-parallel) and [Sharding](https://playwright.dev/docs/test-sharding) for more details.|
|[testConfig.projects](https://playwright.dev/docs/api/class-testconfig#test-config-projects)|Run tests in multiple configurations or on multiple browsers|
|[testConfig.reporter](https://playwright.dev/docs/api/class-testconfig#test-config-reporter)|Reporter to use. See [Test Reporters](https://playwright.dev/docs/test-reporters) to learn more about which reporters are available.|
|[testConfig.retries](https://playwright.dev/docs/api/class-testconfig#test-config-retries)|The maximum number of retry attempts per test. See [Test Retries](https://playwright.dev/docs/test-retries) to learn more about retries.|
|[testConfig.testDir](https://playwright.dev/docs/api/class-testconfig#test-config-test-dir)|Directory with the test files.|
|[testConfig.use](https://playwright.dev/docs/api/class-testconfig#test-config-use)|Options with `use{}`|
|[testConfig.webServer](https://playwright.dev/docs/api/class-testconfig#test-config-web-server)|To launch a server during the tests, use the `webServer` option|
|[testConfig.workers](https://playwright.dev/docs/api/class-testconfig#test-config-workers)|The maximum number of concurrent worker processes to use for parallelizing tests. Can also be set as percentage of logical CPU cores, e.g. `'50%'.`. See [Parallelism](https://playwright.dev/docs/test-parallel) and [Sharding](https://playwright.dev/docs/test-sharding) for more details.|
Example of how to add configuration to `playwright.config.ts` file

```Javascript title="playwright.config.ts"
import { defineConfig } from '@playwright/test';  
  
export default defineConfig({  
fullyParallel: true,  
});
```


## Filtering Tests using Regular Expressions Options

|Option|Description|
|---|---|
|[testConfig.testIgnore](https://playwright.dev/docs/api/class-testconfig#test-config-test-ignore)|Glob patterns or regular expressions that should be ignored when looking for the test files. For example, `'*test-assets'`|
|[testConfig.testMatch](https://playwright.dev/docs/api/class-testconfig#test-config-test-match)|Glob patterns or regular expressions that match test files. For example, `'*todo-tests/*.spec.ts'`. By default, Playwright runs `.*(test\|spec).(js\|ts\|mjs)` files.|
```javascript title="playwright.config.ts"
import { defineConfig } from '@playwright/test';

export default defineConfig({
  testIgnore: '**/test-assets/**',
});
```
## Advanced Configuration Options

|Option|Description|
|---|---|
|[testConfig.globalSetup](https://playwright.dev/docs/api/class-testconfig#test-config-global-setup)|Path to the global setup file. This file will be required and run before all the tests. It must export a single function.|
|[testConfig.globalTeardown](https://playwright.dev/docs/api/class-testconfig#test-config-global-teardown)|Path to the global teardown file. This file will be required and run after all the tests. It must export a single function.|
|[testConfig.outputDir](https://playwright.dev/docs/api/class-testconfig#test-config-output-dir)|Folder for test artifacts such as screenshots, videos, traces, etc.|
|[testConfig.timeout](https://playwright.dev/docs/api/class-testconfig#test-config-timeout)|Playwright enforces a [timeout](https://playwright.dev/docs/test-timeouts) for each test, 30 seconds by default. Time spent by the test function, test fixtures and beforeEach hooks is included in the test timeout.|
```Javascript title="playwright.config.ts"
import { defineConfig } from '@playwright/test';

export default defineConfig({
  globalSetup: './global-setup',
});
```
## Expect Options

|Option|Description|
|---|---|
|[testConfig.expect](https://playwright.dev/docs/api/class-testconfig#test-config-expect)|[Web first assertions](https://playwright.dev/docs/test-assertions) like `expect(locator).toHaveText()` have a separate timeout of 5 seconds by default. This is the maximum time the `expect()` should wait for the condition to be met. Learn more about [test and expect timeouts](https://playwright.dev/docs/test-timeouts) and how to set them for a single test.|
|[expect(page).toHaveScreenshot()](https://playwright.dev/docs/api/class-pageassertions#page-assertions-to-have-screenshot-1)|Configuration for the `expect(locator).toHaveScreenshot()` method.|
|[expect(value).toMatchSnapshot()](https://playwright.dev/docs/api/class-snapshotassertions#snapshot-assertions-to-match-snapshot-1)|Configuration for the `expect(locator).toMatchSnapshot()` method.|