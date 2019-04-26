import json
import requests
from pprint import pprint

import requests
import base64
from requests.auth import HTTPBasicAuth

def basic_authentication():
    url = 'https://www.httpwatch.com'
    username = 'httpwatch'
    password = 'httpwatch'
    usr_pass = username + ':' + password
    auth_token = base64.b64encode(str.encode(usr_pass))
    print("auth_token: ", bytes.decode(auth_token))
    basic_token = 'Basic ' + bytes.decode(auth_token)
    print("basic_token: ", basic_token)
    headers = {'authorization': basic_token, 'Accept': 'text/plain'}
    
    response = requests.get(url, auth=HTTPBasicAuth('user', 'pass'))
##    response = requests.get(url, headers=headers)
    print("response code aS: ", response.status_code)


def basic_authentication_2():
    url = 'https://auth-demo.aerobatic.io/protected-custom'
    username = 'aerobatic'
    password = 'aerobatic'
    usr_pass = username + ':' + password
    auth_token = base64.b64encode(str.encode(usr_pass))
    print("auth_token: ", bytes.decode(auth_token))
    basic_token = 'Basic ' + bytes.decode(auth_token)
    print("basic_token: ", basic_token)
    headers = {'authorization': 'Basic YWVyb2JhdGljOmFlcm9iYXRpYw==', 'Accept': 'text/plain'}
    response = requests.get(url, headers=headers)
    print("response code: ", response.status_code)


def google_get_accesstoken():
    client_id = '1011380097020-kg5dp1d31a78q9ls1cnde880pjkh99dh.apps.googleusercontent.com'
    client_secret = 'R0tgpok_IML5dk7Z02605n3t'
    refresh_token = '1/fYoiqu25071WmEWTuWkHqgWmPsp5F31HNZ5auaOYx7s7-9_ik3reg0KNrW7RFLC_'
    grant_type = 'refresh_token'
    url = 'https://accounts.google.com/o/oauth2/token'
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    request_body = {"client_id": client_id,
                    "client_secret": client_secret,
                    "refresh_token": refresh_token,
                    "grant_type": grant_type}
    response = requests.post(url, data=request_body, headers=headers)
    response_json = json.loads(response.text)
    print("response_json: ", response_json)
    return response_json['access_token']


if __name__ == '__main__':
    basic_authentication()
    # access_token = google_get_accesstoken()
    # print("access_token: ", access_token)
