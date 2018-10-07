Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = "hello this is python programming for machine learning"
>>> a
'hello this is python programming for machine learning'
>>> len(a)
53
>>> a.capitalize()
'Hello this is python programming for machine learning'
>>> a.upper()
'HELLO THIS IS PYTHON PROGRAMMING FOR MACHINE LEARNING'
>>> a.lower()
'hello this is python programming for machine learning'
>>> a.count('i')
5
>>> a.find('i')
8
>>> a.rfind('i')
50
>>> a.find('i',9)
11
>>> a.find('i',0,5)
-1
>>> a.replace('hello', 'bye')
'bye this is python programming for machine learning'
>>> a
'hello this is python programming for machine learning'
>>> a.find('p')
14
>>> a.find('pr')
21
>>> a.center(30)
'hello this is python programming for machine learning'
>>> a.center(40)
'hello this is python programming for machine learning'
>>> a.center(50)
'hello this is python programming for machine learning'
>>> a.center(54)
'hello this is python programming for machine learning '
>>> a.center(58)
'  hello this is python programming for machine learning   '
>>> a.center(60)
'   hello this is python programming for machine learning    '
>>> a.center(60,'*')
'***hello this is python programming for machine learning****'
>>> a.isdigit()
False
>>> type(a)
<class 'str'>
>>> isinstance(a, str)
True
>>> 
