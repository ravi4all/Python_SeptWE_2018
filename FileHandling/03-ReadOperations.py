with open('file_1.txt') as file:
    # data = file.read()

    # data = file.read(10)

    # data = file.readline()

    # data = file.readlines()

    file.seek(10)
    data = file.read()
    print(data)