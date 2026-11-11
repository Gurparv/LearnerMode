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
