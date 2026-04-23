## Introduction

Test retries are a way to automatically re-run a test when it fails. This is useful when a test is flaky and fails intermittently. Test retries are configured in the [configuration file](https://playwright.dev/docs/test-configuration).

## Failures
https://playwright.dev/docs/test-retries#failures

# Retries
Playwright supports **test retries**. When enabled, failing tests will be retried multiple times until they pass, or until the maximum number of retries is reached. By default failing tests are not retried.

```Bash
# Give failing tests 3 retry attempts
npx playwright test --retries=3
```

You can configure retries in the configuration file:
```javascript title="playwright.config.ts"
import { defineConfig } from '@playwright/test';

export default defineConfig({
  // Give failing tests 3 retry attempts
  retries: 3,
});
```

