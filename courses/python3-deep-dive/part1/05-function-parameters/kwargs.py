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


def fn4(*, d, **kwargs):
    print(f'fn4: d={d}, kwargs={kwargs}')


fn4(d=1)  # fn4: d=1, kwargs={}
fn4(d=1, a=2, b=3, c=4)  # fn4: d=1, kwargs={'a': 2, 'b': 3, 'c': 4}


def fn5(**kwargs):
    print(f'fn5: kwargs={kwargs}')


fn5(a=1, b=2, c=3)  # fn5: kwargs={'a': 1, 'b': 2, 'c': 3}


def fn6(*args, **kwargs):
    print(f'fn6: args={args}, kwargs={kwargs}')


fn6()  # fn6: args=(), kwargs={}
fn6(1, 2)  # fn6: args=(1, 2), kwargs={}
fn6(a=1, b=2)  # fn6: args=(), kwargs={'a': 1, 'b': 2}
fn6(1, 2, a=3, b=4)  # fn6: args=(1, 2), kwargs={'a': 3, 'b': 4}

# The native print() is defined like this
# print(*objects, sep='', end='\n', file=sys.stdout, flush=False)
# So you can do these things
print('a', 'b', 'c', sep=',')  # a,b,c

# The next two print() calls print this combined
# a,b,c@d,e,f$
print('a', 'b', 'c', sep=',', end='@')
print('a', 'b', 'c', sep=',', end='$')
