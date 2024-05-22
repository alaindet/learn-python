"""
Rouding works by transforming a number to the closest number based on the rounding
interval. But when rounding a number with a "tie", the discrimination is based
on the Banker's Rounding Algorithm, as per the IEEE 754 standard. It states

Round to the nearest value, with ties rounded to the nearest value with an even
least significant digit
"""

print(round(1.25, 1)) # 1.2 instead of 1.3!

print(round(1.35, 1)) # 1.4 instead of 1.3!

print(round(-1.25, 1)) # -1.2 instead of 1.3!

# This is interesting
# Giving negative numbers to the number of digits to round() rounds the integer
# digits instead of the decimals. Here, we've got 20 and not 30 due to the
# Banker's rounding algorithm
print(round(25, -1)) # 20

# How to force rounding "towards +infinity"? Like this (mind that this works
# only with decimals)
def roundTowardsPlusInfinity(n: float) -> int:
    diff = -0.5 if n < 0 else 0.5
    return int(n + diff)

print(roundTowardsPlusInfinity(-10.4)) # -10
print(roundTowardsPlusInfinity(-10.5)) # -11

def sign(n):
    return -1 if n < 0 else 1

def roundAwayFromZero(n: float) -> int:
    return sign(n) * int(abs(n) + 0.5)

print(roundAwayFromZero(-10.4)) # -10
print(roundAwayFromZero(-10.5)) # -11