commands_data = [{"intf": "Gig0/1",
		    'speed': '1000',
			'duplex': 'full',
            'desc': 'switchport',
		   },
           {"intf": "Gig0/2",
		    'speed': '1000',
			'duplex': 'full',
            'desc': 'switchport',
		   },
           {"intf": "Gig0/3",
		    'speed': '1000',
			'duplex': 'full',
            'desc': 'switchport',
		   }]
		   
configtempl = {"intf": "interface {}",
               'desc':'description {}',
			    'speed': 'speed {}',
				'duplex': 'duplex {}'
			  }

# for k, v in commands.items():
#     # print(v)
#     print(configtempl[k].format(commands[k]))

for config in commands_data:
    for k, v in config.items():
        print(configtempl[k].format(config[k]))