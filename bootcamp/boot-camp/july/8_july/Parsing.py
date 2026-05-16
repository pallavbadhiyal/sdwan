import yaml
from netmiko import ConnectHandler


file = open("6_july_inv.yml", 'r')
devices = yaml.safe_load(file)
output_file = open("6_july_inv.txt", 'w')
com = open("command.txt", "r")
command = com.splitlines()

print(command)
# for device in devices:
#     net_connect = ConnectHandler(device_type=device['device_type'],host=device['host'],username="cisco",password="cisco")
#     output = net_connect.send_command(command)
#     output_file.write(output)
 
#     net_connect.disconnect()
#     # print("Disconnected from the device.")


# output_file.close()
# file.close()