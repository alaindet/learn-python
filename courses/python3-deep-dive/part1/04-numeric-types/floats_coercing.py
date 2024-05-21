"""
There a number of ways to coerce a float into an integer, but all algorithms
produce data loss anyway

Methods are
- Truncation
- Flooring
- Ceiling
- Rouding
"""

import math

# Truncation: just take the integer part
print(math.trunc(10)) # 10
print(math.trunc(10.000)) # 10
print(math.trunc(10.2)) # 10
print(math.trunc(10.999)) # 10

# Equivalent to math.trunc, just a bit implicit
print(int(10)) # 10
print(int(10.000)) # 10
print(int(10.2)) # 10
print(int(10.999)) # 10