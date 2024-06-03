from functools import partial

def my_func(a, b, c) -> None:
    print(a, b, c)

# Manual
def my_func_with_a(b, c) -> None:
    return my_func(10, b, c)

def my_func_with_b(a, c) -> None:
    return my_func(a, 20, c)

def my_func_with_c(a, b) -> None:
    return my_func(a, b, 30)

# With partial
my_func_partial_a = partial(my_func, a=10)
my_func_partial_b = partial(my_func, b=20)
my_func_partial_c = partial(my_func, c=30)

my_func_with_a(b=2, c=3) # 10 2 3
my_func_partial_a(b=2, c=3) # 10 2 3

my_func_with_b(a=1, c=3) # 1 20 3
my_func_partial_b(a=1, c=3) # 1 20 3

my_func_partial_c(a=1, b=2) # 1 2 30
my_func_partial_c(a=1, b=2) # 1 2 30

# Complex example with partial

def fn(a, b, *args, k1, k2, **kwargs):
    print(a, b, args, k1, k2, kwargs)

def manual_partialized(b, *args, k2, **kwargs):
    fn(10, b, *args, k1='a', k2=k2, **kwargs)

# Equivalent
partialized = partial(fn, 10, k1='a')

# Exactly the same
manual_partialized(20, 30, k2='b', k3='c') # 10 20 (30,) a b {'k3': 'c'}
partialized(20, 30, k2='b', k3='c') # 10 20 (30,) a b {'k3': 'c'}

# Another example
def pow(base, exp):
    return base ** exp

squared = partial(pow, exp=2)
cubed = partial(pow, exp=3)

print(pow(3, 2)) # 9
print(squared(3)) # 9

print(pow(3, 3)) # 27
print(cubed(3)) # 27