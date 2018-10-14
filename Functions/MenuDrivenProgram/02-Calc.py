def calc(x,y,opr):
    expression = x + opr + y
    result = eval(expression)
    print("Result is",result)

print("""
1. Add
2. Sub
3. Mul
4. Div
""")

userCh = input("Enter your choice : ")

num_1 = input("Enter first number : ")
num_2 = input("Enter second number : ")

operations = {
    "1" : "+",
    "2" : "-",
    "3" : "*",
    "4" : "/"
}

opr = operations.get(userCh)
calc(num_1, num_2, opr)