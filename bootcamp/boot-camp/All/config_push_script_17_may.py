import yaml
from netmiko import ConnectHandler
from jinja2 import FileSystemLoader, Environment

file = open("config_data_17_may.yml", 'r')
data = yaml.safe_load(file)

# Load the Jinja2 template from file
template_loader = FileSystemLoader(searchpath=".")
env = Environment(loader=template_loader)
template = env.get_template("config_syntax_17_may.j2")

# Render the template with the data
rendered_output = template.render(conf_vlan=data)

# Print the rendered output or write to a file
print(rendered_output)
conf_file = open('config_gen_data_17_may.conf', 'w')
conf_file.write(rendered_output)
conf_file.close()


devices = [{
    'device_type': 'cisco_ios',
    'host': '192.168.119.137',
    'username': 'cisco',
    'password': 'cisco',
},
   {
    'device_type': 'cisco_ios',
    'host': '192.168.119.136',
    'username': 'cisco',
    'password': 'cisco',
   },
   
    {
    'device_type': 'cisco_ios',
    'host': '192.168.119.138',
    'username': 'cisco',
    'password': 'cisco',
}]

for device in devices:
    net_connect = ConnectHandler(**device)
    print("Connected to the device." + device["host"])

# output = net_connect.send_command("show vlan")
    output = net_connect.send_config_from_file('config_gen_data_17_may.conf')
    print("configuration PUSH:")
    print(output)