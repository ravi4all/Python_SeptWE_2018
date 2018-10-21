helloIntent = []
byeIntent = []

chat = True
while chat:
    msg = input("Enter your message : ")

    if msg == 'hello':
        print("hello")
    elif msg == 'bye':
        print('bye')
        chat = False
    else:
        print("I don't understand")