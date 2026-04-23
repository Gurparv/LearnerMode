
Documentation -> https://playwright.dev/docs/test-use-options

- [[#Introduction]]
- [[#Basic Options]]
- [[#Emulation Options]]
- [[#Network Options]]
- [[#Recording Options]]
- [[#Other Options]]
- [[#More browser and context options]]
- [[#Explicit Context Creation and Option Inheritance]]
- [[#Configuration Scopes]]
- [[#Reset an option]]

## Introduction

In addition to configuring the test runner you can also configure [Emulation](https://playwright.dev/docs/test-use-options#emulation-options), [Network](https://playwright.dev/docs/test-use-options#network-options) and [Recording](https://playwright.dev/docs/test-use-options#recording-options) for the [Browser](https://playwright.dev/docs/api/class-browser "Browser") or [BrowserContext](https://playwright.dev/docs/api/class-browsercontext "BrowserContext"). These options are passed to the `use: {}` object in the Playwright config.

## Basic Options
Set the base URL and storage state for all tests:

|Option|Description|
|---|---|
|[testOptions.baseURL](https://playwright.dev/docs/api/class-testoptions#test-options-base-url)|Base URL used for all pages in the context. Allows navigating by using just the path, for example `page.goto('/settings')`.|
|[testOptions.storageState](https://playwright.dev/docs/api/class-testoptions#test-options-storage-state)|Populates context with given storage state. Useful for easy authentication, [learn more](https://playwright.dev/docs/auth).|
```Javascript title="playwright.config.ts"
import { defineConfig } from '@playwright/test';

export default defineConfig({
  use: {
    // Base URL to use in actions like `await page.goto('/')`.
    baseURL: 'http://localhost:3000',

    // Populates context with given storage state.
    storageState: 'state.json',
  },
});
```

## Emulation Options

With Playwright you can emulate a real device such as a mobile phone or tablet. See our [guide on projects](https://playwright.dev/docs/test-projects) for more info on emulating devices. You can also emulate the `"geolocation"`, `"locale"` and `"timezone"` for all tests or for a specific test as well as set the `"permissions"` to show notifications or change the `"colorScheme"`. See our [Emulation](https://playwright.dev/docs/emulation) guide to learn more.

## Network Options

Available options to configure networking:

## Recording Options
With Playwright you can capture screenshots, record videos as well as traces of your test. By default these are turned off but you can enable them by setting the `screenshot`, `video` and `trace` options in your `playwright.config.js` file.

Trace files, screenshots and videos will appear in the test output directory, typically `test-results`.

## Other Options

## More browser and context options
Any options accepted by [browserType.launch()](https://playwright.dev/docs/api/class-browsertype#browser-type-launch), [browser.newContext()](https://playwright.dev/docs/api/class-browser#browser-new-context) or [browserType.connect()](https://playwright.dev/docs/api/class-browsertype#browser-type-connect) can be put into `launchOptions`, `contextOptions` or `connectOptions` respectively in the `use` section.

## Explicit Context Creation and Option Inheritance
If using the built-in `browser` fixture, calling [browser.newContext()](https://playwright.dev/docs/api/class-browser#browser-new-context) will create a context with options inherited from the config:

## Configuration Scopes
You can configure Playwright globally, per project, or per test. For example, you can set the locale to be used globally by adding `locale` to the `use` option of the Playwright config, and then override it for a specific project using the `project` option in the config. You can also override it for a specific test by adding `test.use({})` in the test file and passing in the options.

## Reset an option
You can reset an option to the value defined in the config file. Consider the following config that sets a `baseURL`:

