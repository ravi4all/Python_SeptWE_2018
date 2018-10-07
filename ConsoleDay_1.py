Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Sep_2018/PythonWE_Evening/02-Input.py 
Enter your name : ravi
Hello ravi
Enter first number : 12
Enter second number : 22
Sum is 34
>>> int('12' + '11')
1211
>>> x = "hello world"
>>> x = "hello this is python.\npython is general purpose\npython is interpreted"
>>> print(x)
hello this is python.
python is general purpose
python is interpreted
>>> x = """hello this is pythonpython is general purposepython is interpreted"""
>>> x = """hello this is python
python is general purpose
python is interpreted"""
>>> print(x)
hello this is python
python is general purpose
python is interpreted
>>> x = "hello "python""
SyntaxError: invalid syntax
>>> x = "hello 'python'"
>>> print(x)
hello 'python'
>>> x = 'hello "python"'
>>> print(x)
hello "python"
>>> path = "C:\new folder\abc\"
SyntaxError: EOL while scanning string literal
>>> path = r"C:\new folder\abc\"
SyntaxError: EOL while scanning string literal
>>> path = r"C:\new folder\abc"
>>> path = "C:\new folder\abc"
>>> import os
>>> os.chdir(path)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    os.chdir(path)
OSError: [WinError 123] The filename, directory name, or volume label syntax is incorrect: 'C:\new folder\x07bc'
>>> path = r"C:\new folder\abc"
>>> os.chdir(path)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    os.chdir(path)
FileNotFoundError: [WinError 3] The system cannot find the path specified: 'C:\\new folder\\abc'
>>> path = "C:\\new folder\\abc"
>>> x = "hello\nworld"
>>> print(x)
hello
world
>>> x = "hello\\nworld"
>>> print(x)
hello\nworld
>>> x = r"hello\nworld"
>>> print(x)
hello\nworld
>>> 
