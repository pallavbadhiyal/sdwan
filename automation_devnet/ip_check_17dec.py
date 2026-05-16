ip = input("Plase provide IP : ")
print("given ip is " + ip)
if ip.startswith("10."):
    print("Class A private ip")
elif ip.startswith("172.") and (float(ip[4:7]) >= 16. and float(ip[4:7]) <= 31.):
    print("Class B private ip")
elif ip.startswith("192.168."):
    print("Class C private ip")
else:
    print("Given ip is not private ip")




    