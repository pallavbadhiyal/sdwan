from netmiko import ConnectHandler

iosv_l2 = {
    "device_type" : "cisco_ios",
    "ip" : "192.168.119.133",
    "username" : "cisco",
    "password" : "cisco"

}

net_connect = ConnectHandler(**iosv_l2)
# output = net_connect.send_command("show ip ro")
# print(output)

output = net_connect.send_command("sh ip int bri")
print(output)



