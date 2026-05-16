device_info = {

"device_name" : "Router 1",
"device_type" : "cisco",
"device_ver" : "17.1.10",
"device_interface": "48",
"site_contact":[{"name":"Josh","role":"Manager"},{"name":"Paul","role":"Engineer"}]
}


# print(device_info["site_contact"][1]["role"])
for site_contact in device_info["site_contact"]:
    if (site_contact["name"]) == "Paul":
        print(site_contact["role"])