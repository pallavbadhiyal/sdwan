# import yaml
# from netmiko import ConnectHandler
# from jinja2 import FileSystemLoader, Environment


# file = open("inv.yml", 'r')
# devices = yaml.safe_load(file)

# data = {}
# for device in devices:
#     # Connect to the device
#     print("Connected to the device.", device["hostname"])
#     print(device["hostname"])
#     net_connect = ConnectHandler(device_type=device['device_type'],host=device['host'],username="cisco",password="cisco")


#     # Example command: display the running configuration
#     output = net_connect.send_command("show ver", use_textfsm=True)
#     # output = net_connect.send_command("show ip interface brief", use_textfsm=True)
# #     print(output)
#     # intf_status_list = [item["interface"] for item in output if "down" in item["status"] or item["proto"] == "down"]
#     tempvar = ''
#     # for item in intf_status_list:
#     #     tempvar = tempvar + item + ","
#     # intf_status_list.insert(0, device["hostname"])
#     # print(intf_status_list)
    
    
#     data.update(output)
#     # intf_status_list.insert(0, device["hostname"])
#     # Disconnect from the device
#     net_connect.disconnect()
#     print("Disconnected from the device.")

# print(data)

# # Load the Jinja2 template from file
# template_loader = FileSystemLoader(searchpath=".")
# env = Environment(loader=template_loader)
# template = env.get_template("conf_jinja.j2")
# # print(type(template))

# # Render the template with the data
# rendered_output = template.render(intf_data=data)

# # Print the rendered output or write to a file
# # print(rendered_output)
# conf_file = open('interface_report.csv', 'w')
# conf_file.write(rendered_output)
# conf_file.close()


import yaml
from netmiko import ConnectHandler
from jinja2 import FileSystemLoader, Environment

# Load devices from a YAML file
with open("inv.yml", 'r') as file:
    devices = yaml.safe_load(file)

data = {}
for device in devices:
    try:
        # Connect to the device
        print(f"Connecting to the device: {device['hostname']}")
        net_connect = ConnectHandler(
            device_type=device['device_type'],
            host=device['host'],
            username=device.get('username', 'cisco'),
            password=device.get('password', 'cisco')
        )

        # Example command: display the running configuration
        output = net_connect.send_command("show ver", use_textfsm=True)
        print(f"Output from {device['hostname']}: {output}")

        # Update data dictionary with device hostname and corresponding output
        data[device['hostname']] = output

        # Disconnect from the device
        net_connect.disconnect()
        print(f"Disconnected from the device: {device['hostname']}")

    except Exception as e:
        print(f"Failed to connect or retrieve data from {device['hostname']}: {e}")

# Load the Jinja2 template from file
template_loader = FileSystemLoader(searchpath=".")
env = Environment(loader=template_loader)
template = env.get_template("conf_jinja.j2")

# Render the template with the data
rendered_output = template.render(intf_data=data)

# Write the rendered output to a file
with open('interface_report.csv', 'w') as conf_file:
    conf_file.write(rendered_output)

print("Data collection and report generation complete.")
