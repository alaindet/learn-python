"""\
NameError
https://docs.python.org/3/library/exceptions.html#NameError
Raised when a local or global name is not found
"""
try:
    print(hello) # <-- This variable does not exist
except NameError as err:
    print('NameError:', err)
    # NameError: name 'hello' is not defined


"""\
TypeError
https://docs.python.org/3/library/exceptions.html#TypeError
Raised when an operation or function is applied to an object of inappropriate
type
"""
try:
    print(123 + 'hello')
except TypeError as err:
    print('TypeError:', err)
    # TypeError: unsupported operand type(s) for +: 'int' and 'str'


"""\
ValueError
https://docs.python.org/3/library/exceptions.html#ValueError
Raised when an operation or function receives an argument that has the right
type, but an inappropriate value
"""
try:
    nums = (1, 2, 3, 3, 3)
    print(nums.index(42))
except ValueError as err:
    print('ValueError:', err)
    # ValueError: tuple.index(x): x not in tuple


"""\
KeyError
https://docs.python.org/3/library/exceptions.html#KeyError
Raised when a mapping (dictionary) key is not found in the set of existing keys
"""
try:
    person = {'name': 'Alice', 'age': 80}
    person.pop('missingkey')
except KeyError as err:
    print('KeyError:', err)
    # KeyError: 'missingkey'


"""\
IndexError
https://docs.python.org/3/library/exceptions.html#IndexError
Raised when a sequence subscript is out of range
"""
try:
    nums = [1, 2, 3, 4]
    print(nums[42])
except IndexError as err:
    print('IndexError:', err)
    # IndexError: list index out of range


"""\
AttributeError
https://docs.python.org/3/library/exceptions.html#AttributeError
Raised when an attribute reference or assignment fails
"""
try:
    'foo'.salute()
except AttributeError as err:
    print('AttributeError:', err)
    # AttributeError: 'str' object has no attribute 'salute'