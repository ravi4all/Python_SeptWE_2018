# input() - by default it takes type of data as string
userName = input("Enter your name : ")

message = "Hello "+userName
print(message)

# we need integer type of data
# so we have to type cast the data
#num_1 = int(input("Enter first number : "))
#num_2 = int(input("Enter second number : "))

num_1 = input("Enter first number : ")
num_2 = input("Enter second number : ")

result = int(num_1) + int(num_2)
print("Sum is",result)
