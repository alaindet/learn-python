import string

"""
## Precedence

1. <, >, <=, >=, ==, !==, in, is
2. not
3. and
4. or

a < b or a > c and not x or y
__1________1_________________  1. comparisons    
___________________222_______  2. not
_______________333___________  3. and
______44_________________44__  4. or

Using parentheses and ignoring precedence
(a < b) or ((a > c) and (not x)) or y
"""

print('\nPrecedence\n----------')
print('True or True and False', True or True and False)  # True
print('(True or True) and False', (True or True) and False)  # False


"""
## Short-circuiting

When evaluating an expression with booleans, Python short-circuits if possible
"""

print('\nShort-circuiting\n----------------')

yep = True
nope = False

# Evalutes to False as soon as evaluating nope, since "and" already failed
if nope and yep:
    print('never happens')

# Evaluates to True as soon as evaluating yep, since "or" is satistied
if yep or nope:
    print('happens')

item = None
list = [1, 2, 3]

# Does not search, since item is None and bool(item) False, so "and" fails
if item and item in list:
    print('never happens')

a = 2
b = 0

# Alone, this raises a ZeroDivisionError!
try:
    if a/b > 0:
        print('a/b > 0')
    else:
        print('b is zero!')
except ZeroDivisionError as err:
    print(err)

# Thanks to short-circuiting, the "a/b > 0" part never evaluates
if b and a/b > 0:
    print('a/b > 0')
else:
    print('b is zero!')

name = 'Bob'
if name and name[0] in string.digits:
    print('Name should not start with a digit')

# Equivalent to
if name is not None and len(name) > 0 and name[0] in string.digits:
    print('Name should not start with a digit')


def get_a() -> int:
    print('call to get_a()')
    return 2


def get_b() -> int:
    print('call to get_b()')
    return 0


# Prints
# call to get_b()
# nope
# Note: get_a never gets called due to short-circuiting
if get_b() and get_a():
    print('yep')
else:
    print('nope')
