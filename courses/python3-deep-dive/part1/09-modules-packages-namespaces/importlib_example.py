"""
importlib gives you tools to dynamically import Python modules
"""
import sys
import importlib
import math

importlib.import_module('math')

print('math' in sys.modules) # True
my_math = sys.modules['math'] # Pull in the reference from the cache
print(my_math.sqrt(9)) # 3.0

# As you can see, "my_math" and "math" are two references of the same module
print(my_math is math) # True