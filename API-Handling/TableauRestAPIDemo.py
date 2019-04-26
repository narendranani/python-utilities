import json
import requests
import xml.etree.ElementTree as ET
from pprint import pprint
import os
from requests.packages.urllib3.filepost import encode_multipart_formdata
from requests.packages.urllib3.fields import RequestField

SERVER = "http://ggk-upl-tab-001:8000"
VERSION = '2.5'
xmlns = {'t': 'http://tableau.com/api'}


def sign_in(site, username, password):
    url = SERVER + "/api/{0}/auth/signin".format(VERSION)
    # Builds the request
    xml_request = ET.Element('tsRequest')
    credentials_element = ET.SubElement(xml_request, 'credentials', name=username, password=password)
    ET.SubElement(credentials_element, 'site', contentUrl=site)
    xml_request = ET.tostring(xml_request)
    print("xml_request: ", xml_request)
    server_response = requests.post(url, data=xml_request)
    print("sign_in StatusCode: ", server_response.status_code)
    print("sign_in Response: ", server_response.text)
    print("Typeof server_response: ", type(server_response.text))
    # Reads and parses the response
    parsed_response = ET.fromstring(server_response.text)
    print("parsed_response", parsed_response)
    # Gets the auth token and site ID
    token = parsed_response.find('t:credentials', namespaces=xmlns).get('token')
    site_id = parsed_response.find('.//t:site', namespaces=xmlns).get('id')
    return token, site_id


# https://onlinehelp.tableau.com/current/api/rest_api/en-us/help.htm#REST/rest_api_ref.htm#Query_Projects%3FTocPath%3DAPI%2520Reference%7C_____64
def get_projects(auth_token, site_id):
    url = SERVER + "/api/{}/sites/{}/projects".format(VERSION, site_id)
    # page_num, page_size = 1, 100   # Default paginating values
    # url = url + "?pageSize={0}&pageNumber={1}".format(page_size, page_num)
    headers = {'x-tableau-auth': auth_token}
    server_response = requests.get(url, headers=headers)
    print("get_projects StatusCode: ", server_response.status_code)
    print("get_projects Response: ", server_response.text)
    parsed_response = ET.fromstring(server_response.text)
    total_projects = parsed_response.find('t:pagination', namespaces=xmlns).get('totalAvailable')
    print("total_projects: ", total_projects)
    projects = parsed_response.findall('.//t:project', namespaces=xmlns)
    projects_dict = {project.get('name'): project.get('id') for project in projects}
    print("projects_dict: ", projects_dict)
    return projects_dict


def _make_multipart(parts):
    """
    Creates one "chunk" for a multi-part upload

    'parts' is a dictionary that provides key-value pairs of the format name: (filename, body, content_type).

    Returns the post body and the content type string.
    """
    mime_multipart_parts = []
    for name, (filename, blob, content_type) in parts.items():
        multipart_part = RequestField(name=name, data=blob, filename=filename)
        multipart_part.make_multipart(content_type=content_type)
        mime_multipart_parts.append(multipart_part)

    post_body, content_type = encode_multipart_formdata(mime_multipart_parts)
    content_type = ''.join(('multipart/mixed',) + content_type.partition(';')[1:])
    return post_body, content_type


def publish_workbook(auth_token, site_id, project_id, workbook_file_path, overwrite=True):
    publish_url = SERVER + "/api/{}/sites/{}/workbooks?overwrite={}".format(VERSION, site_id, overwrite)
    workbook_file_path = os.path.abspath(workbook_file_path)
    workbook_filename = os.path.basename(workbook_file_path)
    # Build a general request for publishing
    xml_request = ET.Element('tsRequest')
    workbook_element = ET.SubElement(xml_request, 'workbook', name=workbook_filename)
    ET.SubElement(workbook_element, 'connectionCredentials', embed='false', oAuth='false')
    ET.SubElement(workbook_element, 'project', id=project_id)
    xml_request = ET.tostring(xml_request)
    print("publish xml_request: ", xml_request)

    # Read the contents of the file to publish
    with open(workbook_file_path, 'rb') as f:
        workbook_bytes = f.read()

    # Finish building request for all-in-one method
    parts = {'request_payload': ('', xml_request, 'text/xml'),
             'tableau_workbook': (workbook_filename, workbook_bytes, 'application/octet-stream')}
    payload, content_type = _make_multipart(parts)
    headers = {'x-tableau-auth': auth_token, 'content-type': content_type}
    print("***********************Publishing workbook************************")
    server_response = requests.post(publish_url, data=payload, headers=headers)
    print("***********************Published workbook***********************")
    print("publish status_code", server_response.status_code)
    print("publish response", server_response.text)
    return server_response.status_code == 201


def update_project_name(auth_token, site_id, project_id, new_name):
    put_url = SERVER + "/api/{}/sites/{}/projects/{}".format(VERSION, site_id, project_id)
    # Build a general request for publishing
    xml_request = ET.Element('tsRequest')
    workbook_element = ET.SubElement(xml_request, 'project', parentProjectId=project_id, name=new_name, contentPermissions='ManagedByOwner')
    xml_request = ET.tostring(xml_request)
    print("update xml_request: ", xml_request)
    headers = {'x-tableau-auth': auth_token}
    server_response = requests.put(put_url, data=xml_request, headers=headers)
    print("update status_code", server_response.status_code)
    print("update response", server_response.text)


def sign_out(auth_token):
    """
    Destroys the active session and invalidates authentication token.
    """
    url = SERVER + "/api/{0}/auth/signout".format(VERSION)
    server_response = requests.post(url, headers={'x-tableau-auth': auth_token})
    print("sign_out StatusCode: ", server_response.status_code)
    print("sign_out Response: ", server_response.text)
    return


def main(site, username, password):
    auth_token, site_id = sign_in(site, username, password)
    print("token: {0}, site_id: {1} ".format(auth_token, site_id))
    projects_list = get_projects(auth_token, site_id)
    project_id = projects_list.get('Waiting For API To Upload Workbook')
    workbook_name = "PythonRestAPI.twbx"
    publish_workbook_status = publish_workbook(auth_token, site_id, project_id, workbook_name)
    print("Publish status: ", publish_workbook_status)
    project_id = projects_list.get('Just For Name Update')
    new_name = 'My Name Changed'
    # update_project_name(auth_token, site_id, project_id, new_name)
    sign_out(auth_token)


if __name__ == "__main__":
    username = "narendra.kommoju"
    password = "Hyderabad554"
    site = ""
    main(site, username, password)
