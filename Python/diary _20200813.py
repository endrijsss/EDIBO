Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> if type(a) == int:
	print("labi")

	
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    if type(a) == int:
NameError: name 'a' is not defined
>>> 
>>> a=10
>>> if type(a) == int:
	print("labi")

	
labi
>>> a=5.5
>>> if type(a) == int:
	print("labi")
else:
	print("slikti")

	
slikti
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("arī labi")
else:
	print("slikti")

	
arī labi
>>> a="sgdsgses"
>>> >>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("arī labi")
else:
	print("slikti")
	
SyntaxError: invalid syntax
>>> a = 10
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("arī labi")
else:
	print("slikti")

	
labi
>>> a="fasfasfas"
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("arī labi")
else:
	print("slikti")

	
slikti
>>> a = 10
>>> 
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("arī labi bet nekad netiks redzets")
else:
	print("slikti")

	
labi
>>> print("aaa\n bbbb\n cccc")
aaa
 bbbb
 cccc
>>> print("a
