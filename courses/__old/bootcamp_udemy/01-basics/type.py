"""
Python is dinamically typed, meaning type exists, but it's bound to runtime values
and it is not enforced on variables

Ex.: You can assign a string to a variable previously holding a number
"""

# type() returns the type of the literal value of the type of the value
# contained in a variable
print(type(10)) # Outputs: <class 'int'>
print(type('Hello')) # Outputs: <class 'str'>

# id() returns the address of a variable
a = 42
print(id(a)) # Outputs: 140730341058632
a = 43
print(id(a)) # Outputs: 140730341058664 (different!)

# ??? - Edge case
# Assigning the same value to the same variable does not change the variable's address
a = 42
print(id(a)) # Outputs: 140730341058632
a = 42
print(id(a)) # Outputs: 140730341058632 (same!)

a = 1
b = a
print(id(a)) # Outputs: 140730341057320
print(id(b)) # Outputs: 140730341057320 (same!)

# Complex types
class MyClass:
  x = 5
p1 = MyClass()
print(type(MyClass), type(p1)) # Outputs: <class 'type'> <class '__main__.MyClass'>

a = 123
print('id of constants')
print(id(a)) # Outputs: 140730341061224
print(id(123)) # Outputs: 140730341061224 (same!)
