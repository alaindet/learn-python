import random
from typing import List


def shuffle(the_list: List) -> List:
    return sorted(the_list, key=lambda n: random.random())


def get_random_ints(max=10) -> List[int]:
    ordered_list = list(range(max))
    return shuffle(ordered_list)


print(get_random_ints())  # [0, 3, 4, 7, 8, 9, 2, 6, 1, 5]
print(get_random_ints())  # [3, 1, 0, 9, 6, 8, 2, 5, 7, 4]
print(get_random_ints(5))  # [3, 1, 4, 0, 2]
