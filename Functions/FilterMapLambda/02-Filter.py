def even(num):
    return num % 2 == 0

# print(even(12))
numbers = [12,23,56,14,16,21,26,68,32]

# for n in numbers:
#     print(even(n))

e = list(filter(even, numbers))
print(e)