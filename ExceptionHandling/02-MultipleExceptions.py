try:
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))

    c = a + b
    d = a - b
    e = a / b
    f = a * b
    print(c, d, e, f)

except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid Input, Only digits are allowed")
except BaseException as ex:
    print("Some other error - ",ex)