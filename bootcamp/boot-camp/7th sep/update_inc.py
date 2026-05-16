import os
import json
import requests
import subprocess
from netmiko import ConnectHandler


ssh_username = 'cisco'
ssh_password = 'cisco'
username = 'admin'
password = 'MSa94!rmZ!xF'


def ping_device(ip_address):
    """ 
    Ping Device and share output with responce.
    Args: ip_address (str) 
    Return: Reachability information (str)
    """
    try:
        # The '-c 1' option sends a single ping packet on Linux/MacOS. For Windows, use '-n 1'.
        ping_output = subprocess.run(['ping', '-c', '1', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Check if the ping command was successful
        if ping_output.returncode == 0:
            return f"{ip_address} is reachable."
        else:
            return f"{ip_address} is not reachable."
    
    except Exception as e:
        return f"An error occurred: {str(e)}"
################################################### Connect to Device #########################################################
def connect_device(ip_address):
    net_connect = ConnectHandler(device_type='cisco_ios',host=ip_address,username=ssh_username,password= ssh_password)
    device_output = net_connect.send_command("show ip bgp su | b Nei")
    device_uptime = net_connect.send_command("show ver | in uptime")
    device_output1 = f"Device BGP status \n{device_output}\n\n Device uptime \n{device_uptime} "

    if device_output:
        return device_output1
    net_connect.disconnect()
###########################################################################################################################
instance_url = "https://dev254366.service-now.com/"

# API endpoint for updating an incident (replace 'incident_sys_id' with the actual sys_id of the incident)
incident_sys_id = "db41229883109210c82e9b80deaad30e"
url = f"{instance_url}/api/now/table/incident/{incident_sys_id}"
# Headers for the request
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Incident Information
response = requests.get(url, auth=(username, password), headers=headers)
# print (response.json())

ip_address = response.json()['result']['short_description'].split('|')[0].split()[1]
issue = response.json()['result']['short_description'].split('|')[1].split()[2]
state = response.json()['result']['incident_state']
# Check if the request was successful
if response.status_code == 200:
    # print("Incident Information:", response.json())
    if issue == "Down":
        if "not reachable" in ping_device(ip_address):
            data = {
            "work_notes": f"Device Ping status :\n{ping_device(ip_address)}"
            }
            json_data = json.dumps(data)
            url = f"{instance_url}/api/now/table/incident/{incident_sys_id}"
            update_response = requests.patch(url, auth=(username, password), headers=headers, data=json_data)
            if update_response.status_code == 200:
                print("Work notes updated successfully.")
            else:
                print(f"Failed to update work notes. Status code: {update_response.status_code}")
                print("Response:", update_response.json())
        else:
            data = {
            "work_notes": f"Device Ping status :\n{ping_device(ip_address)}\n\n {connect_device(ip_address)}"
            }
            json_data = json.dumps(data)
            url = f"{instance_url}/api/now/table/incident/{incident_sys_id}"
            update_response = requests.patch(url, auth=(username, password), headers=headers, data=json_data)
            if update_response.status_code == 200:
                print("Work notes updated successfully proceeding to close this incident.")
                payload = {
                'state': "7",
                'close_code': 'Solution provided', 
                'close_notes': 'Incident resolved successfully and closed.'
                }
                close_response = requests.patch(url, auth=(username, password), headers=headers,  json=payload)
            else:
                print(f"Failed to update work notes. Status code: {update_response.status_code}")
                print("Response:", update_response.json())

else:
    print("Failed to Get Information from incident.")
    # print("Status Code:", response.status_code)
    # print("Response:", response.json())




