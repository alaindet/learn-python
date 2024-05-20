import sys
import time
import math

"""
Integers use variable bits to store their value
"""

print(type(100)) # <class 'int'>

# 28 bits are used, due to overhead of 1 being an object
print(sys.getsizeof(0)) # 28
print(sys.getsizeof(1)) # 28

# Big numbers (like 2 ^ 400) can be seamlessly stored in an int
# However, bigger numbers get more time to be manipulated and read
print(sys.getsizeof(2 ** 400)) # 80

# Section: performance ########################################################
# def calc(a):
#     for i in range(10_000_000):
#         a * 2

# start = time.perf_counter()
# calc(42)
# end = time.perf_counter()
# print('42', end-start) # 0.2259469999698922 seconds

# start = time.perf_counter()
# calc(2 ** 100)
# end = time.perf_counter()
# print('2 ** 100', end-start) # 0.4562327999738045 seconds

# start = time.perf_counter()
# calc(2 ** 10_000)
# end = time.perf_counter()
# print('2 ** 10_000', end-start) # 4.155341999954544 seconds


# Section: operations #########################################################
"""
int + int = int
int - int = int
int * int = int
int / int = float
int // int = int
int % int = int

PLEASE NOTE:
This fundamental equation must be always satisfied
a = b * (a // b) + a % b
"""

def my_division(a, b):
    div_result = a // b
    mod_result = a % b
    return (div_result, mod_result)

print(155/4) # 38.75
print(my_division(155, 4)) # (38, 3)

print(math.floor(3.14)) # 3
print(math.floor(-3.14)) # -4
print(math.floor(-3.0000000001)) # -4

# PLEASE NOTE:
# This breaks the precision of the floating point "float" data type, so that the
# value here is -3 and not "-3 plus something very small" and its floor is then
# -3, not -4
print(math.floor(-3.0000000000000001)) # -3