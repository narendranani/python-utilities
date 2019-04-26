import requests
import json

BASE_URL = ""
VERSION = 'te'
HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}


def send_request(method, url, request_body={}, headers={}):
    headers.update(HEADERS)
    request_body = json.dumps(request_body)
    return requests.request(method, url, data=request_body, headers=headers).json()


def sign_in(username, pwd, content_url=""):
    request_body = {
        "credentials": {
            "name": username,
            "password": pwd,
            "site": {
                "contentUrl": content_url
            }
        }
    }
    url = BASE_URL + f'/api/{VERSION}/auth/signin'
    response = send_request('Post', url, request_body)
    return response["credentials"]["token"], response["credentials"]["site"]["id"]


def get_workbooks(token, site_id, workbook_name):
    url = BASE_URL + f'/api/{VERSION}/sites/{site_id}/workbooks'
    headers = {"X-Tableau-Auth": token}
    response = send_request('Get', url, headers=headers)




def get_workbook_connection_id(workbook_id):
    pass


def sign_out():
    pass
