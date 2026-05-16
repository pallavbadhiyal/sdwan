import os
import json
import requests
import subprocess
import pandas as pd
from netmiko import ConnectHandler

# ServiceNow instance details
instance = "dev254366"
username = 'admin'
password = 'MSa94!rmZ!xF'
ssh_username = 'cisco'
ssh_password = 'cisco'

def get_incident_details(ci_name):
    url = f"https://{instance}.service-now.com/api/now/table/incident"

    query_params = {
        'sysparm_query': f'cmdb_ci.name={ci_name}^active=true',
        'sysparm_fields': 'sys_id,number,short_description,cmdb_ci,caller_id,assignment_group,state,priority,opened_at',
        'sysparm_limit': 1,  # Limit to 1 result to get the latest
        'sysparm_order_by': 'opened_at'  # Sort by opened_at (descending by default)
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    response = requests.get(url, auth=(username, password), headers=headers, params=query_params)

    if response.status_code == 200:
        incidents = response.json().get('result', [])

        if incidents:
            incident = incidents[0]  # Get the first (latest) incident
            incident_number = incident['number']
            sys_id = incident['sys_id']
            print(f"Incident Number: {incident_number}")
            print(f"sys_id: {sys_id}")
            return sys_id

        else:
            print(f"No active incidents found for CI: {ci_name}")
    else:
        print(f"Failed to query incidents. Status Code: {response.status_code}")

def read_excel_file_to_list(file_path):
    try:
        # Read Excel file into a pandas DataFrame
        data = pd.read_excel(file_path)
        # Convert DataFrame to a list of lists
        data_list = data.values.tolist()
        return data_list
    except Exception as e:
        print("An error occurred:", e)
        return None
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

def connect_device(ip_address):
    net_connect = ConnectHandler(device_type='cisco_ios',host=ip_address,username=ssh_username,password= ssh_password)
    device_output = net_connect.send_command("show ip bgp su | b Nei")
    device_uptime = net_connect.send_command("show ver | in uptime")
    device_output1 = f"Device BGP status \n{device_output}\n\n Device uptime \n{device_uptime} "

    if device_output:
        return device_output1
    net_connect.disconnect()

if __name__ == "__main__":
    # Provide the path to your Excel file
    excel_file_path = "inv.xlsx"  
    excel_data_list = read_excel_file_to_list(excel_file_path)
    
    if excel_data_list is not None:
        for device in excel_data_list:
            ci_name = device[1].strip()
            sys_id = get_incident_details(ci_name)
            instance_url = "https://dev254366.service-now.com/"

            # API endpoint for updating an incident (replace 'incident_sys_id' with the actual sys_id of the incident)
            url = f"{instance_url}/api/now/table/incident/{sys_id}"
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
                        url = f"{instance_url}/api/now/table/incident/{sys_id}"
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
                        url = f"{instance_url}/api/now/table/incident/{sys_id}"
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