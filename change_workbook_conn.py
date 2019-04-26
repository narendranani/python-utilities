import tableau_utilities as tu


def gen_csv_with_wb_details(server_name, username, password, site_name, project_name=[]):
    tu.BASE_URL = f'http://{server_name}'
    tu.VERSION = 2.5
    token, site_id = tu.sign_in(username, password, site_name)
    print(f"token: {token}")
    # tu.sign_in()


if __name__ == '__main__':
    server_details = {"server_name": "10.211.0.108:8000",
                      "username": "admin",
                      "password": "Hyderabad007",
                      "site_name": "",
                      "project_name": []
                      }
    gen_csv_with_wb_details(**server_details)
