# Connecting to Google API

from dotenv import load_dotenv
from openai import OpenAI
import os
from pydantic import BaseModel


# Output response format needed.
class Evaluation(BaseModel):
    feedback: str
    score: int
    is_acceptable: bool 

# Making calls to Gemini
def call_gemini(query)-> Evaluation:
    print("########## Calling Gemini #########")
    load_dotenv(override=True)
    key = os.getenv('GEMINI_API_KEY')
    google_client = OpenAI(
        api_key = key,
        base_url = 'https://generativelanguage.googleapis.com/v1beta/openai/'
        )
    google_response = google_client.beta.chat.completions.parse(
        model="gemini-2.0-flash",
        messages = query,
        response_format = Evaluation
        )
    res = google_response.choices[0].message.parsed
    #print(res.is_acceptable)
    print("######Gemini Response###########")
    print(res)
    print("################################")

    return res
