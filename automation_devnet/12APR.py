# from netmiko import ConnectHandler

# iosv_l2 = {
#     "device_type" : "cisco_ios",
#     "ip" : "192.168.119.133",
#     "username" : "cisco",
#     "password" : "cisco"

# }

# net_connect = ConnectHandler(**iosv_l2)
# # output = net_connect.send_command("show ip ro")
# # print(output)

# output = net_connect.send_command("sh ver")
# # print(output)

# data = open("12APR.txt", 'w')

# data.write(output)
# data.close()

read_output = open("12APR.txt", 'r')
read_file = read_output.readlines()

for item in read_file:
    if item.startswith("BOOTLDR"):
        print(item)
    else:
        break
read_output.close()
