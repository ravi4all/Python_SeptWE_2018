usermessage = input("Enter your message : ")
usermessage = usermessage.lower()
# Logical Operators - AND, OR, NOT
if usermessage == "hello" or usermessage == "hi" or usermessage == "hey":
    print("Hi there")
elif usermessage == "bye":
    print("Bye User")
else:
    print("I don't understand")