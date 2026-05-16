import requests
import json

vmanage_host = "https://10.10.20.90"
username = "admin"
password = "C1sco12345"

def get_auth_token():
    url = f"{vmanage_host}/j_security_check"
    data = {
        'j_username': username,
        'j_password': password
    }
    session = requests.session()
    login_response = session.post(url, data=data, verify=False)
    # print(login_response)
    return session

def get_devices_list():
    session = get_auth_token()
    url = f"{vmanage_host}/dataservice/device"
    response = session.get(url, verify=False)
    data = response.json()
    print(data)
    return data.get('data', [])
if __name__== "__main__":
    devices = get_devices_list()
    print(json.dumps(devices, indent=4))