def sum(b, c, *var, **kvar):
    # s = a + b
    # return s
    print(b)
    sum = 0
    for item in var:
        sum = sum + item
    # print(sum)
    print(kvar)
    return sum


# p = 20
# q = 50

x = sum("NewDelhi", 20,30,40,50, addr="Delhi", name="NetG")
print(x)

# p = 100
# q = 50

# x = sum(p,q)
# print(x)

# p = 200
# q = 100

# x = sum(p,q)
# print(x)