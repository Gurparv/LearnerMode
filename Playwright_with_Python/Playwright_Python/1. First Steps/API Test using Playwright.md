The simplest way to use playwright for API testing
```python
from plawright.sync_api import Playwright

def test_api_demo(playwright:Playwright):
	api_context = playwright.request.new_context(base_url = "url")
	res = api_context.get("<endpoint>")
	print(res.status)
	print(res.json())

```

## How to add network listener in playwright
```python
from plawright.sync_api import Page
# in this test case basically we are opening a page and then for 1 api we are add a listener and then sending some payload to it. to check response on the page. 

some_payload = 'some fake response'

def intercept_response(route):
	route.fulfill(
		json = some_payload
	)

def test_api_demo(page: Page)
	# intercept_response is a handler here..
	page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
```


# How to add request intercepter in playwright
```python
from plawright.sync_api import Playwright
some_payload = 'some fake response'

def intercept_response(route):
	route.continue_(url="[new_url](https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=1782913782913")

def test_api_demo(page: Page)
	# intercept_response is a handler here..
	page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_response)
```

# inject and save cookies into browser at run time at playwright.
```python
from plawright.sync_api import Page
get_Token = 'asksjdfkldjsdklfsd'

def test_api(page:Page):
# injecting javascript to add token to page, context
	page.add_init_script(
		f""" 
			localStorage.getItem('token',{getToken})
		"""
	)
