import requests
import configparser


config = configparser.ConfigParser()
config.sections()
config.read('mail.ini')


access_token = config['tokens']['access_token']

headers = {
    'Authorization': 'Bearer %s' % access_token,
    'Prefer': 'outlook.timezone="Asia/Tokyo", outlook.body-content-type="text"'
}

params = {}

response = requests.get(
    url="https://graph.microsoft.com/v1.0/me/events",
    params=params,
    headers=headers,
)
if response.status_code != 200:
    print(response.json())
else:
    print(response.text)
