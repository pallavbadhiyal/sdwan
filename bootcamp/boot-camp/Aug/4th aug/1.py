import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime

# Configuration
solarwinds_url = 'http://192.168.154.130:17778/SolarWinds/Orion'
api_version = 'v3'
username = 'admin'
password = 'Admin@123'
alert_resource = 'Alerts'

# Construct the API endpoint
api_endpoint = f'{solarwinds_url}/api/{api_version}/{alert_resource}'

# Set the query parameters (adjust the query to your needs)
query_params = {
    'sysparm_query': 'status=1',  # 1 typically represents active alerts; adjust if needed
    'sysparm_fields': 'AlertID,Node.Caption,Node.LastSync,Alert.Time,Alert.Status,Alert.Message',
    'sysparm_limit': '10'  # Adjust the limit as needed
}

# Make the request
try:
    response = requests.get(api_endpoint, auth=HTTPBasicAuth(username, password), params=query_params, headers={'Content-Type': 'application/json'}, verify=False)

    # Check if the request was successful
    response.raise_for_status()
    data = response.json()

    # Print the results
    print("Alerts retrieved successfully:")
    for record in data.get('results', []):
        device_name = record.get('Node', {}).get('Caption', 'Unknown Device')
        alert_time = record.get('Alert', {}).get('Time', 'Unknown Time')
        status = record.get('Alert', {}).get('Status', 'Unknown Status')
        message = record.get('Alert', {}).get('Message', 'No Message')

        # Calculate downtime if applicable
        if status == '1':  # Assuming '1' indicates an active alert
            opened_at = datetime.strptime(alert_time, '%Y-%m-%dT%H:%M:%S.%fZ')  # Adjust format if necessary
            current_time = datetime.utcnow()
            downtime = current_time - opened_at

            print(f"Device Name: {device_name}")
            print(f"Alert Time: {alert_time}")
            print(f"Status: {status}")
            print(f"Message: {message}")
            print(f"Downtime: {downtime}")
            print("-" * 40)
        else:
            print(f"Device Name: {device_name}")
            print(f"Alert Time: {alert_time}")
            print(f"Status: {status}")
            print(f"Message: {message}")
            print("-" * 40)

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.RequestException as req_err:
    print(f"Error occurred: {req_err}")
except ValueError as json_err:
    print(f"JSON decoding error: {json_err}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
