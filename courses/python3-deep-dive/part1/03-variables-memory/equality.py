"""
- Identity means two objects have the same memory address
- Identity is asserted via the "is" operator
- Equality means two objects have the same value
- Equality is asserted via the "==" operator
"""

def desc(a, b):
    identical = a is b
    equal = a == b
    print(f'Identical? {identical} Equal? {equal}')

# For primitive values, objects with the same value have also the same address
a = 42
b = 42
desc(a, b) # Identical? True Equal? True

# For compound values, objects with the same value CAN and usually have a
# DIFFERENT address
c = [1, 2, 3]
d = [1, 2, 3]
desc(c, d) # Identical? False Equal? True

# Negations
if a is not b:
    print('a is not b')
else:
    print('a is b')

if a != b:
    print('a is not equal to b')
else:
    print('a is equal to b')

# This is a bit surprising: Python figures e and f are of different number types
# but still compares them
e = 10
f = 10.0
desc(e, f) # Identical? False Equal? True

# Variable "e" became a complex number, but comparison with "f" is still true
e = e + 0j
desc(e, f)