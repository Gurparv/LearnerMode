## Introduction

By default, Playwright runs test files in [parallel](https://playwright.dev/docs/test-parallel) and strives for optimal utilization of CPU cores on your machine. In order to achieve even greater parallelisation, you can further scale Playwright test execution by running tests on multiple machines simultaneously. We call this mode of operation "sharding". Sharding in Playwright means splitting your tests into smaller parts called "shards". Each shard is like a separate job that can run independently. The whole purpose is to divide your tests to speed up test runtime.

When you shard your tests, each shard can run on its own, utilizing the available CPU cores. This helps speed up the testing process by doing tasks simultaneously.

In a CI pipeline, each shard can run as a separate job, making use of the hardware resources available in your CI pipeline, like CPU cores, to run tests faster.

Documentation ->https://playwright.dev/docs/test-sharding
