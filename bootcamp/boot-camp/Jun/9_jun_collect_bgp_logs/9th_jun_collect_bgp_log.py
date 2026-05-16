import yaml
from netmiko import ConnectHandler
# from jinja2 import FileSystemLoader, Environment

# file = open("8th_june_data_yaml.yml", 'r')
# data = yaml.safe_load(file)

file = open("9_jun_inv.yml", 'r')
devices = yaml.safe_load(file)

# # Load the Jinja2 template from file
# template_loader = FileSystemLoader(searchpath=".")
# env = Environment(loader=template_loader)
# template = env.get_template("8_jun_conf_R_bgp_jinja.j2")

for device in devices:        
    # rendered_output = template.render(conf_data=data["bgp"][device["hostname"]])
    # config_list = rendered_output.splitlines()
    # print(config_list)
    net_connect = ConnectHandler(device_type=device['device_type'],host=device['host'],username="cisco",password="cisco")
    print("BGP neighborship on device  " + device["hostname"])
    print("--------------------------------------------------")
    output = net_connect.send_command("show ip bgp su | b Nei ")
    output = output.split()
    print("Neighbor " + str(output[10]) + " is up from " + str(output[18]))
    if len(output) > 20:
        print("Neighbor " + str(output[20]) + " is up from " + str(output[28]))
    # output = net_connect.send_config_from_file('config_gen_data.conf')
    # print("configuration PUSH:")
    # Disconnect from the device
    net_connect.disconnect()
    print("--------------------------------------------------")
    print("\n\n\n")