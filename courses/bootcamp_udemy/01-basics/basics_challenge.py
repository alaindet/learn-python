"""
https://www.udemy.com/course/master-python-programming-complete-python-bootcamp/learn/lecture/35718818#overview
"""

from math import isclose

# Challenge 1
a = 1
b = 1.0
c = True
d = 'hello'
e = [1, 2, 3]

# Challenge 2
print(type(a), a) # <class 'int'> 1
print(type(b), b) # <class 'float'> 1.0
print(type(c), c) # <class 'bool'> True
print(type(d), d) # <class 'str'> hello
print(type(e), e) # <class 'list'> [1, 2, 3]

# Challenge 3


# Change this script so that it follows the Python naming and style conventions
# described in PEP8 (https://peps.python.org/pep-0008/)

my_name = 'Andrei'
value = 100

# This is 
# an example of a multiline
# comment in Python.

str = 'Hello'
print('Hello')


# Challenge 7
revenue = 45_897_513
profit = revenue * 0.127
print(format(profit, '.2f')) # 5828984.15

# Challenge 8

a = 0.1
b = 0.3

# Wrong
# print(a * 3 == b) # => False

# Correct
print(isclose(a * 3, b, abs_tol = 0.001)) # True
