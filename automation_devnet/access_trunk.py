

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
