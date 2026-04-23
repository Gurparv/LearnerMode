## Introduction

Playwright Test runs tests in parallel. In order to achieve that, it runs several worker processes that run at the same time. By default, **test files** are run in parallel. Tests in a single file are run in order, in the same worker process.

- You can configure tests using [`test.describe.configure`](https://playwright.dev/docs/test-parallel#parallelize-tests-in-a-single-file) to run **tests in a single file** in parallel.
- You can configure **entire project** to have all tests in all files to run in parallel using [testProject.fullyParallel](https://playwright.dev/docs/api/class-testproject#test-project-fully-parallel) or [testConfig.fullyParallel](https://playwright.dev/docs/api/class-testconfig#test-config-fully-parallel).
- To **disable** parallelism limit the number of [workers to one](https://playwright.dev/docs/test-parallel#disable-parallelism).

You can control the number of [parallel worker processes](https://playwright.dev/docs/test-parallel#limit-workers) and [limit the number of failures](https://playwright.dev/docs/test-parallel#limit-failures-and-fail-fast) in the whole test suite for efficiency.