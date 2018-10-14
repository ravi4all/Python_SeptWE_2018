def temp_conv(cel):
    return 9/5 * cel + 32
# print(temp_conv(34.5))
temp = [34.5,33.4,32.6,37.8,31.4,36.5]
# temp_conv(temp)

# f = []
# for t in temp:
#     # print(temp_conv(t))
#     f.append(temp_conv(t))
# print(f)

# Alternatively
# f = list(map(temp_conv, temp))
# print(f)

def myMap(func, iter):
    data = []
    for i in iter:
        data.append(func(i))
    return data

myMap(temp_conv, temp)
# map(temp_conv, temp)