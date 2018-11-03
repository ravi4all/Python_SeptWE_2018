def atm():
    total = 10000
    pin = int(input("Enter your pin : "))
    # When condition will be false it will raise error
    assert (pin == 1234), "Invalid Pin"
    print("Welcome User")

    withdraw = int(input("Enter the amount : "))
    assert (withdraw > total), "Insufficient Balance"
    total -= withdraw

    print("Transaction Successfull")
    print("Remaining balance is",total)

try:
    atm()
except AssertionError as err:
    print(err)