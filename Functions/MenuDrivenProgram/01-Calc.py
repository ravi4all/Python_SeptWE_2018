def add(x,y):
    z = x + y
    print("Sum is",z)

def sub(x,y):
    z = x - y
    print("Diff is",z)

def mul(x,y):
    z = x * y
    print("Mul is",z)

print("""
1. Add
2. Sub
3. Mul
""")

userCh = input("Enter your choice : ")

num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))

operations = {
    "1" : add,
    "2" : sub,
    "3" : mul
}
operations.get(userCh)(num_1, num_2)