# If statements do not strictly require parentheses, but they can be used
# PEP 8 and Google Style Guide recommend *NOT* using parentheses unless required
# Where "required" implies multiple lines in the if condition and/or better readability

foo = 42
bar = True
baz = None

if foo == 42:
    print('Yes.')

if (foo == 42):
    print('Of course.')

# Kind of required
if (
    foo == 42
    and bar is True
    and baz is None
):
    print('Ok')

def isEven(n: int) -> bool:
    return n % 2 == 0

if isEven(foo):
    print(f'{foo} is even')
else:
    print(f'{foo} is odd')

# The horrible "elif" keyword, it stands for "else if"
if foo < 10:
    print('Foo is less than 10')
elif foo < 30:
    print('Foo is less then 30')
elif foo < 50:
    print('Foo is less then 50')
else:
    print('Foo is more than 50')