"""\
Sets
https://docs.python.org/3/tutorial/datastructures.html#sets

- Collection of unique values
- No ordering is provided
- Hence, no indexing is allowed
"""

# Creating a literal set
from typing import List


set1 = {1, 2, 3, 4}
print(set1)  # {1, 2, 3, 4}

set2 = {1, 2, 3, 3, 3, 4}
print(set2)  # {1, 2, 3, 4} <-- Notice the duplicate 3s are gone!

# Creating a set via set() built-in function
set3 = set({1, 2, 3, 4})
print(set3)  # {1, 2, 3, 4}

# Duplication is removed as well
set4 = set({1, 2, 3, 3, 4})
print(set4)  # {1, 2, 3, 4}

# Checking if a value is in a set
print(3 in set1)  # True
print(42 in set1)  # False

# Simple loop
for n in set1:
    print(n)

# Using a trick to remove duplicates


def remove_duplicates(nums: List[int]) -> List[int]:
    return list(set(nums))


print(remove_duplicates([1, 1, 2, 2, 3, 3]))  # [1, 2, 3]
