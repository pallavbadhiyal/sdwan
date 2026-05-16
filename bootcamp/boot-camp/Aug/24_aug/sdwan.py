
import requests
import json
from requests.auth import HTTPBasicAuth
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Cisco SD-WAN details
SDWAN_CONTROLLER = 'https://sandbox-sdwan-2.cisco.com'
USERNAME = 'devnetuser'
PASSWORD = 'RG!_Yw919_83'

# ServiceNow details
SN_INSTANCE = 'https://dev199136.service-now.com'
SN_USERNAME = 'admin'
SN_PASSWORD = '$w8ju+QIGi8I'

def get_token(controller, username, password): #SDwan connectivityaca
    """
    Authenticate and retrieve a session token.
    """
    url = f"{controller}/j_security_check"
    payload = {
        'j_username': username,
        'j_password': password
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    try:
        response = requests.post(url, data=payload, headers=headers, verify=False)
        response.raise_for_status()
        if 'JSESSIONID' in response.cookies:
            return response.cookies['JSESSIONID']
        else:
            raise Exception("Authentication failed: JSESSIONID not found in response.")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {e}")

def get_device_details(controller, token): #SDwan Connectivity
    """
    Get device details.
    """
    url = f"{controller}/dataservice/device"
    headers = {
        'Cookie': f'JSESSIONID={token}',
        'Content-Type': 'application/json'
    }

    try:
        response = requests.get(url, headers=headers, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {e}")

def create_incident(instance, username, password, incident_details): #Service now connectivity
    """
    Create a new incident in ServiceNow.
    """
    url = f"{instance}/api/now/table/incident"
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    try:
        response = requests.post(
            url,
            auth=HTTPBasicAuth(username, password),
            headers=headers,
            data=json.dumps(incident_details),
            verify=False  # Disable SSL verification (not recommended for production)
        )
        response.raise_for_status()
        
        if response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Failed to create incident: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {e}")

def main():
    try:
        # Get Cisco SD-WAN token and device details
        print("Attempting to retrieve token...")
        token = get_token(SDWAN_CONTROLLER, USERNAME, PASSWORD)
        print("Token retrieved successfully.")

        print("Attempting to retrieve device details...")
        device_details = get_device_details(SDWAN_CONTROLLER, token)
        print("Device details retrieved successfully.")
        
        # Print device details for debugging
        print("Device Details Retrieved:")
        print(json.dumps(device_details, indent=4))

        # # Check device details
        # for device in device_details.get('data', []):
        #     print("Checking device:", device)  # Add this line to see each device data

        #     if (device.get('deviceId') == '10.10.1.17' and 
        #         device.get('host-name') == 'site3-vedge01' and 
        #         device.get('total_cpu_count') == '2'):
                
        #         print("Device matched criteria:", json.dumps(device, indent=4))
        #         state = device.get('state')
                
        #         # Define incident details
        #         incident_details = {
        #             "short_description": f"Device {device.get('host-name')} ({device.get('deviceId')}) has an issue.",
        #             "description": f"Device {device.get('host-name')} with ID {device.get('deviceId')} and CPU count {device.get('total_cpu_count')} has state: {state}.",
        #             "category": "network",
        #             "subcategory": "router",
        #             "assignment_group": "Network Support",
        #             "urgency": "2",
        #             "impact": "2"
        #         }
                
        #         # Create incident in ServiceNow
        #         result = create_incident(SN_INSTANCE, SN_USERNAME, SN_PASSWORD, incident_details)
        #         print("Incident created successfully:")
        #         print(json.dumps(result, indent=4))
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
