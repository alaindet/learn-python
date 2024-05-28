def fn(a, b, *args, d):
    print(f'fn: a={a}, b={b}, args={args}, d={d}')


fn(1, 2, 'x', 'y', d=100)  # fn: a=1, b=2, args=('x', 'y'), d=100
fn(1, 2, d=100)  # fn: a=1, b=2, args=(), d=100

# This fails because the keyword arg d is required!
# fn(1, 2) # TypeError: fn() missing 1 required keyword-only argument: 'd'


def fn2(*args, d):
    """This function has optional positional arguments and one mandatory keyword
    argument"""
    print(f'fn2: args={args}, d={d}')


fn2(1, 2, 3, d=42)  # fn2: args=(1, 2, 3), d=42
fn2(d=100)  # fn2: args=(), d=100


def fn3(*, d):
    """This function only has a mandatory keyword argument and no positional
    arguments are accepted"""
    print(f'fn3: d={d}')

# TypeError: fn3() takes 0 positional arguments but 1 positional argument were given
# fn3(1, d=42)


fn3(d=42)  # fn3: d=42
