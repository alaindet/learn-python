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

print(fibo(30))