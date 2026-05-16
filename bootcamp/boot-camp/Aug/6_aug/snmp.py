import yaml
from netmiko import ConnectHandler


file = open("inv.yml", 'r')
devices = yaml.safe_load(file)


config_list = ["access-list 2 permit 192.168.154.130",
               "snmp-server community LAB ro 2"
]

for device in devices:        
    net_connect = ConnectHandler(device_type=device['device_type'],host=device['host'],username="cisco",password="cisco")
    print("Connected to the device." + device["hostname"])
    output = net_connect.send_config_set(config_list)
    # output = net_connect.send_command("wr")
    print("configuration PUSH:")
    print(output)

    # Disconnect from the device
    net_connect.disconnect()
    print("Disconnected from the device." + device["hostname"])