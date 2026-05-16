# ip = input("Enter your IP: ")
# # print(ip)
# # print(type(ip))
# # print("spliting the ip now")
# ip = ip.split('.')
# # print(ip)
# # print(type(ip))
# # print(type(ip[0]))
# # if len(ip) == 4:
# #     for item in ip:
# #         if item.isdigit():
# #             continue
# #         else:
# #             print("List element is NOT digit")
# #             break
# #     print("Valid IP")
# # else:
# #     print("Given ip NOT valid ip")
# if (len(ip) == 4) and (for item in ip):
        

#         if item.isdigit():
#             print("Valid IP")
#         else:    
#          print("List element is NOT digit")
             
# else:
#     print("Given ip NOT valid ip")


# vlans = [10,20,30,40]
# switches =  ["sw1", "sw2", "sw3"]

# for sw in switches:
#     print("Configuring switch " + sw)
#     for vlan in vlans:
#         print(vlan)
#         print("vlan_" +str(vlan))

# switches = ["1.1.1.1", "2.2.2.2", "3.3.3.3"]
# configs = ["config t", "interface gig0/1", "description connects to server", "switchport", "switchport mode access", "switchport access vlan 10"]

      

# for sw in switches:
#     print("\n\nconfiguring access vlan on switch " + sw)
#     for config in configs:
#         print(config)

switches = ["1.1.1.1", "2.2.2.2", "3.3.3.3"]
interfaces = ["gig0/0", "gig0/1", "gig0/2", "gig0/3"]

access_configs = ["switchport", "switchport mode access", "switchport access vlan 10"]
trunk_configs = ["switchport", "switchport mode trunk", "switchport trunk allowed vlan add 10"]

for sw in switches:
    print("Configuring " + sw)
    for intf in interfaces:
        if intf == "gig0/0" or intf == "gig0/2":
            print("\n"+"interface "+ intf )
            for conf in trunk_configs:
                print(conf)
        else:
            print("\n"+"interface "+ intf )
            for conf in access_configs:
                print(conf)
    print("\n")
