site_list = ["site-A", "site-B", "site-C"]
sw_list = ["sw1", "sw2", "sw3"]
intf_list = ["gig0/1","gig0/2","gig0/3","gig0/4"]
intf_config = ["switchport", "switchport mode access", "switchport access vlan 10"]
intf_trunk_config = ["switchport", "switchport mode trunk", "switchport trunk allowed vlan add 10"]

for site in site_list:
    print("Configuring", site)
    print("$$$$$$$$$$$$$$$$$$$$")
    for sw in sw_list:
        print("Configuring", sw)
        print("^^^^^^^^^^^^^^^^^")
        for intf in intf_list:
            print(f"interface {intf}")
            if intf == "gig0/1" or intf == "gig0/3":
                for config in intf_trunk_config:
                    print(config)
            else:
                for config in intf_config:
                    print(config)
            print("###############################")