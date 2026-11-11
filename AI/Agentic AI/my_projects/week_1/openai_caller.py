# Connecting to OpenAI

from dotenv import load_dotenv
from openai import OpenAI
from pushover_caller import push_notification
import json

record_user_details_json = {
        "name":"record_user_details",
        "description":"Use this tool to record that a user is interested in being in touch and provided an email address",
        "parameters":{
            "type":"object",
            "properties":{
                "email": {
                    "type":"string",
                    "description": "The email address of the user"},
                "name":{
                    "type":"string",
                    "description": "The user's name if they provided it."},
                "notes":{
                    "type":"string",
                    "description":"Any additional information about the conversation that's worth recording to give context"}
            },
            "required":["email"],
            "additonalProperties":False
            }
    }

tools = [{"type":"function","function":record_user_details_json}]


def call_openai(query, has_tool_run=False):
    print("######### Calling OPENAI ############")
    load_dotenv(override=True)
    client = OpenAI()
    #print(tools)
    if not has_tool_run:
        response = client.chat.completions.create(
            model = "gpt-4.1",
            messages = query,
            max_completion_tokens = 300,
            tools = tools
            )
    else:
        response = client.chat.completions.create(
            model = "gpt-4.1",
            messages = query,
            max_completion_tokens = 300
            )
    print("######OpenAI Response###########")
    print(response)
    print("################################")
    result = response.choices[0].message
    return result



      
      
