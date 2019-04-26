import json
import requests

client_id = '1011380097020-kg5dp1d31a78q9ls1cnde880pjkh99dh.apps.googleusercontent.com'
client_secret = 'R0tgpok_IML5dk7Z02605n3t'
refresh_token = '1/fYoiqu25071WmEWTuWkHqgWmPsp5F31HNZ5auaOYx7s7-9_ik3reg0KNrW7RFLC_'
grant_type = 'refresh_token'

import shopifyAPI
shopifyAPI.
def google_get_accesstoken():
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


# Get the list of projects in Google Cloud
def get_projects_list(access_token, url):
    bearer_token = 'Bearer ' + access_token
    headers = {'Authorization': bearer_token, 'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    print('GetProjectsAPI status: ', response.status_code)
    json_response = json.loads(response.text)
    print('Get Projects Response: ', json_response)
    projects = json_response['projects']
    projects_list = [(project['name'], project['projectId']) for project in projects]
    print('Project_id: ', projects_list)


def create_project(access_token):
    url = 'https://cloudresourcemanager.googleapis.com/v1/projects'
    bearer_token = 'Bearer ' + access_token
    headers = {'Authorization': bearer_token, 'Accept': 'application/json', 'Content-Type': 'application/json'}
    request_body = {"name": "PythonSessionDemo", "projectId": "python-session-demo01"}
    # request_body = json.dumps(request_body)
    response = requests.post(url, data=request_body, headers=headers)
    print('CreateProject status: ', response.status_code)
    json_response = json.loads(response.text)
    print('CreateProject response: ', json_response)
    print('json_response: ', json_response)


def delete_project(access_token, project_id):
    delete_url = url + '/' + project_id
    # http = urllib3.PoolManager()
    bearer_token = 'Bearer ' + access_token
    headers = {'Authorization': bearer_token, 'Accept': 'application/json'}
    response = requests.delete(delete_url, headers=headers)
    print('DeleteProject status: ', response.status_code)
    json_response = json.loads(response.text)
    print('DeleteProject response: ', json_response)


if __name__ == "__main__":
    access_token = google_get_accesstoken()
    print("access_token: ", access_token)
    url = 'https://cloudresourcemanager.googleapis.com/v1/projects'
    get_projects_list(access_token, url)
    create_project(access_token)
    project_id = 'python-testing-0001'
    # delete_project(access_token, project_id)
