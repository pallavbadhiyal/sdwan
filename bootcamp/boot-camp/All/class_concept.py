
class calc:
    # def __new__():
    #     pass
    def __init__(self, x, y, z):
        # print(a)
        self.a = x
        self.b = y

    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    @staticmethod
    def mul(l, m):
        return l * m

obj2 = calc(10, 20, 30)

s = obj2.add()
print(s)

m = obj2.sub()
print(m)

z = obj2.mul(4, 5)
print(z)
# obj3 = calc(100, 200)

# s = obj3.add()
# print(s)

# m = obj3.sub()
# print(m)

# s = calc.sub(10,20)
# print(s)

# obj1 = calc()

# s = obj1.add(10,20)
# print(s)

# obj2 = calc()

# s = obj2.add(100,200)
# print(s)

# s = obj2.add(100,200)
# print(s)

# m = obj2.sub(100,200)
# print(m)