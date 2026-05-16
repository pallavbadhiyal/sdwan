import os
import json
import requests

# Replace with your ServiceNow instance URL
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
    "short_description": "Router: 192.168.154.201 | Issue : Down",
    "description": "Router: 192.168.154.201 | Issue : Down",
    "urgency": "2",  # 1 - High, 2 - Medium, 3 - Low
    "impact": "2"  # 1 - High, 2 - Medium, 3 - Low
}

# Convert data to JSON format
json_data = json.dumps(data)

# Make the request
response = requests.post(url, auth=(username, password), headers=headers, data=json_data)

# Check if the request was successful
if response.status_code == 201:
    print("Incident created successfully.")
    print("Response:", response.json())
    print("\n\n\n\n\n")
    print(response.json()['result']['sys_id'])

else:
    print("Failed to create incident.")
    print("Status Code:", response.status_code)
    print("Response:", response.json())



