from functools import reduce


def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        elapsed = perf_counter() - start
        args_ = [str(arg) for arg in args]
        kwargs_ = [f'{k}={v}' for (k, v) in kwargs.items()]
        all_args = ','.join(args_ + kwargs_)
        print(f'{fn.__name__}({all_args}) took {elapsed:.6f} seconds')
        return result

    return inner


def _fibo(n: int) -> int:
    if n <= 2:
        return 1
    return _fibo(n - 1) + _fibo(n - 2)


@timed
def fibo(n: int) -> int:
    return _fibo(n)


@timed
def fibo_loop(n: int) -> int:
    a, b = 1, 1
    for i in range(3, n + 1):
        a, b = b, a + b
    return b


# Implementing Fibonacci's sequence with a loop in much faster (20'000 times!) than
# the bare recursion implementation
print(fibo(30))  # 832040, took 0.127641 seconds
print(fibo_loop(30))  # 832040, took 0.000011 seconds


@timed
def fibo_reduce(n: int) -> int:
    initial = (1, 0)
    dummy = range(n-1)
    result = reduce(
        lambda prev, n: (prev[0] + prev[1], prev[0]),
        dummy,
        initial
    )
    return result[0]


# It's a little slower than
print(fibo_reduce(30))  # 832040, took 0.000018 seconds
