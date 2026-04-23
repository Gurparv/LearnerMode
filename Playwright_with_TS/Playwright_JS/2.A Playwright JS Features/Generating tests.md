1. [[#Introduction]]
2. [[#Running Codegen]]
3. [[#What can you do with Codegen]]
4. [[#Generating locators]]
5. [[#Emulation]]
## Introduction
- In Playwright, you can generate tests automatically using Playwright Codegen.
- Codegen analyzes the rendered page and recommends the best locator, prioritizing role, text, and test id locators. When multiple elements match a locator, the generator improves it to uniquely identify the target element, reducing test failures and flakiness.

## Running Codegen
```Bash
npx playwright codegen <url>
```

## What can you do with Codegen

With the test generator you can record:
- Actions like click or fill by interacting with the page
- Assertions by clicking a toolbar icon, then clicking a page element to assert against. You can choose:
    - `'assert visibility'` to assert that an element is visible
    - `'assert text'` to assert that an element contains specific text
    - `'assert value'` to assert that an element has a specific value
    - `assert snapshot` 

When you finish interacting with the page, press the `'record'` button to stop recording and use the `'copy'` button to copy the generated code to your editor.

Use the `'clear'` button to clear the code and start recording again. Once finished, close the Playwright Inspector window or stop the terminal command.

To learn more about generating tests, check out our detailed guide on [Codegen](https://playwright.dev/docs/codegen).

## Generating locators
You can generate [locators](https://playwright.dev/docs/locators) with the Codegen
Use the copy button to copy the locator and paste it into your code

## Emulation

You can generate tests using emulation for specific viewports, devices, color schemes, geolocation, language, or timezone. The test generator can also preserve authenticated state. Check out the [Test Generator](https://playwright.dev/docs/codegen#emulation) guide to learn more.