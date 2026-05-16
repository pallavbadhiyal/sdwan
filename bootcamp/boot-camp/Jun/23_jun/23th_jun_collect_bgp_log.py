import yaml
import json
from napalm import get_network_driver
from jinja2 import FileSystemLoader, Environment


file = open("23_jun_inv.yml", 'r')
devices = yaml.safe_load(file)

for device in devices:        
    driver = get_network_driver('ios')
    device = driver(hostname=device['host'],username="cisco",password="cisco")
    device.open()
    # facts = device.get_facts()
    # print("Device Facts:")
    # print(facts)

    bgp_neighbors = device.get_bgp_neighbors()

    print("For Router " + bgp_neighbors["global"]["router_id"])
    print("--------------------------------------------------")
    # print(json.dumps(bgp_neighbors["global"]["peers"], indent=4))
    for neighbor_ip, details in bgp_neighbors["global"]["peers"].items():
        uptime = details['uptime']
        neighbor_name = neighbor_ip
        print(f"Neighbor: {neighbor_name}, Uptime: {int(uptime/3600)} hours")
    device.close()
    print("--------------------------------------------------")    