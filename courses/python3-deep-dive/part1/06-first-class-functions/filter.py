"""
- filter() is a higher-order function accepting a function and one iterable
- It applies the given function to all the elements of the iterable
- It returns an iterator
"""

nums = [1, 2, 3, 4]

# <filter object at 0x0000025490EBE650>
print(filter(lambda n: n % 2 == 0, nums))
print(list(filter(lambda n: n % 2 == 0, nums)))  # [2, 4]
