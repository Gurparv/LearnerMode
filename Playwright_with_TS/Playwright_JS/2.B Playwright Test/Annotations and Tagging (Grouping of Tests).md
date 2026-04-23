
## Quick comparison

|Feature|Tags|Annotations|
|---|---|---|
|Primary purpose|Test grouping/filtering|Test metadata & behavior|
|Affects execution|❌|✅|
|CLI filtering|✅ (`--grep`)|❌|
|Structured metadata|❌|✅|
|Built-in types|❌|✅ (`skip`, `fail`, etc.)|
|Reports|Minimal|Fully visible|
## Annotation Introduction
Annotations can be added to a single test or a group of tests.

You can add your own tags and annotations at any moment, but Playwright comes with a few built-in ones:

- [test.skip()](https://playwright.dev/docs/api/class-test#test-skip) marks the test as irrelevant. Playwright does not run such a test. Use this annotation when the test is not applicable in some configuration.
- [test.fail()](https://playwright.dev/docs/api/class-test#test-fail) marks the test as failing. Playwright will run this test and ensure it does indeed fail. If the test does not fail, Playwright will complain.
- [test.fixme()](https://playwright.dev/docs/api/class-test#test-fixme) marks the test as failing. Playwright will not run this test, as opposed to the `fail` annotation. Use `fixme` when running the test is slow or crashes.
- [test.slow()](https://playwright.dev/docs/api/class-test#test-slow) marks the test as slow and triples the test timeout.

Example
```javascript title="demo.spec.js"
test.only('focus this test', async ({ page }) => {
  // Run only focused tests in the entire project.
});
```

## Conditionally skip a test
You can skip certain test based on the condition.
```javascript demo.spec.js
test('skip this test', async ({ page, browserName }) => {
  test.skip(browserName === 'firefox', 'Still working on it');
});
```

## Group tests
You can group tests to give them a logical name or to scope before/after hooks to the group.
```javascript title="demo.spec.js"
import { test, expect } from '@playwright/test';

test.describe('two tests', () => {
  test('one', async ({ page }) => {
    // ...
  });

  test('two', async ({ page }) => {
    // ...
  });
});
```

## Introduction to Tag tests
Tags are simple labels used mainly for filtering tests.

Sometimes you want to tag your tests as `@fast` or `@slow`, and then filter by tag in the test report. Or you might want to only run tests that have a certain tag.

To tag a test, either provide an additional details object when declaring a test, or add `@`-token to the test title. Note that tags must start with `@` symbol.

```javascript title="demo.spec.js"
import { test, expect } from '@playwright/test';

test('test login page', {
  tag: '@fast',
}, async ({ page }) => {
  // ...
});

test('test full report @slow', async ({ page }) => {
  // ...
});
```

You can now run tests that have a particular tag with [`--grep`](https://playwright.dev/docs/test-cli#all-options) command line option.

```Bash
npx playwright test --grep @fast
```

