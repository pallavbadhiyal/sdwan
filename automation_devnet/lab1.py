# Practicing Dictionary concept

deviceinfo = {
    "name": "us-kingston-sw1",
    "site": "kingston",
    "model": 9300,
    "HA": True,
    "site-contacts": [{"name": "John", "role": "automation analyst"}, {"name": "Greg", "role": "Automation eng."}]
}

# print(type(deviceinfo["site-contacts"][0]))
# print(deviceinfo["site-contacts"])
# site = deviceinfo["site-contacts"]
# print(list(site[0].values())[1])

print(list(deviceinfo["site-contacts"][1].values())[1])
print(deviceinfo["site-contacts"][1]["role"])
# site[0].values()