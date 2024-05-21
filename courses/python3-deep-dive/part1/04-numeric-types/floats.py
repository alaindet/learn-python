from math import fabs


a = 0.1

print(f'{a:.25f}') # 0.1000000000000000055511151
print(a) # 0.1

b = 0.1 + 0.1 + 0.1
c = 0.3
print(b == c) # False

# Rouding works, BUT it forces you to use an absolute and fixed tolerance
# expressed in how many decimals you want to calculate the round on
print(round(b, 3) == round(c, 3)) # True

# For big numbers, a relative tolerance is better
# These two numbers differ by less than 0.0001% but rounding with absolute
# tolerance does not check that
b = 10_000.1
c = 10_000.2
print(round(b, 3) == round(c, 3)) # False

# Here, a relative tolerance of 1% is used, which is then equal to 100.002
# Given the real difference is 0.1 (much smaller than 100.002), the two values
# are "closer than 1%" (they're actually closer than 0.0001%)
relative_tolerance = 0.01 # 1%
tolerance = max(b, c) * relative_tolerance
print(fabs(b - c) < tolerance) # True