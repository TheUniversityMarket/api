from mailjet_rest import Client
import os
from uuid import uuid4
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

def send_message(to, message, subject):
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
    'Messages': [
        {
        "From": {
            "Email": "umarket064@gmail.com",
            "Name": "Paul"
        },
        "To": [
            {
            "Email": f"{to}",
            "Name": "User"
            }
        ],
        "Subject": f"{subject}",
        "TextPart": message,
        "CustomID": str(uuid4())
        }
    ]
    }
    result = mailjet.send.create(data=data)
    print (result.status_code)
    return (result.json())

if __name__ == "__main__":
    print(send_message("pauljevans927@gmail.com", "Test", "Test"))