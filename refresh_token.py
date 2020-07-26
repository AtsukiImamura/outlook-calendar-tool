
from requests import post as http_post
import configparser

import configparser


config = configparser.ConfigParser()
config.sections()
config.read('mail.ini')


refresh_token = config['tokens']['refresh_token']

data = {
    'grant_type': 'refresh_token',
    'client_id': '23c140e4-9ba0-4b39-98d6-ac624ae17fa3',
    'redirect_uri': 'https://localhost:8080/app',
    'scope': 'user.read calendars.read offline_access',
    'state': '1234',
    'refresh_token': refresh_token
}
response = http_post(
    'https://login.microsoftonline.com/common/oauth2/v2.0/token',
    data=data,
)

if response.status_code == 200:
    res_data = response.json()

    print(res_data)

    config = configparser.ConfigParser()
    config.sections()
    config.read('mail.ini')

    config['tokens'] = {
        'access_token': res_data['access_token'],
        'refresh_token': res_data['refresh_token'],
    }

    with open('mail.ini', 'w') as configfile:
        config.write(configfile)
else:
    print(response.text)
