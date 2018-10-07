# Nested Loops
'''
for i in range(5):
    print("I is",i)
    for j in range(5):
        print("J is",j)
'''

'''
*
**
***
****
*****
'''

# for i in range(5):
#     for j in range(i+1):
#         print('*', end='')
#     print()

# for i in range(6):
#     print(' ' * (6-i) + '*' * (2*i + 1))

# for i in range(6):
#     for j in range(6-i):
#         print(' ', end='')
#     for k in range(2*i + 1):
#         print('*', end='')
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j, end='')
#     print()

# for i in range(1,6):
#     for j in reversed(range(1,i+1)):
#         print(j, end='')
#     print()

for i in range(1,6):
    for j in range(i+1,0,-1):
        print(j, end='')
    print()