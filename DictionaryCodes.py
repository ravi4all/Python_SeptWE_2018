Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [12,14,15,16,18,21,22]
>>> a[0] = 99
>>> a
[99, 14, 15, 16, 18, 21, 22]
>>> students = ['ram','shyam','moht','amit']
>>> students[2] = 'mohit'
>>> students
['ram', 'shyam', 'mohit', 'amit']
>>> students = ('ram','shyam','moht','amit')
>>> students[0]
'ram'
>>> students[2] = 'mohit'
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    students[2] = 'mohit'
TypeError: 'tuple' object does not support item assignment
>>> students[0:2]
('ram', 'shyam')
>>> students = {'name':}
SyntaxError: invalid syntax
>>> students = {'name':'Ram', 'grade':'A', 'marks':86}
>>> students[0]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    students[0]
KeyError: 0
>>> students['name']
'Ram'
>>> students.keys()
dict_keys(['name', 'grade', 'marks'])
>>> students.values()_
SyntaxError: invalid syntax
>>> students.values()
dict_values(['Ram', 'A', 86])
>>> students.items()
dict_items([('name', 'Ram'), ('grade', 'A'), ('marks', 86)])
>>> students['grade'] = 'A+'
>>> students
{'name': 'Ram', 'grade': 'A+', 'marks': 86}
>>> students['hobby'] = 'Cricket'
>>> students
{'name': 'Ram', 'grade': 'A+', 'marks': 86, 'hobby': 'Cricket'}
>>> del students['marks']
>>> students
{'name': 'Ram', 'grade': 'A+', 'hobby': 'Cricket'}
>>> students = {"name":['Ram','Shyam','Gopal','Mohit','Amit'],"hobby":['cricket','football','cricket','football','shooting'],"marks":[87,67,76,88,56]}
>>> students
{'name': ['Ram', 'Shyam', 'Gopal', 'Mohit', 'Amit'], 'hobby': ['cricket', 'football', 'cricket', 'football', 'shooting'], 'marks': [87, 67, 76, 88, 56]}
>>> students['name']
['Ram', 'Shyam', 'Gopal', 'Mohit', 'Amit']
>>> students['name'][0]
'Ram'
>>> students['marks']
[87, 67, 76, 88, 56]
>>> students['name'][0], students['marks'][0], students['hobby'][0]
('Ram', 87, 'cricket')
>>> for i in range(5):
	print(students['name'][i], students['marks'][i], students['hobby'][i])

	
Ram 87 cricket
Shyam 67 football
Gopal 76 cricket
Mohit 88 football
Amit 56 shooting
>>> 
