import os
import requests
from orionsdk import SwisClient
 
# main() is our main function to do the thing
def main():
    # these are the variables where we store your connection information
    hostName  = '192.168.154.130'
    username  = os.getenv('solarwinds_username')
    password  = os.getenv('solarwinds_password')
    # This is the query we are using
    swqlQuery = 'SELECT Caption, Uri FROM Orion.Nodes ORDER BY Caption'
 
    # Build a connection to the server
    swis = SwisClient(hostName, username, password)
   
    # let's run the query and store the results in a variable
    response = swis.query(swqlQuery)
    print(response)
    # there are multiple responses, so we'll need to go through each entry
    for result in response['results']:
        # output the caption and uri
        print("{Caption} [{Uri}]".format(**result))
 
requests.packages.urllib3.disable_warnings()
 
if __name__ == '__main__':
    main()

#=============================================Export alerts =======================================================

# import os
# import requests
# from orionsdk import SwisClient


# def main():
#     npm_server = '192.168.154.130'
#     username  = os.getenv('solarwinds_username')
#     password  = os.getenv('solarwinds_password')

#     AlertID = 1 #AlertID for which we export data in xml file.

#     swis = SwisClient(npm_server, username, password)
#     results = swis.invoke('Orion.AlertConfigurations', 'Export', AlertID)
#     print(results)

#     with open('out.xml', 'w') as f:
#         f.write(results)

# requests.packages.urllib3.disable_warnings()


# if __name__ == '__main__':
#     main()

#==============================Add Alert node

# import os
# import requests
# from orionsdk import SwisClient

# # Configuration
# solarwinds_url = '192.168.154.130'
# username  = os.getenv('solarwinds_username')
# password  = os.getenv('solarwinds_password')


# # Initialize the SWIS client
# client = SwisClient(solarwinds_url, username, password)

# def get_all_alerts():
#     # Define the SWQL query to fetch all alerts
#     query = "SELECT NodeID, Caption, IPAddress FROM Orion.AlertInfo"
#     # query = "SELECT TOP 10 Alert.DisplayName AS AlertName, Alert.Message AS AlertDescription, Alert.TimeStamp AS AlertTime FROM Orion.AlertInfo AS Alert ORDER BY Alert.TimeStamp DESC"


#     try:
#         # Execute the SWQL query
#         alerts = client.query(query)
        
#         # Return the results
#         return alerts['results']
    
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return None

# def main():
#     # Get all alerts
#     alerts = get_all_alerts()
    
#     if alerts:
#         # Print or process the alert data
#         for alert in alerts:
#             print(alert)
#     else:
#         print("No alerts data retrieved.")

# requests.packages.urllib3.disable_warnings()

# if __name__ == "__main__":
#     main()