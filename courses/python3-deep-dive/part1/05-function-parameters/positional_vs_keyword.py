"""
## Positional arguments
- As any other programming language, positional args are an ordered sequence
"""


def with_pos_args(a, b, c):
    """A function with positional arguments only"""
    print(f'with_pos_args: a={a}, b={b}, c={c}')


with_pos_args(1, 2, 3)  # with_pos_args: a=1, b=2, c=3

"""
## Keywords arguments
- Functions can accept "named" or "keyword" arguments
- This allows to specify only some arguments and not all
- This allows providing arguments in any order to the functions without affecting
  the result
"""


def with_keyword_args(a=1, b=2, c=3):
    """A function with named arguments only"""
    print(f'with_keyword_args: a={a}, b={b}, c={c}')


def sum_keyword_args(a=1, b=2, c=3) -> int:
    return a + b + c


with_keyword_args()  # with_keyword_args: a=1, b=2, c=3
with_keyword_args(c=42)  # with_keyword_args: a=1, b=2, c=42

print(
    sum_keyword_args(c=30, a=10, b=20),  # 60
    sum_keyword_args(a=10, b=20, c=30),  # 60
    sum_keyword_args(b=20, c=30, a=10),  # 60
)
