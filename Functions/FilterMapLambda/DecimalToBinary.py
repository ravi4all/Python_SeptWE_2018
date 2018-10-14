def decimalToBin(num):
    if num > 1:
        decimalToBin(num // 2)
    print(num % 2, end='')

# decimalToBin(17)

numbers = [12,34,11,5,23,13,24,26,55]
for n in numbers:
    decimalToBin(n)
    print()