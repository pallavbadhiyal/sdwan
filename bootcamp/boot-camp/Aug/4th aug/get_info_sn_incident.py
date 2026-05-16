import os
import json
import requests

username = os.getenv('sn_username')
password = 'MSa94!rmZ!xF'

###########################################################################################################################
instance_url = "https://dev254366.service-now.com/"

# API endpoint for updating an incident (replace 'incident_sys_id' with the actual sys_id of the incident)
incident_sys_id = "2a97b13b83b78610c82e9b80deaad3f1"
url = f"{instance_url}/api/now/table/incident/{incident_sys_id}"
# Headers for the request
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Incident Information
response = requests.get(url, auth=(username, password), headers=headers)
# Check if the request was successful
if response.status_code == 200:
    print("Incident Information:", response.json())
else:
    print("Failed to Get Information from incident.")



