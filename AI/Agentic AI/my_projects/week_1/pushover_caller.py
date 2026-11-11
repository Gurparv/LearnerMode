from dotenv import load_dotenv
import os
import requests


def push_notification(my_message):
    load_dotenv(override=True)
    url = os.getenv('PUSHOVER_URL')
    app_token = os.getenv('PUSHOVER_APP_TOKEN')
    user_token = os.getenv('PUSHOVER_USER_TOKEN')
    requests.post(url,data =  {
                    "token": app_token,
                    "user": user_token,
                    "message": my_message
                     }
                 )


