'''
Rules to define variable name : 
- only underscore is allowed
- variable name cannot start with number
- numbers are allowed after any character
- reserved keywords cannot be name of variables
Keywords in python - or, and, not, is, in, for etc
'''

a = 10
b = 12
c = a + b

#print("Sum is",c)

#print("Sum of", a, "and", b, "is", c)

# %d - int, %s - str, %f - float
#print("Sum of %d and %d is %d"%(a,b,c))

#print("Sum of {} and {} is {}".format(a,b,c))

print(f"Sum of {a} and {b} is {c}")
