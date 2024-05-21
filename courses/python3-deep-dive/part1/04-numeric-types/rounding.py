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