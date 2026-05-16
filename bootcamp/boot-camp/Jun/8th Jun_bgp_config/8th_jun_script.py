import yaml
from netmiko import ConnectHandler
from jinja2 import FileSystemLoader, Environment

file = open("8th_june_data_yaml.yml", 'r')
data = yaml.safe_load(file)

file = open("8_jun_inv.yml", 'r')
devices = yaml.safe_load(file)

# Load the Jinja2 template from file
template_loader = FileSystemLoader(searchpath=".")
env = Environment(loader=template_loader)
template = env.get_template("8_jun_conf_R_bgp_jinja.j2")

for device in devices:        

    rendered_output = template.render(conf_data=data["bgp"][device["hostname"]])
    config_list = rendered_output.splitlines()
    # print(config_list)
    net_connect = ConnectHandler(device_type=device['device_type'],host=device['host'],username="cisco",password="cisco")

    print("Connected to the device." + device["hostname"])

    output = net_connect.send_config_set(config_list)
    # output = net_connect.send_config_from_file('config_gen_data.conf')
    print("configuration PUSH:")
    print(output)

    # Disconnect from the device
    net_connect.disconnect()
    print("Disconnected from the device." + device["hostname"])