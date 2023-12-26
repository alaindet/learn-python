def exponentiate(n: int, power=2) -> int:
    return n ** power


# With positional-only arguments
print(exponentiate(2, 3))  # 8

# With positional and keyword arguments mixed
print(exponentiate(2, power=3))  # 8

# With keyword-only arguments
print(exponentiate(n=2, power=3))  # 8

# With keyword-only arguments (no positional arguments) no order is needed
print(exponentiate(power=3, n=2))  # 8


def show_info(a: int, b: str, *args, instructor='John', **kwargs) -> None:
    """\
    This shows the correct ordering of parameters, which is
    1. Parameters
    2. `*args`
    3. Default parameters
    4. `**kwargs`
    """
    print('First, params:', a, b)
    print('Second, *args:', args, type(args))
    print('Third, default params:', instructor)
    print('Fourth, **kwargs:', kwargs.items())


show_info(1, 'hello', 2, 3, 4, foo=111, bar=222)
# First, params: 1 hello
# Second, *args: (2, 3, 4) <class 'tuple'>
# Third, default params: John
# Fourth, **kwargs: dict_items([('foo', 111), ('bar', 222)])
