1. [[#Introduction]]
2. [[#Recording a Trace]]
3. [[#Viewing the trace]]
## Introduction
Playwright Trace Viewer is a GUI tool that lets you explore recorded Playwright traces of your tests, meaning you can go back and forward through each action of your test and visually see what was happening during each action.


## Recording a Trace

By default the [playwright.config](https://playwright.dev/docs/trace-viewer#tracing-on-ci) file contains the configuration needed to create a `trace.zip` file for each test. Traces are setup to run `on-first-retry`, meaning they run on the first retry of a failed test. Also `retries` are set to 2 when running on CI and 0 locally. This means the traces are recorded on the first retry of a failed test but not on the first run and not on the second retry

```typescript title="playwright.config.ts"
import { defineConfig } from '@playwright/test';
export default defineConfig({
  retries: process.env.CI ? 2 : 0, // set to 2 when running on CI
  // ...
  use: {
    trace: 'on-first-retry', // record traces on first retry of each test
  },
});
```

To learn more about available options to record a trace check out our detailed guide on [Trace Viewer](https://playwright.dev/docs/trace-viewer).

Traces are normally run in a Continuous Integration (CI) environment, because locally you can use [UI Mode](https://playwright.dev/docs/test-ui-mode) for developing and debugging tests. However, if you want to run traces locally without using [UI Mode](https://playwright.dev/docs/test-ui-mode), you can force tracing to be on with `--trace on`.

```Bash
npx playwright test --trace on
```

## Viewing the trace

View traces of your test by clicking through each action or hovering using the timeline and see the state of the page before and after the action. Inspect the log, source and network, errors, and console during each step of the test. The trace viewer creates a DOM snapshot so you can fully interact with it and open the browser DevTools to inspect the HTML, CSS, etc.

