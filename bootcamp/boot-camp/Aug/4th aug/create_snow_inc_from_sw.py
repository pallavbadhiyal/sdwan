import os
import json
import requests

# SolarWinds API details
solarwinds_url = 'http://192.168.154.130:17778/SolarWinds/InformationService/v3/Json/Query'
solarwinds_username = os.getenv('solarwinds_username')
solarwinds_password = os.getenv('solarwinds_password')
solarwinds_query = "SELECT NodeID, Caption, Status FROM Orion.Nodes"  # Example query

# ServiceNow API details

# Replace with your ServiceNow instance URL
instance_url = "https://dev254366.service-now.com/"

# API endpoint for creating an incident
servicenow_url = f"{instance_url}/api/now/table/incident"
servicenow_url = '"https://dev254366.service-now.com/api/now/table/incident'
servicenow_username = os.getenv('servicenow_username')
servicenow_password = 'MSa94!rmZ!xF'

# Function to get information from SolarWinds
def get_solarwinds_data():
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    response = requests.post(
        solarwinds_url,
        auth=(solarwinds_username, solarwinds_password),
        headers=headers,
        json={'query': solarwinds_query}
    )
    response.raise_for_status()
    return response.json()

# Function to create an incident in ServiceNow
def create_servicenow_incident(description):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    incident_data = {
        'short_description': 'Issue detected by SolarWinds',
        'description': description,
        'urgency': '2',
        'impact': '2'
    }
    response = requests.post(
        servicenow_url,
        auth=(servicenow_username, servicenow_password),
        headers=headers,
        json=incident_data
    )
    response.raise_for_status()
    return response.json()

# Main function
def main():
    # Collect data from SolarWinds
    solarwinds_data = get_solarwinds_data()
    print (solarwinds_data)    
    # # Example of processing the data and creating a description
    # description = 'Nodes status information:\n'
    # for node in solarwinds_data['results']:
    #     description += f"NodeID: {node['NodeID']}, Caption: {node['Caption']}, Status: {node['Status']}\n"

    # # Create an incident in ServiceNow
    # incident_response = create_servicenow_incident(description)
    # print('Incident created successfully:', incident_response)

if __name__ == '__main__':
    main()
