"""\
Strings are just arrays of one-letter strings
Indexing with negative indices is fine
"""

# Pick letter at index 6
print('Hello World'[6]) # 'W'

# Pick letter at index length - 1 (the last character)
print('Hello World'[-1]) # 'd'

# Out-of-range positive index: raises an IndexError
# print(salute[100])

# Out-of-range negative index: raises an IndexError
# print(salute[-100])

# Left index only
print('Foo Bar'[0:]) # 'Foo Bar'

# Right index only
print('Foo Bar'[:3]) # 'Foo'

# Out-of-range right index
print('Foo Bar'[:999]) # 'Foo Bar'

# Out-of-range left index
print('Foo Bar'[999:]) # ''

# Pick last two characters
print('Foo Bar'[-2:]) # 'ar'

# All but the last character
print('Foo Bar'[:-1]) # 'Foo Ba'

# Trick to copy
a = 'Foo Bar'
b = a[:]
a = 'Foo Baz'
print(a) # 'Foo Baz'
print(b) # 'Foo Bar'

# This raises a TypeError, because strings are immutable!
# a[1] = 'X'

question = 'How many characters does this question have?'
print(question, len(question))