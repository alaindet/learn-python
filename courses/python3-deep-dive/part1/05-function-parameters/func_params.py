"""
# Functions
- In Python, any function argument is passed *BY REFERENCE*

## Conventions
- The variables scoped into the functions are called function *parameters*
- The values passed externally to the function via calling it are *arguments*
"""


from typing import List


def sum(a: int, b: int) -> int:
    return a + b


x = 10
y = 20
the_sum = sum(x, y)
print('the_sum', the_sum)  # 30


def param_id(the_arg: List[int]) -> None:
    return hex(id(the_arg))


a = [1, 2, 3]
print('outside:', hex(id(a)))  # 0x211b7168600
print('inside:', param_id(a))  # 0x211b7168600

# Here is a function with a default parameter
# WARNING: default parameters must be at end of positional arguments


def sum_with_default_args(a: int, b=0) -> int:
    return a + b


print(sum_with_default_args(42))  # 42
