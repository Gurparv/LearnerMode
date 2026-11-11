import os
from dotenv import load_dotenv
from openai import OpenAI
from PyPDF2 import PdfReader
import gradio as gr
from pydantic import BaseModel

load_dotenv(override=True)

openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key:
    print("yes")
else:
    print("No")

# creating OpenAI client reference
openai = OpenAI()
print("OpenAI client created successfully")


# Reading the pdf file.
reader = PdfReader("me/my_linkedin_profile.pdf")
linkedin = ""
for page in reader.pages:
    text =  page.extract_text()
    if text:
        linkedin += text

print(linkedin)
print()

# Opening and Reading summary.txt file
with open("me/summary.txt","r",encoding="utf-8") as f:
    summary = f.read()

print(summary)

name = "GurparvSingh"

system_prompt = f"You are acting as {name}. You are answering questions on {name}'s website, \
        particularly questions related to {name}'s career, background, skills and experience.\
        Your responsibility is to represent {name} for interactions on the website as faithfully as possible.\
        You are given a summary of {name} background and LinkedIn profile which you can to asnwer questions.\
        Be professional and engaging, as if talking to a potential client or future employer who came across the website.\
        If you don't know the answer, say so."

system_prompt += f"\n\n## Summar: \n {summary}\n\n## LinkedIn Profile:\n{linkedin}\n\n"
system_prompt += f"With this context, please chat with the user, always staying in character as {name}."

print(system_prompt)

def chat(message, history):
    custom_message = [{"role":"system", "content": system_prompt}] + \
            history + \
            [{"role":"user","content":message}]
    response = openai.chat.completions.create(model="gpt-4o-mini",messages=custom_message,max_tokens=100)
    print(f"Custom message = {custom_message}")
    return response.choices[0].message.content

gr.ChatInterface(chat,type="messages").launch()

##############################################################
