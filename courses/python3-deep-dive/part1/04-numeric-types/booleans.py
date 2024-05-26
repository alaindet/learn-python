"""
# Booleans

In Python, the boolean primitive type is "bool" and is a subclass of int
Two constants are pre-defined, True (1) and False (0)
"""

print('issubclass(bool, int)', issubclass(bool, int))  # True

# Booleans work with == as well as "is" since all boolean variables point to the
# same memory address of either the True constant of the False constant
a = 3 > 2  # This is assigned to the memory address of the constant True
b = True

print('a == b', a == b)  # True
print('a is b', a is b)  # True

one = 1
zero = 0
yes = True
no = False

# "Weird but ok" sentences
print('\n"Weird-but-ok" sentences\n------------------------')
print('True + True', True + True)  # 2
print('True > False', True > False)  # True
print('True * False', True * False)  # 0
print('False is False', False is False)  # True
print('True == 1', True == 1)  # True
print('yes is one', yes is one)  # False <-- Notice this
print('False == 0', False == 0)  # True
print('no is zero', no is zero)  # False <-- Notice this
print('-True', -True)  # -1

# WARNING
# True and 1 have the same value, but they have different addresses
# Same: False and 0 have the same value, but different addresses, so
# False is 0 fails

"""
## Truthyness

Every single object in Python has a "truth value" or "truthyness", which means
anything can be converted to a boolean by default (and be used in if statements).

By conventions, EVERYTHING is True except for these few things that are False
- Empty list `[]`
- Empty tuples `()`
- Empty dictionaries `{}`
- Empty sets `set()`
- Empty strings `''`
- Empty ranges `range(0)`
- `0`
- `0.0`
- `0j`
- `None`
- `False`
- Any object implementing `__bool__()` and returning False
- Any object implementing `__len__()` and returning `0`
"""


class WithDunderBool():
    def __bool__(self):
        return False


class WithDunderLen():
    def __len__(self):
        return 0


print('\nTruthyness\n----------')

# The obvious ones
print('bool(None)', bool(None))  # False
print('bool(False)', bool(False))  # False

# The empty sequences, because they're length is zero
print('bool([])', bool([]))  # False
print('bool(list())', bool(list()))  # False
print('bool(())', bool(()))  # False
print('bool(tuple())', bool(tuple()))  # False
print('bool({})', bool({}))  # False
print('bool(dict())', bool(dict()))  # False
print('bool(set())', bool(set()))  # False
print('bool(range(0))', bool(range(0)))  # False

# The empty string
print('bool(\'\')', bool(''))  # False

# The zeros
print('bool(0)', bool(0))  # False
print('bool(0.0)', bool(0.0))  # False
print('bool(0j)', bool(0j))  # False

# Object implementing __bool__ and __len__
print('bool(WithDunderBool())', bool(WithDunderBool()))  # False
print('bool(WithDunderLen())', bool(WithDunderLen()))  # False
