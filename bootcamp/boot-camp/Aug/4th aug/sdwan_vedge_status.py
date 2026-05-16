import os
import json
import requests

# Replace with your Cisco SD-WAN controller URL
base_url = "http://10.10.20.90/"

# API endpoint for device status (replace 'device_id' with the actual device ID)
device_id = "Devbox"
url = f"{base_url}/dataservice/device"

# Replace with your API username and password
username = "admin"
password = "C1sco12345"


# Disable warnings for insecure requests (self-signed certificates)
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def get_api_token(session):
    # Assuming your vManage uses a login endpoint for getting the token
    login_url = f"{base_url}/j_security_check"
    login_data = {
        "j_username": username,
        "j_password": password
    }

    response = session.post(login_url, data=login_data, verify=False)
    
    if response.status_code != 200:
        raise Exception(f"Failed to login. Status Code: {response.status_code}. Response: {response.text}")
    
    # The session should now be authenticated; return the session object
    return session

def get_devices(session):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    response = session.get(url, headers=headers, verify=False)
    
    print("Response Status Code:", response.status_code)
    print("Response Text:", response.text)
    
    if response.status_code == 200:
        try:
            return response.json()
        except ValueError as e:
            print("Failed to parse JSON. Response content:", response.text)
            raise e
    else:
        raise Exception(f"Failed to retrieve devices. Status Code: {response.status_code}. Response: {response.text}")
def main():
    with requests.session() as session:
        # Log in to the API to get a session token
        get_api_token(session)

        # Retrieve the list of connected devices
        devices = get_devices(session)
        
        # Print the devices information
        print("Connected devices:")
        print(json.dumps(devices, indent=2))

if __name__ == "__main__":
    main()