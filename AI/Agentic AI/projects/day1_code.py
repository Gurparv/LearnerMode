from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv(override=True)

openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key:
    print("yes")
else:
    print("No")

# creating OpenAI client reference
openai_python_client = OpenAI()
print("OpenAI client created successfully")

# creating a list of messages in the OpenAI format
message = [
    {"role": "user",
    "content": "Who founded OpenAI?, short response"}
    ]

response = openai_python_client.chat.completions.create(
        model = "gpt-4.1",
        messages = message
        )
print(response)
print(response.choices[0].message.content)
print("////////////////////////////////////////")

'''# Excercise for practice
Ask LLM to suggest a business area that might be worth exploring for an Agentic AI opportunity.
Then ask LLM to present a pain point in that industry - something challenging that might be ripe for an Agentic solution.
Finally have 3rd LLM call propose the Agentic AI solution'''

question1 = [{"role":"user","content":"Act as a veteran business analyst and market analyzer - suggest 1 business area that might be worth exploring for Agentic AI opportunity"}]
print(question1)
print("\n")
response = openai_python_client.chat.completions.create(model = "gpt-4.1", messages = question1, max_tokens = 100)
res = response.choices[0].message.content
print(res+"\n")

question2 = [{"role":"user", "content": res + " \n Now for this opportunity, present a pain point in that industry - something challenging that might be ripe for an Agentic solution."}]
print(question2)
print("\n")

response = openai_python_client.chat.completions.create(model = "gpt-4.1", messages = question2, max_tokens = 100)
res = response.choices[0].message.content
print(res)

question3 = [{"role":"user","content": res+"\n.Now propose a Agentic AI solution for this"}]
print(question3)
print("\n")

response = openai_python_client.chat.completions.create(model="gpt-4.1",messages=question3, max_tokens = 100)
res = response.choices[0].message.content
print(res)

