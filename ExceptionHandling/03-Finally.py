import io
try:
    file = open('demo_1.txt', 'w')
    print("File Open")
    data = ["hello world","bye world"]
    file.write(data[0])
except io.UnsupportedOperation as ex:
    print('File is open in different mode')
except BaseException as ex:
    print("Error",ex)
else:
    print("Else executed")
finally:
    print("Finally executed")
    file.close()
    print("File Closed...")