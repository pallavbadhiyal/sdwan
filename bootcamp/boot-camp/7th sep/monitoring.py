import os
import json
import requests
import subprocess
import pandas as pd

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
device_ip = []

if __name__ == "__main__":
    # Provide the path to your Excel file
    excel_file_path = "inv.xlsx"  
    excel_data_list = read_excel_file_to_list(excel_file_path)
    
    if excel_data_list is not None:
        for device in excel_data_list:
            ip_address = device[0].strip()
            ci = device[1].strip()
            if "not reachable" in ping_device(ip_address):
                print("Not Reachable\n\nNot Reachable")
                print(f"Device Ping status :\n{ping_device(ip_address)}")
                instance_url = "https://dev254366.service-now.com/"

                # API endpoint for creating an incident
                url = f"{instance_url}/api/now/table/incident"

                # Replace with your ServiceNow username and password
                username = 'admin'
                password = 'MSa94!rmZ!xF'

                # Headers for the request
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                }

                # Data for the new incident
                data = {
                    "short_description": f"Device : {ci} is not reachable",
                    "description": f"Device : {ci} | IP Address : {ip_address} | Issue : Down",
                    "urgency": "2",  # 1 - High, 2 - Medium, 3 - Low
                    "impact": "2",  # 1 - High, 2 - Medium, 3 - Low
                    "cmdb_ci": f"{ci}",
                    "assignment_group": "network",
                    "caller_id": "Pallav Badhiyal"
                }

                # Convert data to JSON format
                json_data = json.dumps(data)

                # Make the request
                response = requests.post(url, auth=(username, password), headers=headers, data=json_data)

                # Check if the request was successful
                if response.status_code == 201:
                    print("Incident created successfully.")
                    print("Response:", response.json())

                else:
                    print("Failed to create incident.")
                    print("Status Code:", response.status_code)
                    print("Response:", response.json())


            else:
                print("Reachable\n\nReachable")
                print(f"Device Ping status :\n{ping_device(ip_address)}")
            