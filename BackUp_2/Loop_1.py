n = int(input("Enter the number : "))

'''
print("2 x 1 = 2")
print("2 x 2 = 4")
print("2 x 3 = 6")
print("2 x 4 = 8")
print("2 x 5 = 10")
'''
for i in range(1,11):
    print("{} x {} = {}".format(n,i,n*i))

for i in reversed(range(10)):
    print(i)