from typing import Callable, List


print(max(3, 4, 2, 5, 6, 42, 1)) # 42

def my_reducer(fn: Callable[[int, int], int], seq: List[int]) -> int:
    """TODO: Use generics"""
    result: int = seq[0]
    for n in seq[1:]:
        result = fn(result, n)
    return result

print(my_reducer(lambda a, b: a if a > b else b, [1, 2, 3, 4, 5])) # Max: 5
print(my_reducer(lambda a, b: a if a < b else b, [1, 2, 3, 4, 5])) # Min: 1
print(my_reducer(lambda a, b: a + b, [1, 2, 3, 4, 5])) # Sum: 15


"""
Python has a specialized reducer already defined in the functools built-in package
"""

from functools import reduce

print(reduce(lambda a, b: a if a > b else b, [1, 2, 3, 4, 5])) # Max: 5
print(reduce(lambda a, b: a if a < b else b, [1, 2, 3, 4, 5])) # Min: 1
print(reduce(lambda a, b: a + b, [1, 2, 3, 4, 5])) # Sum: 15

# "Minimum" character code
print(reduce(lambda a, b: a if a < b else b, 'python')) # h

# Works with sets
print(reduce(lambda a, b: a if a < b else b, {1, 2, 3, 4, 5})) # 1

# Works with tuples
print(reduce(lambda a, b: f'{a} {b}', ('hello', 'world'))) # hello world

# The initializer argument
# TypeError: reduce() of empty iterable with no initial value
# print(reduce(lambda a, b: a + b, []))
print(reduce(lambda a, b: a + b, [], 0)) # 0

# Built-in reducers
print(min(1, 2, 3, 4, 5)) # 1
print(min([1, 2, 3, 4, 5])) # 1

print(max(1, 2, 3, 4, 5)) # 5
print(max([1, 2, 3, 4, 5])) # 5

# Doesn't work with variadic arguments
print(sum([1, 2, 3, 4, 5])) # 15

# any() returns True if at least one element is truthy, otherwise it returns False
# Doesn't work with variadic arguments
print(any([False, 0, '', 42, None])) # True
print(any([False, 0, '', 0.0, None])) # True

# all() returns True only if ALL elements are truthy, otherwise it returns False
# Doesn't work with variadic arguments
print(all([True, 1, 1.0, 42, '', 69])) # False
print(all([True, 1, 1.0, 42, 'answer', 69])) # True