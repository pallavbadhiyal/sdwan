ip = input("Enter an IP: ")

if ip.startswith('10.') or (ip.startswith('172.') and float(ip[4:7]) >= 16 and float(ip[4:7]) <= 31) or ip.startswith('192.168.'):
    print('this is a private IP')
else:
    print('not a private IP')
