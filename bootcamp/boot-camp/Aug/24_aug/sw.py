import os
import json
import requests
from requests.auth import HTTPBasicAuth


# Configuration
solarwinds_url = 'http://192.168.154.130:17774/SolarWinds/InformationService/v3/Json/Query?'
username = os.getenv('solarwinds_username')
password = os.getenv('solarwinds_password')

# Query to get alert information
query = "SELECT+AlertActiveID,+AlertObjectID,+TriggeredDateTime,+TriggeredMessage+FROM+Orion.AlertActive"

def get_solarwinds_alerts(url, auth, query):
    try:
        # Send the GET request to SolarWinds API
        response = requests.get(url, auth=auth, params={'query': query}, verify=False)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse JSON response
        alerts = response.json()
        
        return alerts
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def main():
    # Set up basic authentication
    auth = HTTPBasicAuth(username, password)
    
    # Get alerts
    alerts = get_solarwinds_alerts(solarwinds_url, auth, query)
    
    if alerts:
        # Print or process the alert data
        print(json.dumps(alerts, indent=4))
    else:
        print("No alerts data retrieved.")

if __name__ == "__main__":
    main()