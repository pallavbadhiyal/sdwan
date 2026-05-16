
def config_gen(sw_config_data,sw_config_syntax):
    for k, v in sw_config_data.items(): 
        if k == "intf":
            print(sw_config_syntax["intf_s"].format(v))
        elif k == "desc":
            print(sw_config_syntax["desc_s"].format(v))
        elif k == "intf_mode":
            print(sw_config_syntax["intf_mode_s"].format(v))
        else:
            print(sw_config_syntax["vlan_id_s"].format(v))



sw_config_data = {
    "intf": "gig0/1",
    "desc": "Connected to server 1",
    "intf_mode": "access",
    "vlan_id": "10"
}

sw_config_syntax = {
    "intf_s": "interface {}",
    "desc_s": "description {}",
    "intf_mode_s": "switchport mode {}",
    "vlan_id_s": "switchport access vlan {}"
}
config_gen(sw_config_data,sw_config_syntax)
