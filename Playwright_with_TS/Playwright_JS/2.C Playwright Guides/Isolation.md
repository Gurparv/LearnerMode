## Introduction

Tests written with Playwright execute in isolated clean-slate environments called browser contexts. This isolation model improves reproducibility and prevents cascading test failures.

## What is Test Isolation?

Test Isolation is when each test is completely isolated from another test. Every test runs independently from any other test. This means that each test has its own local storage, session storage, cookies etc. Playwright achieves this using [BrowserContext](https://playwright.dev/docs/api/class-browsercontext "BrowserContext")s which are equivalent to incognito-like profiles. They are fast and cheap to create and are completely isolated, even when running in a single browser. Playwright creates a context for each test, and provides a default [Page](https://playwright.dev/docs/api/class-page "Page") in that context.

## Why is Test Isolation Important?

- No failure carry-over. If one test fails it doesn't affect the other test.
- Easy to debug errors or flakiness, because you can run just a single test as many times as you'd like.
- Don't have to think about the order when running in parallel, sharding, etc.

## How Playwright Achieves Test Isolation
https://playwright.dev/docs/browser-contexts#how-playwright-achieves-test-isolation

## Multiple Contexts in a Single Test
https://playwright.dev/docs/browser-contexts#multiple-contexts-in-a-single-test