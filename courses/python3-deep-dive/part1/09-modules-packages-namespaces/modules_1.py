def foo():
    pass

print(foo)              # <function foo at 0x000002266F1F9B20>
print(globals()['foo']) # <function foo at 0x000002266F1F9B20>
print(locals()['foo'])  # <function foo at 0x000002266F1F9B20>

import math
import fractions

# This is a special module, it's written in C
print(math) # <module 'math' (built-in)>
print(globals()['math']) # <module 'math' (built-in)>
print(type(math)) # module
print(id(math)) # 2563753579584
print(fractions) # <module 'fractions' from 'C:\\...\\.pyenv\\...\\Lib\\fractions.py'>
print(type(fractions)) # module

import math
print(id(math)) # 2563753579584 (Same as above)

"""
The code below prints a dictionary containing all the functions from the math
module
"""
# print(math.__dict__)

"""
This prints a dictionary containing all the loaded modules
For a small script, it even loads ~60 modules!
"""
# import sys
# print(sys.modules)

from types import ModuleType

print('is fractions a module?', isinstance(fractions, ModuleType))

mymod = ModuleType('mymod', 'This is the mymod module')
print('is mymod a module?', isinstance(mymod, ModuleType))
print(mymod.__dict__)
# An empty module looks like this
# {
#     '__name__': 'mymod',
#     '__doc__': 'This is the mymod module',
#     '__package__': None,
#     '__loader__': None,
#     '__spec__': None
# }

mymod.pi = 3.14159
mymod.sum = lambda a, b: a + b
print(mymod.__dict__)
# {
#     '__name__': 'mymod',
#     '__doc__': 'This is the mymod module',
#     '__package__': None,
#     '__loader__': None,
#     '__spec__': None
#     'pi': 3.14159,
#     'sum': <function <lambda> at 0x0000013BC4279D00>
# }