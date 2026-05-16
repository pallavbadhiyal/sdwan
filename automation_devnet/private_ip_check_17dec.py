ip = input("Plase provide IP : ")
print("given ip is " + ip)
if ip.startswith("10."):
    print("Class A private ip")
elif ip.startswith("172.") and (float(ip[4:7]) >= 16. and float(ip[4:7]) <= 31.):
    print("Class B private ip")
elif ip.startswith("192.168."):
    print("Class C private ip")
elif (float(ip[0:4]) <= 126.):
    print("this is a class A public ip")
elif (float(ip[0:4]) >= 127.) or (float(ip[0:4]) <= 191.):
    print("this is a class B public ip")
elif (float(ip[0:4]) >= 192.) or (float(ip[0:4]) <= 223.):
    print("this is a class C public ip")

