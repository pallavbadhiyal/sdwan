def addition_with_args(*args):
    temp = 0
    for item in args:
        temp += int(item)
    print(temp)

var = input("Enter number to add with comma saprated ")
var_list = var.split(",")
print(var_list)
addition_with_args(*var_list)