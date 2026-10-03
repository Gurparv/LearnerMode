## Basics
1. Basic Understanding of client-server architecture.
	Client - An app, mobile, CLI or any other computer/machine making request to server.
	Server - The computer which responds to the request with a payload of data.

2. FastAPI builds server-side(backend) logic.
	And FastAPI maps the request to a corresponding route.

3. Routes and Endpoints
	1. Endpoint is another word for Routes
	2. A Route(or Endpoint) is a specific path that the server recognizes and maps to a procedure(a piece of code).
	Online Store Example
	
```Text
The /product endpoint returns list of products
the /products/42 endpoint returns the details of product #42
```

4. Mental model
	- The FastAPI model maps a route to a Python function that executes when the endpoint is hit.
	- We call these functions `route handler` functions
	- The `/products` route may map to a `get_products` function.

---

## 

1. HTTP (HyperText Transfer Protocol) is a web standard, a set of rules for how `clients` and `servers` talk to each other.
2. A HTTP request includes a `route` and a `HTTP Verb` also called an `HTTP method`.
3. The `HTTP method` describes the `type` of request
4. Eg `GET, POST, DELETE`

	

