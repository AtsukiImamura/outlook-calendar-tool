
import requests
import configparser
import json


config = configparser.ConfigParser()
config.sections()
config.read('mail.ini')


access_token = config['tokens']['access_token']

headers = {
    'Authorization': 'Bearer %s' % access_token,
    'Content-Type': 'application/json',
    'Prefer': 'outlook.timezone="Asia/Tokyo"'
}


response = requests.post(
    headers=headers,
    url="https://graph.microsoft.com/v1.0/me/events",
    data=json.dumps({
        "subject": "Let's go for lunch",
        "body": {
            "contentType": "HTML",
            "content": "Does late morning work for you?"
        },
        "start": {
            "dateTime": "2020-07-30T12:00:00",
            "timeZone": "Asia/Tokyo"
        },
        "end": {
            "dateTime": "2020-07-30T14:00:00",
            "timeZone": "Asia/Tokyo"
        },
        "location": {
            "displayName": "Harry's Bar"
        },
    })
)
if response.status_code != 201:
    print(response.json())
else:
    print(response.text)
