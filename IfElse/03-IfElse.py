import webbrowser
from datetime import datetime
import os, random

helloIntent = ['hello','hi','hey','hie']
date = ['date please', 'date today', 'todays date', 'date']
time = ['time please', 'please time', 'time']

while True:
    usermessage = input("Enter your message : ")
    usermessage = usermessage.lower()

    # Membership Operators - in, not in
    if usermessage in helloIntent:
        print("Hi there")
    elif usermessage == "bye":
        print("Bye User")
        break
    elif usermessage.startswith('open'):
        web = usermessage.split()[1]
        webbrowser.open(web+'.com')
    elif usermessage in date:
        d = datetime.now().date()
        print("Date is",d)
    elif usermessage in time:
        t = datetime.now().time()
        print("Time is",t.strftime("%H:%M:%S %P"))
    elif usermessage.startswith("play"):
        path = r'C:\Users\asus\Music'
        os.chdir(path)
        songs = os.listdir(path)
        currentSong = random.choice(songs)
        os.startfile(currentSong)
    else:
        print("I don't understand")
