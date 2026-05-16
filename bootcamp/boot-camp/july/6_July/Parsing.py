import yaml
from netmiko import ConnectHandler


file = open("6_july_inv.yml", 'r')
devices = yaml.safe_load(file)


for device in devices:
    # Connect to the device
    print("Connected to the device.", device["hostname"])
    print(device["hostname"])
    net_connect = ConnectHandler(device_type=device['device_type'],host=device['host'],username="cisco",password="cisco")


    # Example command: display the running configuration
    output = net_connect.send_command("show ver", use_textfsm=True)

    print(output)
    # for item in output:
    #     # print(item["interface"], item["status"])
    #     if item["status"] == "administratively down":
    #         print(item["interface"] + " is Admin Down on " + device["hostname"])
    

    # Disconnect from the device
    net_connect.disconnect()
    print("Disconnected from the device.")