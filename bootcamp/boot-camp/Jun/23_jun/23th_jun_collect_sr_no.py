import yaml
import json
from napalm import get_network_driver


file = open("23_jun_inv.yml", 'r')
devices = yaml.safe_load(file)

for device in devices:        
    driver = get_network_driver('ios')
    device = driver(hostname=device['host'],username="cisco",password="cisco")
    device.open()
    facts = device.get_facts()
    # print("Device Facts:")
    # print(facts["hostname"])

    print("--------------------------------------------------")
    print(" For " + facts["hostname"] + " Serial Number is " + facts["serial_number"])
    device.close()
    print("--------------------------------------------------")    