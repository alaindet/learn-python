"""
Python does some things when using a non-boolean as a boolean, (ex.: if, while)
"""

my_list = [1, 2, 3]

if my_list:
    print('my_list is truthy (shortcut)')
else:
    print('my_list is falsy (shortcut)')

# This is equivalent to
if my_list is not None and len(my_list) > 0:
    print('my_list is truthy')
else:
    print('my_list is falsy')


empty_list = []

# As expected, this is falsy
if empty_list:
    print('empty_list is truthy')
else:
    print('empty_list is falsy')

# This is interesting. The list gets filled, but "append()" returns None, which
# is falsy
if empty_list.append(1):
    print('empty_list is truthy')
else:
    print('empty_list is falsy')

# Checking again, now empty_list is truthy
if empty_list:
    print('empty_list is truthy', empty_list)
else:
    print('empty_list is falsy')
