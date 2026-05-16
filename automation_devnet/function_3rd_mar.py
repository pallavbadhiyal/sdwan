def multiplication(x,y,*list, **key_dic):
    print(x)
    print(y)
    print(list)
    print(key_dic)

    for data in list :
        m = data * m
        print(m)



list = [3,4,5]
multiplication(1,2, *list, a = 6, b = 7)