"""
- map() is a higher-order function accepting a function and one or more iterables
- It applies the given function to all the elements of the iterables
- It returns an iterator
"""

nums = [1, 2, 3, 4]


def squared_nums(nums):
    return map(lambda n: n ** 2, nums)


print(squared_nums(nums))  # <map object at 0x000001284C8BE770>
print(list(squared_nums(nums)))  # [1, 4, 9, 16]

for n in squared_nums(nums):
    print(n)


# Note: map() accepts multiple iterables and iterates on all iterables at the
# same time
list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(list(map(lambda a, b: a + b, list1, list2)))  # [11, 22, 33]


# Note: map() stops iterating at the shortest iterable of all the given ones
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30]
print(list(map(lambda a, b: a + b, list1, list2)))  # [11, 22, 33]
