Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = "hello world this is python programming"
>>> x[0]
'h'
>>> x[10]
'd'
>>> x[-1]
'g'
>>> x[-5]
'm'
>>> x[20]
'p'
>>> x[19]
' '
>>> x[0:20]
'hello world this is '
>>> x[20:0]
''
>>> x[0:20:1]
'hello world this is '
>>> x[20:0:-1]
'p si siht dlrow olle'
>>> x[20:-1:-1]
''
>>> x[20:-1:1]
'python programmin'
>>> x[20:0:-1]
'p si siht dlrow olle'
>>> x[-1:-20]
''
>>> x[-1:-20:-1]
'gnimmargorp nohtyp '
>>> x[:]
'hello world this is python programming'
>>> x[0:20:2]
'hlowrdti s'
>>> x[::-1]
'gnimmargorp nohtyp si siht dlrow olleh'
>>> x[20::-1]
'p si siht dlrow olleh'
>>> x.capitalize()
'Hello world this is python programming'
>>> x.upper()
'HELLO WORLD THIS IS PYTHON PROGRAMMING'
>>> x.lower()
'hello world this is python programming'
>>> x.swapcase()
'HELLO WORLD THIS IS PYTHON PROGRAMMING'
>>> x.title()
'Hello World This Is Python Programming'
>>> x.find('y')
21
>>> x.count('o')
4
>>> x.find('o')
4
>>> x.rfind('o')
29
>>> x.find('o',5)
7
>>> x.replace('hello', 'bye')
'bye world this is python programming'
>>> x
'hello world this is python programming'
>>> x.center(60)
'           hello world this is python programming           '
>>> len(x)
38
>>> x.center(40)
' hello world this is python programming '
>>> x.center(50)
'      hello world this is python programming      '
>>> x.center(50, '#')
'######hello world this is python programming######'
>>> x.isalpha()
False
>>> x.isdecimal()
False
>>> x.isdigit()
False
>>> x.islower()
True
>>> x.split()
['hello', 'world', 'this', 'is', 'python', 'programming']
>>> x.split('t')
['hello world ', 'his is py', 'hon programming']
>>> 
