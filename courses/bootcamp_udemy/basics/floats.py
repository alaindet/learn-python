"""
Decimals in Python are stored as floating point numbers (base 2),
meaning there's always an approximation
Almost all languages have the same problem
Some languages have specialized data types for precise decimals
"""

from math import isclose

# Approximation works at this level of detail
print(0.125 == 1 / 10 + 2  / 100 + 5 / 1000) # True

# However, this rational periodic number cannot be approximated with 20 decimals
print(format(1/3, '.20f')) # 0.33333333333333331483

# Even exact values are approximated!
print(format(1/10, '.20f')) # 0.10000000000000000555

# In this case, 0.125 has an exact representation in base 2
print(format(1/8, '.20f')) # 0.12500000000000000000

# Watch this
a = 0.1 * 3
b = 0.3
print(format(a, '.20f')) # 0.30000000000000004441
print(format(b, '.20f')) # 0.29999999999999998890
print(a == b) # False

# math.isclose() to the rescue!
x = 0.0000001
y = 0.0000002
print(x == y) # False
# This uses "absolute tolerance" so that the two values must be at most
# That much apart
# This is better for exact values and/or small values
print(isclose(x, y, abs_tol=0.01)) # True

x = 9999999999.001
y = 9999999999.002
print(x == y) # False
# This uses "relative tolerance" so that the two value must be at most
# That much percentage apart relative to their values
# This is better for large numbers
print(isclose(x, y, rel_tol=0.01)) # True

a = 3.4
b = 2.3
print(a + b) # 5.699999999999999 (Should be 5.7!)
