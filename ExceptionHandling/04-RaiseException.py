def atm():
    total = 10000
    pin = int(input("Enter your pin : "))
    if pin == 1234:
        print("Welcome User")
    else:
        raise ValueError("Invalid Pin")

    withdraw = int(input("Enter the amount : "))
    if withdraw > total:
        raise ValueError("Insufficient Balance")
    else:
        total -= withdraw

    print("Transaction Successfull")
    print("Remaining balance is",total)

try:
    atm()
except ValueError as err:
    print(err)