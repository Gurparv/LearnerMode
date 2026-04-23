
## Introduction
There are two ways to configure global setup and teardown: using a global setup file and setting it in the config under [`globalSetup`](https://playwright.dev/docs/test-global-setup-teardown#option-2-configure-globalsetup-and-globalteardown) or using [project dependencies](https://playwright.dev/docs/test-global-setup-teardown#option-1-project-dependencies). With project dependencies, you define a project that runs before all other projects. This is the recommended approach, as it integrates better with the Playwright test runner: your HTML report will include the global setup, traces will be recorded, and fixtures can be used. For a detailed comparison of the two approaches, see the table below.

| Feature                                             | Project Dependencies (recommended) | `globalSetup` (config option)             |
| --------------------------------------------------- | ---------------------------------- | ----------------------------------------- |
| Runs before all tests                               | ✅ Yes                              | ✅ Yes                                     |
| HTML report visibility                              | ✅ Shown as a separate project      | ❌ Not shown                               |
| Trace recording                                     | ✅ Full trace available             | ❌ Not supported                           |
| Playwright fixtures                                 | ✅ Fully supported                  | ❌ Not supported                           |
| Browser management                                  | ✅ Via `browser` fixture            | ❌ Fully manual via `browserType.launch()` |
| Parallelism and retries                             | ✅ Supported via standard config    | ❌ Not applicable                          |
| Config options like `headless` or `testIdAttribute` | ✅ Automatically applied            | ❌ Ignored                                 |
