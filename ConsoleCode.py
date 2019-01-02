Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 12
>>> b = "hello"
>>> bricks = [3,4,5,7,8,9,12,23,5,78,13]
>>> students = ["ram","shyam",'john','mike','tom']
>>> students[0]
'ram'
>>> students[3]
'mike'
>>> students[-1]
'tom'
>>> player = ['jump','punch','kick','walk','run','swim']
>>> player[4]
'run'
>>> player.append('gun')
>>> player
['jump', 'punch', 'kick', 'walk', 'run', 'swim', 'gun']
>>> player.append('fly')
>>> player
['jump', 'punch', 'kick', 'walk', 'run', 'swim', 'gun', 'fly']
>>> students.append('Ravi')
>>> students
['ram', 'shyam', 'john', 'mike', 'tom', 'Ravi']
>>> even = []
>>> even.append(2)
>>> even.append(4)
>>> even.append(6)
>>> even
[2, 4, 6]
>>> even = []
>>> 4 / 2
2.0
>>> 4 % 2
0
>>> for i in range(1,21):
	if i % 2 == 0:
		print("Even Number",i)
	else:
		print("Odd Number",i)

		
Odd Number 1
Even Number 2
Odd Number 3
Even Number 4
Odd Number 5
Even Number 6
Odd Number 7
Even Number 8
Odd Number 9
Even Number 10
Odd Number 11
Even Number 12
Odd Number 13
Even Number 14
Odd Number 15
Even Number 16
Odd Number 17
Even Number 18
Odd Number 19
Even Number 20
>>> for i in range(1,21):
	if i % 2 == 0:
		print(i)

		
2
4
6
8
10
12
14
16
18
20
>>> even = []
>>> for i in range(1,21):
	if i % 2 == 0:
		even.append(i)

		
>>> even
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> even = []
>>> odd =[]
>>> for i in range(1,21):
	if i % 2 == 0:
		even.append(i)
	else:
		odd.append(i)

		
>>> even
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> odd
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
>>> even.insert(3,99)
>>> even
[2, 4, 6, 99, 8, 10, 12, 14, 16, 18, 20]
>>> even.pop()
20
>>> even.pop()
18
>>> even
[2, 4, 6, 99, 8, 10, 12, 14, 16]
>>> even.pop(3)
99
>>> even
[2, 4, 6, 8, 10, 12, 14, 16]
>>> even.remove(5)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    even.remove(5)
ValueError: list.remove(x): x not in list
>>> students
['ram', 'shyam', 'john', 'mike', 'tom', 'Ravi']
>>> students.remove('mike')
>>> students
['ram', 'shyam', 'john', 'tom', 'Ravi']
>>> powerup = ['superjump','superpunch','superfast']
>>> player
['jump', 'punch', 'kick', 'walk', 'run', 'swim', 'gun', 'fly']
>>> player + powerup
['jump', 'punch', 'kick', 'walk', 'run', 'swim', 'gun', 'fly', 'superjump', 'superpunch', 'superfast']
>>> player
['jump', 'punch', 'kick', 'walk', 'run', 'swim', 'gun', 'fly']
>>> player.extend(powerup)
>>> player
['jump', 'punch', 'kick', 'walk', 'run', 'swim', 'gun', 'fly', 'superjump', 'superpunch', 'superfast']
>>> students = [['ram','shyam','john','mike','tom','tyson'],[50,54,56,76,87,85],['football','cricket','hockey','cricket','shooting','cricket']]
>>> students
[['ram', 'shyam', 'john', 'mike', 'tom', 'tyson'], [50, 54, 56, 76, 87, 85], ['football', 'cricket', 'hockey', 'cricket', 'shooting', 'cricket']]
>>> students[0]
['ram', 'shyam', 'john', 'mike', 'tom', 'tyson']
>>> students[1]
[50, 54, 56, 76, 87, 85]
>>> students[2]
['football', 'cricket', 'hockey', 'cricket', 'shooting', 'cricket']
>>> students[0][0]
'ram'
>>> students[2][1]
'cricket'
>>> students[0][0], students[1][0], students[2][0]
('ram', 50, 'football')
>>> len(students)
3
>>> len(students[0])
6
>>> for i in range(len(students[0])):
	print(students[0][i], students[1][i], students[2][i])

	
ram 50 football
shyam 54 cricket
john 56 hockey
mike 76 cricket
tom 87 shooting
tyson 85 cricket
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> players
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    players
NameError: name 'players' is not defined
>>> player
['jump', 'punch', 'kick', 'walk', 'run', 'swim', 'gun', 'fly', 'superjump', 'superpunch', 'superfast']
>>> player[0]
'jump'
>>> player[0:5]
['jump', 'punch', 'kick', 'walk', 'run']
>>> player[0:10:2]
['jump', 'kick', 'run', 'gun', 'superjump']
>>> player[0:10:3]
['jump', 'walk', 'gun', 'superpunch']
>>> 
