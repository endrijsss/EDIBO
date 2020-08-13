Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruit = 'banana'
>>> letter = fruit[1]
>>> print(letter)
a
>>> letter = fruit(0)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    letter = fruit(0)
TypeError: 'str' object is not callable
>>> print(letter)
a
>>> letter = fruit[0]
>>> print(letter)
b
>>> fruit[0] + fruit[1]
'ba'
>>> fruit[1] + fruit[3] + fruit[5]
'aaa'
>>> fruit[N-1]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    fruit[N-1]
NameError: name 'N' is not defined
>>> N = len(fruit)
>>> N
6
>>> fruit(N-1)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    fruit(N-1)
TypeError: 'str' object is not callable
>>> fruit[N-1]
'a'
>>> lenght = len(fruit)
>>> last = fruit(length)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    last = fruit(length)
NameError: name 'length' is not defined
>>> last = fruit[length]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    last = fruit[length]
NameError: name 'length' is not defined
>>> last = fruit[length]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    last = fruit[length]
NameError: name 'length' is not defined
>>> last = fruit[length-1]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    last = fruit[length-1]
NameError: name 'length' is not defined
>>> length = len(fruit)
>>> last = fruit[length]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    last = fruit[length]
IndexError: string index out of range
>>> last = fruit[length-1]
>>> print(last)
a
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1

	
b
a
n
a
n
a
>>> fruit = 'abcdef'
>>> N
6
>>> N-1
5
>>> N-13
-7
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1

	
>>> 
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1

	
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1

	
>>> fruit[1] + fruit[3] + fruit[5]
'bdf'
>>> last = fruit[length-1]
>>> last = fruit[length-1]
>>> https://www.py4e.com/html3/06-strings
SyntaxError: invalid syntax
>>> index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1
    
SyntaxError: multiple statements found while compiling a single statement
>>> index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1
    
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1

	
a
b
c
d
e
f
>>> 
