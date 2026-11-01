
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

---

At this point this `demo.py` python code is creating a FastAPI application which supports a single route `/`

```python title="main.py"
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "hello from fastAPI"};

```

---

FastAPI server has 2 run modes -
1. Development
```terminal
fastapi dev
```
2. Production
```terminal
fastapi run
```

---

## Swagger Docs
`/docs` will open the swagger docs for your application.
```
localhost:8000/docs
```
   
   ![[Pasted image 20261004112453.png]]

---

## Curl command
```terminal
curl -X 'GET' \ 'http://127.0.0.1:8000/' \ -H 'accept: */*'
```

--- 

## Declare route status code
```python title="main.py"
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Yooooo!"};
```

OR

```python title="main.py"
from fastapi import FastAPI, status

app = FastAPI()

@app.get("/", status_code = status.HTTP_200_OK)
def root():
    return {"message": "Hello from fastAPI application!"};
```

Manually raise error 
```python title="main.py"
from fastapi import FastAPI, status

app = FastAPI()

@app.get("/", status_code = status.HTTP_200_OK)
def root():
    raise ValueError();
    return {"message": "Hello from fastAPI application!"};
```

---

## Customizing Swagger Docs

```Python title="main.py"
from fastapi import FastAPI, status

app = FastAPI(
        title="Gurparv Software services",
        description="High reliable highly performant software for your biz",
        version="1.0.0",
        contact={"name": "Gurparv Enterprise",
                 "phone":"901-878-1738",
                 "email":"bestsoftware@gmail.com"}
         )

@app.get("/", status_code = status.HTTP_200_OK)
def root():
    return {"message": "Hello from fastAPI application!"};
 
```

![[Pasted image 20261004121623.png]]

