"""
Python does not have prefix (++i) and postfix (i++) operators
There are only short-hand assignments like below
"""

a = 1
a += 2 # Equivalent: a = a + 2
a -= 1 # Equivalent: a = a - 1
a *= 3 # Equivalent: a = a * 3
a /= 2 # Equivalent: a = a / 2
a **= 2 # Equivalent: a = a ** 2
a %= 2 # Equivalent: a = a % 2

# Built-in functions
quotient, remainder = divmod(31, 6)
print(quotient, remainder) # 5 1

print(pow(4, 3)) # 64
print(sum([1, 2, 3, 4, 5])) # 15
print(max([1, 2, 5, 3, 4])) # 5
print(min([1, 2, -42, 3, 4])) # -42
print(round(5.55), round(1.5), round(2.2)) # 6 2 2

# With given number of decimals
print(
    round(6.66666666, 1),
    round(6.66666666, 3),
) # 6.7 6.667
