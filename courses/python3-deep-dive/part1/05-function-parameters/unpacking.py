"""
Any iterable is a "packed" value that can be unpacked. These include
- Lists
- Tuples
- Strings
- Sets
- Dictionaries
"""

# Unpacking a list
a, b, c = [1, 2, 3]
# ^^^^^------------ this is a tuple
#---------^^^^^^^^^ this is a list

# Unpacking a tuple
a, b, c = 10, 20, 30

# Unpacking a string
a, b, c = 'xyz'
print('a string:', a) # x
print('b string:', b) # y
print('c string:', c) # z

try:
    a, b = 'xyz'
except ValueError:
    print('You cannot unpack 3 characters into 2 variables')

# Swapping via unpacking without a temporary variable
# What happens is: Python creates the (b, a) tuple on the right in memory
# Then, is deconstructs it and assigns it to a and b accordingly
a, b = 10, 20 # Impropertly defined "Parallel assignment"
a, b = b, a
print('swap: a:', a) # 20
print('swap: b:', b) # 10

# Unpacking a dictionary
dd = {'foo': 1, 'bar': 2, 'baz': 3}

# Straight unpacking gives you keys
# WARNING: ordering in keys is not guaranteed
a, b, c = dd
print('dict keys: a:', a) # foo
print('dict keys: b:', b) # bar
print('dict keys: c:', c) # baz

# Unpack dict values
a, b, c = dd.values()
print('dict values: a:', a) # 1
print('dict values: b:', b) # 2
print('dict values: c:', c) # 3

# Unpack dict key-value pairs as tuples
a, b, c = dd.items()
print('dict items: a:', a) # ('foo', 1)
print('dict items: b:', b) # ('bar', 2)
print('dict items: c:', c) # ('baz', 3)

# Unpacking and looping
# Prints
# key=foo, value=1
# key=bar, value=2
# key=baz, value=3
for key, value in dd.items():
    print(f'key={key}, value={value}')

# Unpacking a set
# WARNING: As in dictionaries, sets do not have guaranteed ordering for keys
s = {'a', 'b', 'c'}
a, b, c = s
print('set: a', a) # a
print('set: b', b) # b
print('set: c', c) # c

# Printing it multiple times can give different ordering
s = {'q', 'u', 'i', 'c', 'k'}
print(s) # {'c', 'q', 'u', 'k', 'i'}
# Second try prints, for example: {'c', 'i', 'q', 'k', 'u'}

# Unpacking a mixed tuple
a, b, c = 10, {1, 2}, ['a', 'b']
print('mixed tuple: a:', a) # 10
print('mixed tuple: b:', b) # {1, 2}
print('mixed tuple: c:', c) # ['a', 'b']

# Creating a 1-element tuple

# Not like this!
a = (42)
print(a, type(a)) # 42 <class 'int'>

# But like this!
a = (42,)
# a = 42, # This is fine too, but using parentheses is more common
print(a, type(a)) # (42,) <class 'tuple'>