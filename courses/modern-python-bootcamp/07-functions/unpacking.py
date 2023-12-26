from typing import List

"""\
Tuple unpacking refers to transforming a list or a tuple argument in a tuple
parameter for a function. Useful with *args
"""


def sum_all(*args: List[int]) -> int:
    result = 0
    for n in args:
        result += n
    return result


nums = [1, 2, 3, 4, 5, 6, 7]
total = sum_all(*nums)  # <-- Look here: this is unpacking
print(total)  # 28


"""\
Dictionary unpacking refers to transforming a dictionary argument in a dictionary
parameter for a function. Useful with **kwargs
"""


def favorite_colors(**kwargs):
    for person, color in kwargs.items():
        print(f'{person} loves {color}')


people = {
    'Alice': 'Black',
    'Bob': 'Orange',
    'Charlie': 'Green',
}

favorite_colors(**people)
# Alice loves Black
# Bob loves Orange
# Charlie loves Green
