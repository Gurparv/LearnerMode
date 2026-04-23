
## Introduction
Playwright was created specifically to accommodate the needs of end-to-end testing. Playwright supports all modern rendering engines including Chromium, WebKit, and Firefox. Test on Windows, Linux, and macOS, locally or on CI, headless or headed with native mobile emulation.

The [Playwright library](https://playwright.dev/python/docs/library) can be used as a general purpose browser automation tool, providing a powerful set of APIs to automate web applications, for both sync and async Python.

There is also a Playwright Pytest plugin, which is the recommended way to write end-to-end tests. Here is the documentation -> https://playwright.dev/python/docs/intro

This introduction describes the Playwright Pytest plugin, which is the recommended way to write end-to-end tests.
## Setting Up Virtual Environment

`python -m venv .venv`

## Installation commands 

`pip install pytest-playwright`
`playwright install`

## First Script
```python

import re
from playwright.sync_api import Page

def test_youtube(page: Page):
	page.goto("https://abc.com")
	print("hello !")

```

## To run the script from terminal
`pytest`
`pytest -s`  // if you want to see print statements on terminal/console