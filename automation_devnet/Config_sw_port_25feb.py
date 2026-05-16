########################### STANDARD CONFIG #####################################
# def config_switch_with_desc(switches,interfaces,description_1,description_2):
#     for sw in switches:
#         print("\nConfiguring " + sw)
#         for intf in interfaces:
#             print("interface " + intf )
#             if intf == "gig0/1" or intf == "gig0/3":
#                 print(description_1)
#             else:
#                 print(description_2)

# switches = ["sw1", "sw2", "sw3"]
# interfaces = ["gig0/1", "gig0/2", "gig0/3"]
# description_1 = "description Connected to Server"
# description_2 = "description Connected to Core Switch"
# config_switch_with_desc(switches,interfaces,description_1,description_2)



########################### NO STANDARD CONFIG #####################################
def config_switch_with_desc(switches,interfaces,description_1,description_2):
    for sw in switches:
        if sw == "sw1":   
            print("\nConfiguring " + sw)
            for intf in interfaces:
                print("interface " + intf )
                if intf == "gig0/1" or intf == "gig0/3":
                    print(description_1)
                else:
                    print(description_2)
        
        if sw == "sw2":   
            print("\nConfiguring " + sw)
            for intf in interfaces:
                print("interface " + intf )
                if intf == "gig0/1":
                    print(description_2)
                else:
                    print(description_1)
        if sw == "sw3":   
            print("\nConfiguring " + sw)
            for intf in interfaces:
                print("interface " + intf )
                if intf == "gig0/1" or intf == "gig0/3":
                    print(description_2)
                else:
                    print(description_1)



switches = ["sw1", "sw2", "sw3"]
interfaces = ["gig0/1", "gig0/2", "gig0/3"]
description_1 = "description Connected to Server"
description_2 = "description Connected to Core Switch"
config_switch_with_desc(switches,interfaces,description_1,description_2)