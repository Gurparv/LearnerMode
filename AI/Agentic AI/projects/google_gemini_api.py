import os
from dotenv import load_dotenv
from openai import OpenAI
from PyPDF2 import PdfReader
import gradio as gr
from pydantic import BaseModel

load_dotenv(override=True)

client = os.getenv('GOOGLE_API_KEY')

if client:
    print("yes")
else:
    print("No")

# creating OpenAI client reference
openai = OpenAI()
print("OpenAI client created successfully")
gemini = OpenAI(
        api_key = os.getenv("GOOGLE_API_KEY"),
        base_url = "https://generativelanguage.googleapis.com/v1beta/openai/")

model_name = "gemini-2.0-flash"

message = [{"role":"user","content":"What is Africa?"}]

response = gemini.chat.completions.create(model = model_name, messages = message,max_tokens=10)
print(response)
print(response.choices[0].message.content)
print()

class Evaluation(BaseModel):
    is_acceptable: bool
    feedback: str

response = gemini.beta.chat.completions.parse(model="gemini-2.0-flash",messages=message, response_format=Evaluation)
print(response)
print(response.choices[0].message.parsed)
