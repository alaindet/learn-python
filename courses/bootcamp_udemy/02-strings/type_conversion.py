# milesInput = input('Enter miles: ')
# print(type(milesInput)) # <class 'str'>
# miles = float(milesInput)
# kilometers = miles * 1.609
# print('In kilometers:', kilometers)

a = 1
print(type(a)) # <class 'int'>
a_float = float(a)
print(type(a_float)) # <class 'float'>

b = 2.8
print(type(b)) # <class 'float'>
b_int = int(b)
print(type(b_int), b_int) # <class 'int'> 2

c = '3.0'
print(type(c)) # <class 'str'>
c_float = float(c)
print(type(c_float), c_float) # <class 'float'> 3.0

#  c_int = int(c) # Raises a ValueError!

d = 'hello'
# d_float = float(d) # Raises a ValueError!

# This causes havoc since "str" is a reserved keyword for Python
# Later, any explicit or implicit use of the native "str" class will break!
str = 'redeclaring-builtin-str'
# a = str(123) # Raises a TypeError!
