def fn_counter(fn):
    count = 0

    def apply(*args, **kwargs):
        nonlocal count
        count += 1
        return fn(*args, **kwargs)

    def times():
        return count

    return apply, times


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


add_apply, add_times = fn_counter(add)
print(add_apply.__closure__)
# Prints
# (
#   <cell at 0x000002BCA05AFE80: int object at 0x00007FFA3B565D80>, <-- count
#   <cell at 0x000002BCA05AFDC0: function object at 0x000002BCA0739BC0> <-- fn
# )
print(add_apply.__code__.co_freevars)  # ('count', 'fn')

print('add_apply(10, 10) = ', add_apply(10, 10))  # 20
print('add_apply(10, 10) = ', add_apply(10, 10))  # 20
print('add_apply(10, 10) = ', add_apply(10, 10))  # 20
print(f'add() called {add_times()} times')  # add() called 3 times

mul_apply, mul_times = fn_counter(mul)
print(mul_apply.__closure__)
# Prints
# (
#   <cell at 0x0000029014B3FFD0: int object at 0x00007FFA3B565D80>,  <-- count
#   <cell at 0x0000029014B3FF10: function object at 0x0000029014CD9BC0> <-- fn
# )
print(mul_apply.__code__.co_freevars)  # ('count', 'fn')

print('mul_apply(10, 10) = ', mul_apply(10, 10))  # 100
print('mul_apply(10, 10) = ', mul_apply(10, 10))  # 100
print(f'mul() called {mul_times()} times')  # mul() called 2 times
