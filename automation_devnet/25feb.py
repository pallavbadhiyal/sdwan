#############  VLAN Creation ##################
# def config_vlan(sw_ip,sw_vlan):
#     for sw_ip in sw_ip:
#         print(f"configuring switch {sw_ip}")
#         for v in sw_vlan:
#             print(f"vlan {v}")
#             print(f"vlan name vlan_{v}")

# sw_ip = [ "1.1.1.1" , "2.2.2.2" , "3.3.3.3"]
# sw_vlan = ["10","20","30"]
# config_vlan(sw_ip,sw_vlan)


#############  VLAN Creation for perticular sw  ##################
def config_vlan(sw_ip,sw_vlan):
    for sw_ip in sw_ip:
        print(f"Configuring VLAN on switch {sw_ip}")
        if sw_ip == "1.1.1.1":
            print("vlan " + sw_vlan[0])
            print("vlan name vlan_" + sw_vlan[0] )
            print("vlan " + sw_vlan[2])
            print("vlan name vlan_" + sw_vlan[2] + "\n")
        if sw_ip == "2.2.2.2":
            print("vlan " + sw_vlan[1])
            print("vlan name vlan_" + sw_vlan[1] + "\n")
        if sw_ip == "3.3.3.3":
            for v in sw_vlan:
             print(f"vlan {v}")
             print(f"vlan name vlan_{v}")

sw_ip = [ "1.1.1.1" , "2.2.2.2" , "3.3.3.3"]
sw_vlan = ["10","20","30"]
config_vlan(sw_ip,sw_vlan)

