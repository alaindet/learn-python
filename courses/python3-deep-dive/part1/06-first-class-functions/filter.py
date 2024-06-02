"""
- filter() is a higher-order function accepting a function and one iterable
- It applies the given function to all the elements of the iterable
- It returns an iterator
"""

nums = [1, 2, 3, 4]

# <filter object at 0x0000025490EBE650>
print(filter(lambda n: n % 2 == 0, nums))
print(list(filter(lambda n: n % 2 == 0, nums)))  # [2, 4]

# If you pass no function to filter, it just checks for truthyness
junk = [1, 0, 4, 'a', '', None, True, False]
filtered1 = list(filter(None, junk))
filtered2 = list(filter(lambda x: bool(x), junk))

print(filtered1)  # [1, 4, 'a', True]
print(filtered2)  # [1, 4, 'a', True]
print(filtered1 == filtered2)  # True
