# config_data = [{"intf": "Gig0/1",
# 		    'speed': '1000',
# 			'duplex': 'full',
#             'desc': 'switchport',
# 		   },
#            {"intf": "Gig0/2",
# 		    'speed': '1000',
# 			'duplex': 'full',
#             'desc': 'switchport',
# 		   },
#            {"intf": "Gig0/3",
# 		    'speed': '1000',
# 			'duplex': 'full',
#             'desc': 'switchport',
# 		   }]
		   
command = {"intf": "Gig0/1",
		    'speed': '1000',
			'duplex': 'full',
            'desc': 'switchport',
		   }
     
configtempl = {"intf": "interface {}",
               'desc':'description {}',
			    'speed': 'speed {}',
				'duplex': 'duplex {}'
			  }

config_file = open("config_data.config", 'w')


for k, v in configtempl.items():
    # print(v)
    # print(configtempl[k].format(config_data[k]))
    config_file.write(configtempl[k].format(config_data[k] + '\n'))

config_file.close()

open_to_read = open("config_data.config", 'r')

# Reads each line at a time, used for knows line of numbers
for counter in range(4):
	print(open_to_read.readline().rstrip('\n'))
	print("Hello")

open_to_read.close()

open_to_read = open("config_data.config", 'r')
# reads all line of config from the given file object
file_data_output = open_to_read.readlines()
print(file_data_output)

open_to_read.close()

open_to_read = open("config_data.config", 'r')
# Reads all lines at a time from the file
for data in open_to_read.readlines():
    print(data.rstrip('\n'))

