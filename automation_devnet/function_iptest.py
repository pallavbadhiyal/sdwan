ip = input("Please provide your ip address: ")
ip_address = ip.split(".")
size = len(ip_address)

def ip_velidation_check(ip_address):
    if size==4 and all (0 <= int(ip) <= 255 for ip in ip_address):
        return True
    else:    
        return False 

def ip_class_check(ip_address):
    if ip.startswith("10."):
     return ("Class A private ip")
    elif ip.startswith("172.") and (16 <= int(ip_address[1]) <= 31):
     return ("Class B private ip")
    elif ip.startswith("192.168."):
     return ("Class C private ip")
    elif (int(ip_address[0]) <= 126):
     return ("this is a class A public ip")
    elif (127 <= int(ip_address[0]) <= 191):
     return ("this is a class B public ip")
    elif (192 <= int(ip_address[0]) <= 223):
     return ("this is a class C public ip")
    elif (224 <= int(ip_address[0]) <= 239):
     return("this is a class D ip and Reserve for multi-tasking")
    elif (240 <= int(ip_address[0]) <= 254):
     return("this is a class E ip and reserved for research and Development Purposes")

if (ip_velidation_check(ip_address)) == True:
 print(f"{ip} is a Valid IP")
 print(ip_class_check(ip_address))
else:
  print(f"\n{ip} is not a Valid IP")