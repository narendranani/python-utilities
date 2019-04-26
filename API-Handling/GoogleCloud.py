import urllib3
import json

client_id = '1011380097020-kg5dp1d31a78q9ls1cnde880pjkh99dh.apps.googleusercontent.com'
client_secret = 'R0tgpok_IML5dk7Z02605n3t'
refresh_token = '1/fYoiqu25071WmEWTuWkHqgWmPsp5F31HNZ5auaOYx7s7-9_ik3reg0KNrW7RFLC_'
grant_type = 'refresh_token'


def google_get_accesstoken():
    http = urllib3.PoolManager()
    url = 'https://accounts.google.com/o/oauth2/token'
    response = http.request('POST', url)
    print('status: ', response.status)
    access_token = response.data
    print('Accesstoken: ', response.data)
    return access_token


access_token = google_get_accesstoken()
http = urllib3.PoolManager()


# Get the list of projects in Google Cloud
# def get_projects_list(access_token, url):
#     urllib3.disable_warnings()
#     bearer_token = 'Bearer ' + access_token
#     headers = {'Authorization': bearer_token, 'Accept': 'application/json'}
#     response = http.request('GET', url, headers=headers)
#     print('ProjectsAPI status: ', response.status)
#     # print('PorjectsAPI Response: ', response.data) #Response will be in bytes
#     json_response = json.loads(response.data)
#     print('json_response: ', json_response)
#     projects = json_response['projects']
#     print('Projects: ', projects)
#     print('Project_id: ', projects[0]['projectId'])
#
#
# url = 'https://cloudresourcemanager.googleapis.com/v1/projects'
# get_projects_list(access_token, url)
#
#
# def create_project(access_token):
#     urllib3.disable_warnings()
#     # http = urllib3.PoolManager()
#     bearer_token = 'Bearer ' + access_token
#     headers = {'Authorization': bearer_token, 'Accept': 'application/json'}
#     data = {'projectId': 'pythonsessiondemo0901'}
#     # data = urllib3.request.urlencode(data)
#     response = http.request('POST', url, headers=headers, body=json.dumps(data))
#     print('CreateProject status: ', response.status)
#     # print('CreateProject Body: ', response.data)
#     json_response = json.loads(response.data)
#     print('json_response: ', json_response)
#
#
# create_project(access_token)
#
#
# def delete_project(access_token, project_id):
#     urllib3.disable_warnings()
#     delete_url = url + '/' + project_id
#     # http = urllib3.PoolManager()
#     bearer_token = 'Bearer ' + access_token
#     headers = {'Authorization': bearer_token, 'Accept': 'application/json'}
#     response = http.request('DELETE', delete_url, headers=headers)
#     print('DeleteProject status: ', response.status)
#     # print('CreateProject Body: ', response.data)
#     json_response = json.loads(response.data)
#     print('json_response: ', json_response)
#
#
# project_id = 'pythonsessiondemo0901'
# delete_project(access_token, project_id)
#
#
# # For list of scopes or generating refresh token,
# # visit https://cloud.google.com/bigquery/docs/reference/rest/v2/projects/list
#
# print("Number of pools: ", len(http.pools))
#
# def basic_authentication():
#     # Basic Authentication
#     from http.client import HTTPSConnection
#     from base64 import b64encode
#
#     # This sets up the https connection
#     http = urllib3.PoolManager()
#     # we need to base 64 encode it
#     # and then decode it to acsii as python 3 stores it as a byte string
#     userAndPass = b64encode(b"username:password").decode("ascii")
#     headers = {'Authorization': 'Basic %s' % userAndPass}
#     # then connect
#     response = http.request('GET', '/', headers=headers)
#     # get the response back
#     print('status: ', response.status)
#     print('BasicAuth: ', response.data)


# # by using http.client
# import http.client
#
# # Get the list of projects in Google Cloud
# def get_projects_list(access_token):
#     bearer_token = 'Bearer ' + access_token
#     connection = http.client.HTTPSConnection(r'cloudresourcemanager.googleapis.com')
#     headers = {'Authorization': bearer_token, 'Accept': 'application/json'}
#     connection.request('GET', '/v1/projects', headers=headers)
#     response = connection.getresponse()
#     print(response.read().decode())
#
#
#
# get_projects_list(access_token)

