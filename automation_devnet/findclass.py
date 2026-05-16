ip = input("Enter your IP : ")
print("Given IP : " + ip)
if ip.startswith("10."):
    print("Class A Private IP")
elif ip.startswith("172.16."):
    print("Class B Private IP")
elif ip.startswith("192.168."):
    print("Class C Private IP")
