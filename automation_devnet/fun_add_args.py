def addition_with_args(*args):
    temp = 0
    for item in args:
        temp = temp + item
    print(temp)

addition_with_args(1,2,3,4,5,6,7,8,9)