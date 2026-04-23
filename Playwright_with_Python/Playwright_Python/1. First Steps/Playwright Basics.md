**Headings**
1. [[#Different Ways to start Playwright]]
2. [[#Device Emulation]]
3. [[#Take Screenshot]]
4. [[# Run on specific Browser only]]
5. [[#Filter components]]
6. [[#New Tab]]
7. [[#Alerts]]
8. [[#Frames]]
9. [[#Mouse Hover]]
10. [[#Web Table]]
11. [[#Set ViewPort Size]]
12. [[#Open Window in Maximized mode]]
13. [[#Focus on tab when multiple tabs are open.]]
14. [[#Type like a human would]]
15. [[#Slowmo setup]]
16. [[#TODO File upload]]
17. [[#TODO Drag and Drop]]
18. [[#TODORight click]]



## Different Ways to start Playwright

1.
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    chrome = playwright.chromium.launch(headless=False)
    context = chrome.new_context()
    page = context.new_page()
    page.goto("https://playwright.dev/python/docs/test-runners")
```

2. 
```python
from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
chromium = playwright.chromium
chrome = chromium.launch(headless=False)
context = chrome.new_context()
page = context.new_page()
page.goto("https://playwright.dev/python/docs/library")
page.screenshot(path="demo2.png")
page.close()
context.close()
chrome.close()
playwright.stop()
print("everything is closed")
```

3. Open Playwright using pytest fixtures (page)
```python 
def test_ss(page):
    page.goto("https://www.youtube.com/")

# Note there are other fixtures too like 'browser', 'context' etc Refer Documentation 'Pytest Plugin reference'
```

4. Open Playwright using pytest fixtures but with hint
```Python
def test_youtube(page: Page):
	page.goto("https://abc.com)
	print("hello!")
```

5. another way
```Python
from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://example.com")
    # other actions...
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```

6. playwright fixture
```Python
def test_1(playwright):
	playwright.chromium.launch()
```

Tip if suggestions not coming then import fixture

```python
from playwright.sync_api import Page

def test_playwrightSHortcut(page: Page):
	page.goto("url")
	# now suggestions should come.
```

---

## Device Emulation

Running on Device Eg 'Iphone 13'
```Python
from playwright.sync_api import sync_playwright
 
playwright = sync_playwright().start()
iphone = playwright.devices['iPhone 13']
chrome = playwright.chromium.launch(headless=False)
context = chrome.new_context(**iphone,)
page = context.new_page()
page.goto("https://www.google.com/")
page.screenshot(path="my_devices_iphone_ss.png")
print("end devices")
```

---

## Take Screenshot
1. Take screenshot
```python
from playwright.sync_api import sync_playwright
 
chrome = sync_playwright().start().chromium.launch()
context = chrome.new_context()
page = context.new_page()
page.goto("https://www.youtube.com/")

# take screenshot
page.screenshot(path="my_screenshot.png") 

page.close()
context.close()
chrome.close()
print("end")
```

2. Take Screenshot 2
```python
def test_demo(page):
    page.goto("https://playwright.dev/python/docs/library")
    page.screenshot(path="test_demo_screenshot.png")
```

---

## Record Video 
Record Video in playwright

```python
from playwright.sync_api import sync_playwright

chrome = sync_playwright().start().chromium.launch()

#Record video
context = chrome.new_context(record_video_dir="videos/")

page = context.new_page()
page.goto("https://www.geeksforgeeks.org/machine-learning/machine-learning-model-evaluation/")
page.goto("https://www.youtube.com/")
page.goto("https://www.google.com/")
 
page.close()
context.close()
chrome.close()
print("end")
```

---

## Run on specific browser only

```Python
from playwright.sync_api import Page
import pytest


@pytest.mark.only_browser("firefox")
def test_demo(page: Page):
    page.goto("https://playwright.dev/python/docs/test-runners")
    breakpoint()
    
# Cmd command -> pytest --browser-channel firefox
```

```Python
# Open Edge browser in Playwright
def test_demo4(playwright: Playwright):   
    browser = playwright.chromium.launch(channel="msedge",headless=False)  
    contxt = browser.new_context(no_viewport=True)  
    page = contxt.new_page()  
    page.goto("https://rahulshettyacademy.com/AutomationPractice")
```

---

## Filter Components

```Python
iphone_locator = page.locator("some css").filter(has_text="iphone")
iphone_locator.get_by_role("button").click()
```

---

## New Tab

```Python
page.goto("")
page.locator("xpath of element which when clicked opens new tab").click()
with page.expect_popup() as my_new_tab:
	my_chid_page = my_new_tab.value
	my_child_page.locator("")
```

```Python
# Handle Pop-up or New Tab
 
page.goto("https://rahulshettyacademy.com/AutomationPractice")  
  
with page.expect_event("popup") as new_page:  
    page.locator("xpath=//button[text()='Open Window']").click()  
popup_window = new_page.value

print( popup_window.title() )

# Method 2
page.goto("https://rahulshettyacademy.com/AutomationPractice")  
  
with page.expect_popup() as new_page:  
    page.locator("xpath=//button[text()='Open Window']").click()  
popup_window = new_page.value

print(popup_window.title())
```

---

## Alerts
```Python
def test_checks(page: Page):	
	page.on("dialog",lambda dialog:dialog.accept())
```

```Python
# New tab
# Alert
browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])  
context = browser.new_context(no_viewport=True)  
page = context.new_page()  
page.goto("https://rahulshettyacademy.com/AutomationPractice")  
#page.expect_event("dialog")  
page.on("dialog", lambda dialog: print(dialog.message))  
page.locator("xpath=//input[@id='alertbtn']").click()  
time.sleep(5)

# Example 2
def my_alert_handler(dialog):  
    print()  
    print(dialog.message)  
    dialog.accept()  
    
def test_demo3(playwright: Playwright):  
    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])  
    context = browser.new_context(no_viewport=True)  
    page = context.new_page()  
    page.goto("https://rahulshettyacademy.com/AutomationPractice")  
    #page.expect_event("dialog")  
    #page.on("dialog", lambda dialog: print(dialog.message))    page.on("dialog", my_alert_handler)  
    page.locator("xpath=//input[@id='alertbtn']").click()  
    time.sleep(5)
```

---
## Frames
```Python
def test_checks(page:Page):
	my_iframe = page.frame_locator("")
	my_iframe.get_by_role("") # here searches are happening in inscope of 'my_iframe' only.
```

---

## Mouse Hover
```Python
page.locator("").hover()
```

---

## Web Table
```Python
for index in range(page.locator("th").count()):
	if page.locator("th").nth(index).filter(has_text="Price").count()>0:
		colValue = index
		print(f"price value is {colValue}")
		
```

---
## Set Viewport Size
```Python
# 1. To set viewport size (browser size) from Page.
page.set_viewport_size({"width":1920,"height":1080})
```

---

## Open Window in Maximized mode
```Python
# Method 2 to open window in maximized mode.
browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])  
browser_context = browser.new_context(no_viewport=True)  
page = browser_context.new_page()  
page.goto("https://google.com")
```

---

## Focus on tab when multiple tabs are open.
```Python
# WHen 2 windows/tabs are open u want to switch to window 1.
page1.bring_to_front()

## Example 
browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])  
browser_context = browser.new_context(no_viewport=True)  
page = browser_context.new_page()  
page.goto("https://rahulshettyacademy.com/AutomationPractice")  
print()  
print(page.title())  
with page.expect_popup() as newpop:  
    page.locator("xpath=//a[@id='opentab']").click()  
new_tab = newpop.value  
  
print(new_tab.title())  
time.sleep(5)  
page.bring_to_front()  
time.sleep(5)  
new_tab.bring_to_front()  
time.sleep(5)
```

---

## Type like a human would
```Python
# Type valus in a locator just like a human would
page.locator("xpath=//input[@id='autocomplete']").press_sequentially("in",delay=2000)  
```

## Slowmo setup
```Python
# Adding slow-mo in playwright
browser = playwright.chromium.launch(headless=False,slow_mo=2000) 
```