# sw_config_data = {
#     "intf": "gig0/1",
#     "desc": "Connected to server",
#     "intf_mode": "access",
#     "vlan_id": "10"
# }

# sw_config_syntax = {
#     "intf": "interface {}",
#     "desc": "description {}",
#     "intf_mode": "switchport mode {}",
#     "vlan_id": "switchport access vlan {}"
# }

# for k, v in sw_config_data.items():
#     print(sw_config_syntax[k].format(v))

#########################  More   #############################

sw_config_data_list = [{
    "intf": "gig0/1",
    "desc": "Connected to server",
    "intf_mode": "access",
    "vlan_id": "10"
},
{
    "intf": "gig0/2",
    "desc": "Connected to server",
    "intf_mode": "access",
    "vlan_id": "11"
},
{
    "intf": "gig0/3",
    "desc": "Connected to server",
    "intf_mode": "access",
    "vlan_id": "12"
}]

sw_config_syntax = {
    "intf": "interface {}",
    "desc": "description {}",
    "intf_mode": "switchport mode {}",
    "vlan_id": "switchport access vlan {}"
}

config = []
for sw_config_data in sw_config_data_list:
    for k, v in sw_config_data.items():
        config.append(sw_config_syntax[k].format(v))
print(config)
