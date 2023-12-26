from typing import List


def sum_all(*nums: List[int]) -> int:
    """\
    *args is a special parameter which, when declared in a function, gathers all
    the remaining arguments in a tuple. The name can be anything starting with *
    Example: *hello
    """
    result = 0
    for n in nums:
        result += n
    return result


print(sum_all(1, 2, 3, 4))  # 10
print(sum_all(11, 22, 33, 44, 55, 66))  # 231


def favorite_colors(**kwargs):
    """\
    **kwargs is a special parameter which, when declared in a function, gathers all
    the remaining arguments in a dictionary. The name can be anything starting with **
    Example: **world
    """
    for person, color in kwargs.items():
        print(f'{person.capitalize()}\'s favorite color is {color.capitalize()}')


favorite_colors(foo='red', bar='green', baz='blue')
# Foo's favorite color is Red
# Bar's favorite color is Green
# Baz's favorite color is Blue
