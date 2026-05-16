ip = input("Enter an IP: ")

test_ip = ip.split('.')
#print(test_ip)
#print(len(test_ip))
flag = True
for char in test_ip:
    if char.isdigit():
        if len(test_ip) == 4 and int(test_ip[0]) != 0:
            if int(char) >=0 and int(char) <= 255:
                continue
            else:
                flag = False
                break
        else:
            flag = False
            break
    else:
        print("provide integer numbers")
        flag = False
        break
# if len(test_ip) == 4 and int(test_ip[0]) != 0:
#     for char in test_ip:
#         # print(char)
#         # if char.isdigit() and int(char) >=0 and int(char) <= 255:
#         if int(char) >=0 and int(char) <= 255:
#             # if int(char) >=0 and int(char) <= 255:
#             #     # print(char)
#             #     continue
#             # else:
#             #     # print('invalid IP')
#             #     flag = False
#             #     break
#             continue
#         else:
#             # print("invalid IP")
#             flag = False
#             break
# else:
#     # print("invalid IP")
#     flag = False

tested_ip = ".".join(test_ip)

if flag == True:
    print(tested_ip + ' is a valid IP')
else:
    # print('It is an invalid IP')
    print(tested_ip + ' is not a valid IP')
#tested_ip = ".".join(test_ip)
#print(tested_ip + " is a valid IP")