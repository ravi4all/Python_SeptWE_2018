file = open('dhoni.mp4', 'rb')

data = file.read()
# print(data)

file.close()

file = open('dhoni_1.mp4', 'wb')
file.write(data)
file.close()