print('This is a string in single quotes')
print("This is a string in double quotes")
print('Escaping \'single quotes\'')
print("Escaping \"double quotes\"")
print('Mixing "quotes" (the opposite is fine too)')

# PEP 8 – Style Guide for Python Code
# https://peps.python.org/pep-0008/
# It recommends single quotes, just saying

print('You can put\nnew lines in strings')
print(r'You can skip escaping by prefixing a string with r for "raw", look at this => C:\Hello')

print("""Multiline
literals can be made with three quotes, better be double quotes
and they're used for Docstrings (documentaion in code), usually.
""")

# PEP 257 – Docstring Conventions
# https://peps.python.org/pep-0257/ 
# Docstrings should be done this way

print("""\
The slash at the end of line prevents automatic newlines,\
so this gets printed on a single line      
""")

# Multiplying and summing strings, no problem
print('ba' + 'na' * 2) # 'banana'

# You can even juxtapose strings and Python glues them together
print('Foo' 'Bar') # 'FooBar'
print(
    'Juxtapositioning '
    'is great for multiline literals too, '
    'but it only works with literals. '
    'Variables must rely on good ol\' + (plus) operator'
)

# See string-slicing.py
