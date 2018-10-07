Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [1,2,3,5,5,7,'hello', 10.4,True]
>>> b = (1,2,3,5,5,7,'hello', 10.4,True)
>>> a[0] = 100
>>> a
[100, 2, 3, 5, 5, 7, 'hello', 10.4, True]
>>> b[0] = 100
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    b[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> d = {'name':'Ram','company':'TCS','sal':30000}
>>> s = {2,4,5,6,8,3,2,4,5,8,9,2,2}
>>> s
{2, 3, 4, 5, 6, 8, 9}
>>> d
{'name': 'Ram', 'company': 'TCS', 'sal': 30000}
>>> d['dept'] = 'IT'
>>> d
{'name': 'Ram', 'company': 'TCS', 'sal': 30000, 'dept': 'IT'}
>>> x = {'list':a, 'tuple':b, 'set':s, 'dict':d}
>>> x
{'list': [100, 2, 3, 5, 5, 7, 'hello', 10.4, True], 'tuple': (1, 2, 3, 5, 5, 7, 'hello', 10.4, True), 'set': {2, 3, 4, 5, 6, 8, 9}, 'dict': {'name': 'Ram', 'company': 'TCS', 'sal': 30000, 'dept': 'IT'}}
>>> d['list']
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    d['list']
KeyError: 'list'
>>> x['list']
[100, 2, 3, 5, 5, 7, 'hello', 10.4, True]
>>> x['dict']
{'name': 'Ram', 'company': 'TCS', 'sal': 30000, 'dept': 'IT'}
>>> y = [x,a,b,s]
>>> y
[{'list': [100, 2, 3, 5, 5, 7, 'hello', 10.4, True], 'tuple': (1, 2, 3, 5, 5, 7, 'hello', 10.4, True), 'set': {2, 3, 4, 5, 6, 8, 9}, 'dict': {'name': 'Ram', 'company': 'TCS', 'sal': 30000, 'dept': 'IT'}}, [100, 2, 3, 5, 5, 7, 'hello', 10.4, True], (1, 2, 3, 5, 5, 7, 'hello', 10.4, True), {2, 3, 4, 5, 6, 8, 9}]
>>> 
