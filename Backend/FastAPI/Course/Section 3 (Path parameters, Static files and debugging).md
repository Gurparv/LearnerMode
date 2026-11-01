## Add `/rooms` route to our FastAPI application

```python title="main.py"
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
 
@app.get("/rooms", status_code=status.HTTP_200_OK)
def get_rooms():
    room1 = {
        "price": 2000,
        "rooms": "2BHK"
    }
    room2 = {
        "price":5000,
        "rooms": "5BHK"
    }
    return [room1, room2]
```

![[Pasted image 20261004130043.png]]

---

## Path parameters

Path paramters are Dynamic, named segments of the `URL/path` part of route eg `/rooms/12` now we cannot create 12 endpoints like we did above coz its not scalable. 
We wrap the path parameter in curly braces in the route string eg `/coffees.{coffee_id}`

```Python title="demo.py"
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI"};

@app.get("/rooms/{room_id}")
def get_rooms(room_id: int):
    if room_id == 10:
        return { "Message" : "Room Booked"}
    elif room_id <= 10:
        return { "Message" : "Room UnAvailable"}
    else :
        return {"Message" : "Error"}

```

```Terminal
uv run fastapi dev demo.py
```

---

## Error Responses
Now for the below code: 
If i go with Path parameter 5 eg `/rooms/5` . I will get `null`

```python title="demo.py"
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI"};

@app.get("/rooms/{room_id}")
def get_rooms(room_id: int):
    if room_id == 10:
        return { "Message" : "Room Booked"}
```

![[Pasted image 20261031191647.png]]

Note- It didnt give error. even in Chrome >> network tab as shown below

![[Pasted image 20261031191737.png]]

What we want is to properly return a error status code, more specifically a `404` saying that the requested resource is not found. We will have to manually trigger an error so that FastAPI can return a different status code and a different response body.

Solution Code-
```Python title="demo.py"
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI"};

@app.get("/rooms/{room_id}")
def get_rooms(room_id: int):
    if room_id == 10:
        return { "Message" : "Room Booked"}
    else:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Room NOT FOUND!!")

```

![[Pasted image 20261031195352.png]]

==Rewatch the video -> 23. The swagger part at the end of video==

==2 scenarios to understand - If i put string instead of number then notice what happens==
![[Pasted image 20261031200013.png]]

==Refresh your API testing fundamentals. from some courses==

---

## Route Order

FastApi tries to match routes to python function in order they are written in file that is from top to bottom

Eg
```Python title="demo.py"
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI"};

@app.get("/rooms/{room_id}")
def get_rooms(room_id: int):
    if room_id == 10:
        return { "Message" : "Room Booked"}
    else:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Room NOT FOUND!!")

@app.get("/rooms/faq")
def get_faq():
    return {"Message":"Frequently asked Questions page"}


```

![[Pasted image 20261101141211.png]]

This should have worked right.. coz we have `/rooms/faq` but it failed becoz it was confused with `/rooms/{rooms_id}`

FIX->
```Python title="demo.py"
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI"};

@app.get("/rooms/faq")
def get_faq():
    return {"Message":"Frequently asked Questions page"}

@app.get("/rooms/{room_id}")
def get_rooms(room_id: int):
    if room_id == 10:
        return { "Message" : "Room Booked"}
    else:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Room NOT FOUND!!")
```

![[Pasted image 20261101141638.png]]

---

## Serving Static Files from Endpoints

![[Pasted image 20261101150413.png]]

```Python title="demo.py"
from fastapi import FastAPI, HTTPException, status
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/assets",StaticFiles(directory="assets"), name="MyAssets")

@app.get("/")
def root():
    return {"message": "Hello from FastAPI"};

```



![[Pasted image 20261101150302.png]]

---

## Section Review for revision.