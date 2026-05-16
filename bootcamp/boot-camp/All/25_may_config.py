import yaml
import pandas as pd
from netmiko import ConnectHandler
from jinja2 import FileSystemLoader, Environment

file = open("25_may_data_yaml.yml", 'r')
data = yaml.safe_load(file)

# Load the Jinja2 template from file
template_loader = FileSystemLoader(searchpath=".")
env = Environment(loader=template_loader)
template = env.get_template("25_may_conf_vlan_jinja.j2")

# Render the template with the data
rendered_output = template.render(conf_vlan=data)
config_list = rendered_output.splitlines()


def read_excel_file_to_list(file_path):
    try:
        # Read Excel file into a pandas DataFrame
        data = pd.read_excel(file_path)
        # Convert DataFrame to a list of lists
        data_list = data.values.tolist()
        return data_list
    except Exception as e:
        print("An error occurred:", e)
        return None
device_ip = []

if __name__ == "__main__":
    # Provide the path to your Excel file
    excel_file_path = "Device_ip.xlsx"  
    excel_data_list = read_excel_file_to_list(excel_file_path)
    
    if excel_data_list is not None:
        for device in excel_data_list:        
            net_connect = ConnectHandler(device_type='cisco_ios',host=device[0],username="cisco",password="cisco")
            print("Connected to the device." + str(device[0]))

            # output = net_connect.send_config_set(config_list)
            # # output = net_connect.send_config_from_file('config_gen_data.conf')
            # print("configuration PUSH:")

            output = net_connect.send_command("show vlan")
            print(output)

            # Disconnect from the device
            net_connect.disconnect()
            print("Disconnected from the device." + str(device[0]))