# import requests
# from django.shortcuts import render

# # ---- SD-WAN Login and Data Retrieval ----
# def get_sdwan_devices(vmanage_host, username, password):
#     # Base URL
#     base_url = f"https://{vmanage_host}"

#     # Disable SSL warnings for demo (not recommended for production)
#     requests.packages.urllib3.disable_warnings()

#     # Login endpoint
#     login_url = f"{base_url}/j_security_check"
#     payload = {
#         'j_username': username,
#         'j_password': password
#     }

#     session = requests.session()
#     login_response = session.post(url=login_url, data=payload, verify=False)

#     if login_response.status_code != 200 or 'html' in login_response.text.lower():
#         raise Exception("Login failed! Check vManage credentials.")

#     # Get device list
#     devices_url = f"{base_url}/dataservice/device"
#     response = session.get(url=devices_url, verify=False)
#     response.raise_for_status()

#     data = response.json()
#     print(data)
#     return data.get('data', [])

    

# # ---- Django View ----
# def devices_view(request):
#     vmanage_host = "10.10.20.90"
#     username = "admin"
#     password = "C1sco12345"

#     try:
#         devices = get_sdwan_devices(vmanage_host, username, password)
#     except Exception as e:
#         return render(request, 'dashboard/error.html', {'error': str(e)})

#     return render(request, 'dashboard/devices.html', {'devices': devices})
    
######################################## 16th MAy  ############################
# import requests
# import json
# from django.shortcuts import render
# vmanage_host = "https://sandbox-sdwan-2.cisco.com"
# username = "devnetuser"
# password = "RG!_Yw919_83"

# def get_auth_token():
#     url = f"{vmanage_host}/j_security_check"
#     data = {
#         'j_username': username,
#         'j_password': password
#     }
#     session = requests.session()
#     login_response = session.post(url, data=data, verify=False)
#     # print(login_response)
#     return session

# def get_devices_list():
#     session = get_auth_token()
#     url = f"{vmanage_host}/dataservice/device"
#     response = session.get(url, verify=False)
#     data = response.json()
#     print(data)
#     return data.get('data', [])
# def devices_view(request):
#     try:
#         devices = get_devices_list()
#         # print(devices)
#     except Exception as e:
#         return render(request, 'dashboard/error.html', {'error': str(e)})

#     return render(request, 'dashboard/devices.html', {'devices': devices})
# if __name__== "__main__":
#     devices = get_devices_list()
#     print(json.dumps(devices, indent=4))

######################################## 16th MAy test 2 ############################
from django.shortcuts import render
import requests
import urllib3

urllib3.disable_warnings()

VMANAGE_HOST = "https://sandbox-sdwan-2.cisco.com"
USERNAME = "devnetuser"
PASSWORD = "RG!_Yw919_83"


def get_jsessionid():
    url = f"{VMANAGE_HOST}/j_security_check"

    payload = {
        'j_username': USERNAME,
        'j_password': PASSWORD
    }

    session = requests.session()

    response = session.post(
        url,
        data=payload,
        verify=False
    )

    if response.status_code != 200:
        return None

    return session


def devices_view(request):

    session = get_jsessionid()

    if not session:
        return render(request, 'devices.html', {
            'error': 'Login Failed'
        })

    url = f"{VMANAGE_HOST}/dataservice/device"

    response = session.get(
        url,
        verify=False
    )

    data = response.json()

    devices = []

    for d in data['data']:
        devices.append({
            'host_name': d.get('host-name'),
            'device_id': d.get('deviceId'),
            'system_ip': d.get('system-ip'),
            'site_id': d.get('site-id'),
            'device_type': d.get('device-type'),
            'status': d.get('reachability'),
        })
    
    return render(request, 'dashboard/devices.html', {'devices': devices})
    