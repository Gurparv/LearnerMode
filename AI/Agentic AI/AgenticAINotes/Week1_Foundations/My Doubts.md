1. How to connect to OpenAI()
You can pass the OpenAI Key in directly in function OpenAI() or
You can use dotenv and load the Api key using it to load it to the environment.
```python
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)

client = OpenAI()

response = client.responses.create(
  model="gpt-4.1",
  input="Tell me a three sentence bedtime story about a unicorn."
)

print(response)
```


2. How to read PDF using PyPDF2 python library?
https://pypi.org/project/PyPDF2/

3.  Python Gradio library basics
```python
import gradio as gr
import random

def greet(message, history):
    print(message)
    print("*************")
    print(history)
    return random.choice(["yes", "no"])

gr.ChatInterface(
        fn = greet,
        type = "messages").launch()

```

```powershell
(.venv) GURPARV-PC ->> python .\test_gradio.py
* Running on local URL:  http://127.0.0.1:7860
* To create a public link, set `share=True` in `launch()`.
hi
*************
[]
whats history
*************
[{'role': 'user', 'metadata': None, 'content': 'hi', 'options': None}, {'role': 'assistant', 'metadata': None, 'content': 'no', 'options': None}]
again plz
*************
[{'role': 'user', 'metadata': None, 'content': 'hi', 'options': None}, {'role': 'assistant', 'metadata': None, 'content': 'no', 'options': None}, {'role': 'user', 'metadata': None, 'content': 'whats history', 'options': None}, {'role': 'assistant', 'metadata': None, 'content': 'no', 'options': None}]
what else
*************
```

4. Sharing your Gradio project to public using Hugging Spaces
https://www.gradio.app/guides/sharing-your-app

- Have your file named app.py or app.
- Create a Space on hugging face.
- Put the code their 'upload it'
- and wait for it to run.
- and go run it.
```python
import gradio as gr
import random

def greet(message, history):
    print(message)
    print("*************")
    print(history)
    return random.choice(["yes", "no"])

gr.ChatInterface(
        fn = greet,
        type = "messages").launch()

```

5. Pydantic

```python
from pydantic import BaseModel

class Evaluation(BaseModel):
    is_acceptable : bool

data = 123

res = Evaluation(is_acceptable = 11)
print(res)
```

==My Prompt==
can you please explain to me pydantic python library , the practical part and its use-case only with a simple example.


Absolutely! Here's a **practical, simple explanation of Pydantic** in Python:

---

## 🧰 What is Pydantic?

**Pydantic** is a library that lets you define **data models** using Python classes — and it automatically:

- **Validates** data
    
- **Parses** input (e.g. from JSON or dicts)
    
- Ensures data types are **correct**
    
- Converts raw/untrusted data into structured Python objects
    

---

## 🔧 When is it used (Real Use Case)?

- **APIs (like FastAPI)**: Validate and parse user input (e.g. request body)
    
- **Config loading**: Parse `.json` or `.env` files
    
- **Structured tools for LLMs**: Define valid input/output formats
    

---

## ✅ Practical Example: User Sign-Up Form

```python
from pydantic import BaseModel, EmailStr

# Define your data schema
class UserSignup(BaseModel):
    username: str
    email: EmailStr
    age: int

# Incoming data (e.g. from a web form or JSON)
raw_data = {
    "username": "gurparv",
    "email": "gurparv@example.com",
    "age": "30"  # Note: string instead of int
}

# Parse and validate
user = UserSignup(**raw_data)

print(user)
print(user.age)  # 👉 auto-converted to int
```

### 🧠 Output:

```python
username='gurparv' email='gurparv@example.com' age=30
30
```

---

## 💥 If validation fails:

```python
bad_data = {
    "username": "gp",
    "email": "not-an-email",
    "age": "abc"
}

user = UserSignup(**bad_data)
```

✅ Will raise a **clear error** with which field failed and why.

---

## 🧠 Summary

|Feature|Benefit|
|---|---|
|✅ Validation|Ensures data is safe/correct|
|🔄 Parsing|Converts types (str → int)|
|🔒 Structured|You get strongly-typed objects|
|⚡ Fast|Built on `dataclasses` + `Cython`|

---

Would you like the same example shown with **FastAPI** or used as an LLM tool schema?
6. Getting 'Structed Response' from LLM in structure you define
https://ai.google.dev/gemini-api/docs/openai#structured-output

---
---

# Day 5

1. PushOver application setup
```python 
from dotenv import load_dotenv
from openai import OpenAI
import json
import os
import requests
from PyPDF2 import PdfReader
import gradio as gr

load_dotenv(override=True)
openai= OpenAI()

# For pushover
pushover_user = os.getenv("PUSHOVER_USER")
pushover_token = os.getenv("PUSHOVER_TOKEN")
pushover_url = "https://api.pushover.net/1/messages.json"

def push(message):
    print(f"Push : {message}")
    payload = {"user": pushover_user, "token":pushover_token,"message":message}
    requests.post(pushover_url, data=payload)

push("Hey There!")
```

2. Converting a 'python function' into a 'tool'
==My Prompt==
tell me if my understanding of tool is correct.
I tell LLM via json schema that there is a tool at its disposal that it can request for us to run with the parameter we want. and we can run it and then send output to you again.?
concise answer 

✅ Yes, exactly.
You tell the LLM (via JSON schema) that a tool exists. The LLM can **request** to use it with specific parameters.  
**You run** the tool yourself, then send the result back to the LLM so it can continue the conversation.

==My prompt==
so the parameters it sends to us .. we can say that it parsed it according to the schema we provided?
concise answer

✅ Yes. The LLM parses the parameters **based on the schema you provided** and sends them to you in a structured format (usually JSON).


## What does "converting a Python function into a tool" mean?

This depends on the context.

### ✅ In general, it means:

> **Making a Python function callable outside of your code**, often as a CLI command, API endpoint, plugin, or component in a larger system (like LangChain, OpenAI function calling, or shell tool).


Got it! You’re asking how to **convert a Python function into a tool that an LLM (like OpenAI's GPT or LangChain) can call**, using **function calling/tool use format**.

---

## ✅ LLM Tool Basics

When you "convert" a function into a **tool** in the LLM world (like OpenAI or LangChain), you:

1. **Define the function** in Python.
2. **Describe it in a structured way** (JSON schema style).
3. Register it with the LLM (OpenAI, LangChain, etc.).
    

---

## ⚙️ Example: Convert a Python Weather Function into an LLM Tool

### 💡 Step 1: Write a simple Python function

```python
def get_weather(city: str) -> str:
    """Returns fake weather info for demo purposes."""
    return f"The weather in {city} is sunny and 27°C."
```

---

### 💡 Step 2: Describe the function as a tool (OpenAI-compatible format)

```python
get_weather_tool = {
    "name": "get_weather",
    "description": "Get the current weather in a given city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The name of the city to get weather for"
            }
        },
        "required": ["city"]
    }
}
```

---

### 💡 Step 3: Use it with OpenAI GPT (pseudo-code, working structure)

```python
from openai import OpenAI

# Step 1: Send tool definition with your prompt
response = client.chat.completions.create(
    model="gpt-4-0613",
    messages=[{"role": "user", "content": "What's the weather in Delhi?"}],
    tools=[get_weather_tool],
    tool_choice="auto",
)

# Step 2: Check if model called your tool
tool_call = response.choices[0].message.tool_calls[0]
if tool_call.function.name == "get_weather":
    city = tool_call.function.arguments["city"]
    result = get_weather(city)  # call your actual function

    # Step 3: Send function result back to GPT
    final_response = client.chat.completions.create(
        model="gpt-4-0613",
        messages=[
            {"role": "user", "content": "What's the weather in Delhi?"},
            response.choices[0].message,  # Tool call msg
            {"role": "tool", "name": "get_weather", "content": result},
        ],
    )

    print(final_response.choices[0].message.content)
```

---

## 🔁 Summary

|Step|What You Do|Purpose|
|---|---|---|
|1|Write a function|Your logic (e.g., get_weather)|
|2|Define a tool schema (JSON-style)|Tells LLM how to call the function|
|3|Register it in a tool-calling API|OpenAI/LangChain triggers it when needed|
|4|Run the function, send output back|LLM continues the conversation|

---

Would you like this same setup in **LangChain**, **FastAPI as a backend tool**, or a **multi-tool demo** next?

==OpenAI Tools guide== = https://platform.openai.com/docs/guides/tools
==Python Globals()== -> https://www.codecademy.com/resources/docs/python/built-in-functions/globals


## Example 2 - Tool call

## ✅ Here's the Correct Flow with Function Calling

```python
from openai import OpenAI
import json

client = OpenAI()

# Step 1: Define your tool schema
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current temperature for a given location.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City and country e.g. Bogotá, Colombia"
                }
            },
            "required": ["location"]
        }
    }
}]

# Step 2: Send user prompt and tool schema to GPT
response = client.chat.completions.create(
    model="gpt-4-0613",  # or gpt-4.1 (if using newer version)
    messages=[
        {"role": "user", "content": "What is the weather in Paris today?"}
    ],
    tools=tools,
    tool_choice="auto"
)

# Step 3: Get the tool call from GPT (if any)
tool_call = response.choices[0].message.tool_calls[0]
function_name = tool_call.function.name
arguments = json.loads(tool_call.function.arguments)

# Step 4: Call your actual Python function
def get_weather(location: str):
    # Dummy version, just for testing
    return f"The weather in {location} is sunny and 25°C."

tool_output = get_weather(arguments["location"])

# Step 5: Send function result back to GPT
second_response = client.chat.completions.create(
    model="gpt-4-0613",
    messages=[
        {"role": "user", "content": "What is the weather in Paris today?"},
        response.choices[0].message,
        {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "name": function_name,
            "content": tool_output
        }
    ]
)

# Final GPT response including tool result
print(second_response.choices[0].message.content)
```

---

## 🔍 Summary

|Step|What Happens|
|---|---|
|1|You tell GPT what tool is available (via schema)|
|2|GPT may respond with an intent to call a tool|
|3|YOU (the developer) receive the tool call + arguments|
|4|YOU call the actual Python function and send the result back|
|5|GPT continues the conversation with that tool output|

---

## 🧠 Key Insight

> **LLMs only "suggest" calling tools — they don’t run your Python code themselves. You must handle that part.**

---

Let me know if you want this adapted for a real API like OpenWeatherMap or wrapped with FastAPI/LangChain for full integration.