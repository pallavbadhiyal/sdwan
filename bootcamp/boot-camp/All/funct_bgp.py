bgp_commands = {'neighbor': 'neighbor {} remote-as {}',
					'nexthop' : 'neighbor {} nexthop-self',
					'updatesource': 'neighbor {} updatesource loopback 1',
					'policy-in' : 'neighbor {} route-map {} in',
					'policy-out' : 'neighbor {} route-map {} out'
					}
neighborlist = [ {'remote_ip': '1.1.1.1',
					'asn' :'100',
					'policy-in': 'NETG1',
					'policy-out': 'INDIA1'
				  },{'remote_ip': '2.2.2.2',
					'asn' : '200',
					'policy-in': 'NETG2',
					'policy-out': 'INDIA2'
				  },{'remote_ip': '3.3.3.3',
					'asn' : '300',
					'policy-in': 'NETG3',
					'policy-out': 'INDIA3'
				  },{'remote_ip': '4.4.4.4',
					'asn' : '400',
					'policy-in': 'NETG4',
					'policy-out': 'INDIA4'
				  }
				  
				]
def bgp_config_gen(commands, neighbordata): # passing positional arguments
    print("router bgp 99")
    for data in neighbordata:
        print(commands["neighbor"].format(data["remote_ip"], data["asn"]))
        print(commands["nexthop"].format(data["remote_ip"]))
        print(commands["updatesource"].format(data["remote_ip"]))
        print(commands["policy-in"].format(data["remote_ip"], data["policy-in"]))
        print(commands["policy-out"].format(data["remote_ip"], data["policy-out"]))
        
def sum(a, b):
    s = a + b
    print(s)
    # return s

print("I am in funct_bgp module")
print(__name__)

# if __name__ == "__main__":
#     bgp_config_gen(bgp_commands, neighborlist)
# bgp_config_gen(bgp_commands, neighborlist)
# bgp_config_gen(bgp_commands, neighborlist)

# print("router bgp 99")
# for data in neighborlist:
#     print(bgp_commands["neighbor"].format(data["remote_ip"], data["asn"]))
#     print(bgp_commands["nexthop"].format(data["remote_ip"]))
#     print(bgp_commands["updatesource"].format(data["remote_ip"]))
#     print(bgp_commands["policy-in"].format(data["remote_ip"], data["policy-in"]))
#     print(bgp_commands["policy-out"].format(data["remote_ip"], data["policy-out"]))
    
# print("router bgp 99")
# for data in neighborlist:
#     print(bgp_commands["neighbor"].format(data["remote_ip"], data["asn"]))
#     print(bgp_commands["nexthop"].format(data["remote_ip"]))
#     print(bgp_commands["updatesource"].format(data["remote_ip"]))
#     print(bgp_commands["policy-in"].format(data["remote_ip"], data["policy-in"]))
#     print(bgp_commands["policy-out"].format(data["remote_ip"], data["policy-out"]))
    
# print("router bgp 99")
# for data in neighborlist:
#     print(bgp_commands["neighbor"].format(data["remote_ip"], data["asn"]))
#     print(bgp_commands["nexthop"].format(data["remote_ip"]))
#     print(bgp_commands["updatesource"].format(data["remote_ip"]))
#     print(bgp_commands["policy-in"].format(data["remote_ip"], data["policy-in"]))
#     print(bgp_commands["policy-out"].format(data["remote_ip"], data["policy-out"]))