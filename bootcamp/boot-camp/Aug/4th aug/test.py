# import os
# import requests
# import json
# # SolarWinds API details

# solarwinds_url = "http://192.168.154.130:17778/SolarWinds/InformationService/v3/Json/Query?query=SELECT+Uri+FROM+Orion.Pollers+ORDER+BY+PollerID+WITH+ROWS+1+TO+3+WITH+TOTALROWS"
# solarwinds_username = os.getenv('solarwinds_username')
# solarwinds_password = os.getenv('solarwinds_password')
# solarwinds_query = """
#     SELECT
#         a.AlertActiveID,
#         a.AlertObjectID,
#         a.EntityCaption,
#         a.TriggeredMessage,
#         a.Acknowledged,
#         a.TriggeredDateTime,
#         a.Notes
#     FROM
#         Orion.AlertActive a
#     WHERE
#         a.EntityType = 'Orion.Nodes'
# """  # Example query to fetch node alerts

# # Function to get information from SolarWinds
# def get_solarwinds_data():
#     headers = {
#         'Content-Type': 'application/json',
#         'Accept': 'application/json',
#     }
#     try:
#         response = requests.post(
#             solarwinds_url,
#             auth=(solarwinds_username, solarwinds_password),
#             headers=headers,
#             json={'query': solarwinds_query}
#         )
#         response.raise_for_status()
        
#         # Print the raw response content for debugging
#         print("Response Content:", response.content.decode())

#         # Parse JSON response
#         data = response.json()
#         return data
#     except requests.exceptions.HTTPError as http_err:
#         print(f"HTTP error occurred: {http_err}")
#     except requests.exceptions.ConnectionError as conn_err:
#         print(f"Connection error occurred: {conn_err}")
#     except requests.exceptions.Timeout as timeout_err:
#         print(f"Timeout error occurred: {timeout_err}")
#     except requests.exceptions.RequestException as req_err:
#         print(f"An error occurred: {req_err}")
#     except json.JSONDecodeError as json_err:
#         print(f"JSON decode error: {json_err}")
#         print("Response content:", response.content.decode())
#     return None

# # Main function
# def main():
#     # Collect data from SolarWinds
#     solarwinds_data = get_solarwinds_data()
    
#     # Check if data is returned
#     if solarwinds_data:
#         # Print the retrieved data
#         for alert in solarwinds_data.get('results', []):
#             print(f"AlertActiveID: {alert['AlertActiveID']}, AlertObjectID: {alert['AlertObjectID']}, "
#                   f"EntityCaption: {alert['EntityCaption']}, TriggeredMessage: {alert['TriggeredMessage']}, "
#                   f"Acknowledged: {alert['Acknowledged']}, TriggeredDateTime: {alert['TriggeredDateTime']}, "
#                   f"Notes: {alert['Notes']}")
#     else:
#         print("No data retrieved or an error occurred.")
# if __name__ == '__main__':
#     main()

import subprocess
def ping_device(ip_address):
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
    
ip_address = "192.168.154.201"

print(ping_device(ip_address))