ip = input("Enter your ip")
ip = ip.split('.')
# print(ip)

flag = True
if len(ip) == 4 and int(ip[0]) != 0:
    for item in ip:
        if not (int(item)>= 0 and int(item) <=255):
            flag = False
            break
    if flag == True:
        print("Given ip is having valid octets")
    else:
        print("Invalid IP octet")
else:
    print("Not valid ip")
    

        