# lambda - anonymous function

# def add(x,y):
#     return x + y

# add = lambda x,y : x + y
# print(add(3,4))

temp = [34.5,33.4,32.6,37.8,31.4,36.5]
print(list(map(lambda c : 9 / 5 * c + 32, temp)))

even = list(filter(lambda e : e % 2 == 0, [i for i in range(1,51)]))
print(even)