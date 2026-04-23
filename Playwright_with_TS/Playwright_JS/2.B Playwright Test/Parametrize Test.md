## Introduction

You can either parameterize tests on a test level or on a project level.

## Parameterized Tests
```javascript title="example.spec.ts"
[
  { name: 'Alice', expected: 'Hello, Alice!' },
  { name: 'Bob', expected: 'Hello, Bob!' },
  { name: 'Charlie', expected: 'Hello, Charlie!' },
].forEach(({ name, expected }) => {
  // You can also do it with test.describe() or with multiple tests as long the test name is unique.
  test(`testing with ${name}`, async ({ page }) => {
    await page.goto(`https://example.com/greet?name=${name}`);
    await expect(page.getByRole('heading')).toHaveText(expected);
  });
});
```



## Parameterized projects
Playwright Test supports running multiple test projects at the same time. In the following example, we'll run two projects with different options.

We declare the option `person` and set the value in the config. The first project runs with the value `Alice` and the second with the value `Bob`.

https://playwright.dev/docs/test-parameterize#parameterized-projects


## Passing Environment Variables
https://playwright.dev/docs/test-parameterize#passing-environment-variables