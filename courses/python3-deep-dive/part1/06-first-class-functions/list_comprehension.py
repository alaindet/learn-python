"""
A list comprehension is a syntactic construct to build lists in a concise way

General syntax is
[<expr> for <varname> in <iterable>]

or with filtering
[<expr> for <varname> in <iterable> if <conditional_expr>]

It is generally used as an alternative to map() and filter()
"""

nums = [1, 2, 3, 4]

# Basic approach
doubled1 = []
for num in nums:
    doubled1.append(num * 2)
print(doubled1)  # [2, 4, 6, 8]

# Equivalent via map()
doubled2 = list(map(lambda num: num * 2, nums))
print(doubled2)  # [2, 4, 6, 8]

# Equivalent via list comprehension
# This is sligthly faster and more efficient since it translates to less
# byte code and less work for the garbage collector
doubled3 = [num * 2 for num in nums]
print(doubled3)  # [2, 4, 6, 8]

# Return the odd numbers up to 100 using filtering
odds1 = list(filter(lambda num: num % 2 == 1, range(101)))
# print(odds1)  # [1, 3, 5, 7, ..., 99]
odds2 = [num for num in range(101) if num % 2 == 1]
# print(odds2)  # [1, 3, 5, 7, ..., 99]
print(odds1 == odds2)  # True

# Combine with zip()
# Sum numbers [0, 10] and [10, 20] pairwise
with_zip = [a + b for a, b in zip(range(10+1), range(10, 20+1))]
print(with_zip)  # [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

# Replace map() and filter() with a list comprehension
nums = range(10)

# With map() and filter()
list1 = list(filter(lambda y: y < 25, map(lambda x: x**2, nums)))
print(list1)  # [0, 1, 4, 9, 16]

# With a nested list comprehension
list2 = [x**2 for x in nums if x**2 < 25]
print(list2)  # [0, 1, 4, 9, 16]

# With a nested list comprehension
list3 = [y for y in [x**2 for x in nums] if y < 25]
print(list3)  # [0, 1, 4, 9, 16]
