ip = input("Enter an IP: ")

if ip.startswith('10.'):
    print('This is Class A IP')
elif ip.startswith('172.') and float(ip[4:7]) >= 16 and float(ip[4:7]) <= 31:
    print('this is class B IP')
elif ip.startswith('192.168.'):
    print('this is class C IP')
else:
    print('not a private IP')
