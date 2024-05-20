def desc(the_var, the_message = None):
    address = hex(id(the_var))

    if the_message is not None:
        print(the_message, address)
    else:
        print(address)

# Notice that a and b have a SHARED REFERENCE to the literal value 42, which
# even has the same address as a and b
a = 42
b = 42
desc(a, 'a') # a 0x7ffc3201ced8
desc(b, 'b') # b 0x7ffc3201ced8
desc(42, '42') # 42 0x7ffc3201ced8

# The reason why "a" and "b" have the same reference, is because the CPython runtime
# creates and caches number objects (in old versions, from -6 to 256), for performance
# given how how much these numbers are user
a = 999999
b = 999999
print(a is b) # True

# Here, however c and d do NOT share a reference to [1, 2, 3] since changing
# a mutable object does not change its address and leads to unwanted side effects
c = [1, 2, 3]
d = [1, 2, 3]
desc(c, 'c') # c 0x151171ed880
desc(d, 'd') # d 0x151171ed100

# Here, we manually created a shared reference, meaning "e" and "f" point to the
# same mutable object
e = [1, 2, 3]
f = e
desc(e, 'e') # e 0x1b1523e7100
desc(f, 'f') # f 0x1b1523e7100

"""
The None object is an immutable object with a shared reference among all
variables set to None

- None is usually used to test if a variable exists and/or has been assigned
"""

if a is not None:
    print('a has a value')