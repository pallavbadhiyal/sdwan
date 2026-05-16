# import funct_bgp # includes all functions
from funct_bgp import bgp_config_gen # Imports selective function

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

# if __name__ == "__main__":
# 	bgp_config_gen(bgp_commands, neighborlist)
# sum(10,20)

print("I am in copy module")
print(__name__)