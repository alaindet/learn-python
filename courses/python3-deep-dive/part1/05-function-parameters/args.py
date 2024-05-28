from numbers import Number
from typing import List, Tuple, Union


def my_sum(*args: List[Number]) -> Number:
    """\
    A generic typed re-implementation of the sum() function. Uses the Number
    generic tyiping
    """
    result = 0
    for n in args:
        result += n
    return result


def weird_sum(a, b, *args):
    """With variadic arguments at the end"""
    result = a + b
    for n in args:
        result += n
    return result


# Unpacking the other way around
nums = [1, 2, 3, 4, 5]
# print(my_sum(nums))  # <-- This does not work!
print(my_sum(*nums))  # This works


def avg(*args: List[Number]) -> float:
    """Generic average function, accepts variadic arguments"""

    count = len(args)

    if count == 0:
        return 0.0

    return sum(args) / count


print(avg(1, 2, 3, 4))  # 2.5


def mixed_avg(*args: List[Union[Number, List[Number], Tuple[Number]]]) -> float:
    """Calculates average of a sequence of numbers. Works with variadic arguments,
    lists, tuples and sets"""
    count = len(args)

    if count == 0:
        return 0

    def avg(nums: List[Number]) -> float:
        return sum(nums) / len(nums)

    if count > 1:
        return avg(args)

    first_arg = args[0]
    is_list = isinstance(first_arg, list)
    is_tuple = isinstance(first_arg, tuple)
    is_set = isinstance(first_arg, set)

    if is_list or is_tuple or is_set:
        try:
            return avg(first_arg)

        # One or more value is not a number!
        except TypeError:
            return 0.0


# Works with variadic arguments
print('mixed_avg variadic:', mixed_avg(1, 2, 3, 4))
print('mixed_avg list:', mixed_avg([1, 2, 3, 4]))
print('mixed_avg tuple:', mixed_avg((1, 2, 3, 4)))
print('mixed_avg set:', mixed_avg({1, 2, 3, 4}))
print('mixed_avg invalid values:', mixed_avg({1, 2, '3', 4}))
