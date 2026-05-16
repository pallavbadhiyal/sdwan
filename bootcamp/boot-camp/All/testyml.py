import yaml		 
config_file  = open("config_yml.yaml", 'r') 
config_data = yaml.safe_load(config_file)
config_file.close()

config_file  = open("config_yml_wr.yaml", 'w') 
yaml.dump(config_data, config_file)

# import json
# config_file  = open("config_json.json", 'r')
# config_data = json.load(config_file)
# # print(type(config_data))


# config_file  = open("config_json_wr.json", 'w')
# json.dump(config_data, config_file, indent=4)

configtempl = {"intf": "interface {}",
               'desc':'description {}',
			    'speed': 'speed {}',
				'duplex': 'duplex {}'
			  }

config_file = open("config_data.config", 'w')


for k, v in configtempl.items():
    print(configtempl[k].format(config_data[k]))

