# Global Variables
a = 10
b = 12
def add():
    # Local Variables
    x = 10
    y = 12
    global z
    z = x + y
    print("Sum is",z)

add()
# print(a+b)
print(z)