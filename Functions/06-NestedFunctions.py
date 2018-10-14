def calc():
    x = 10
    y = 12
    def add():
        z = x + y
        return z

    def sub():
        z = x - y
        return z
    # print(add())
    # print(sub())
    return add, sub
x = calc()
print(x[0]())
# print(x())