ip = input("Please provide your ip address: ")
ip_address = ip.split(".")
size = len(ip_address)
if size==4 and all (0 < int(ip) <= 255 for ip in ip_address):
    print(f"\n{ip} is a Valid IP")
else    :    
    print(f"\n{ip} is not a Valid IP")

if ip.startswith("10"):
    print("Class A private ip")
elif ip.startswith("172.") and (16 <= int(ip_address[1]) <= 31):
    print("Class B private ip")
elif ip.startswith("192.168."):
    print("Class C private ip")
elif (int(ip_address[0]) <= 126):
    print("this is a class A public ip")
elif (int(ip_address[0]) >= 127) and (int(ip_address[0]) <= 191):
    print("this is a class B public ip")
elif (int(ip_address[0]) >= 192) and (int(ip_address[0]) <= 223):
    print("this is a class C public ip")