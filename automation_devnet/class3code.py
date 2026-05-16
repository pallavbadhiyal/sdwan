ip =  input("Enter your ip: ")
# print(type(ip))
print("Given ip:" + ip)
if ip.startswith("10."):
    print("Class A Private IP")
elif ip.startswith("192.168."):
    print("Class C Private ip")
# else:
#     print("NOT Class A private ip")
