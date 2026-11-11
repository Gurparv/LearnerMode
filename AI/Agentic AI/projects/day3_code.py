import os
import json
from dotenv import load_dotenv
from openai import OpenAI

print("helloday2")
load_dotenv(override=True)

openai_key = os.getenv('OPENAI_API_KEY')

if openai_key:
    print("yes")
else:
    print("no")

# creating openAi client 
client = OpenAI
print("client created successfully")
