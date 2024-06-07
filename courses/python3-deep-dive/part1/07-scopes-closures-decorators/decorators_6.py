def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        elapsed = perf_counter() - start
        print(f'{fn.__name__}() took {elapsed:.6f} seconds')
        return result

    return inner

def memoized(fn):
    from functools import wraps

    cache = {}

    @wraps(fn)
    def inner(*args, **kwargs):
        if args not in cache:
            cache[args] = fn(*args, **kwargs)
        return cache[args]

    return inner

def _fibo(n: int) -> int:
    """
    The base function used to calculate any number in the Fibonacci sequence by
    using brute force
    """
    if n <= 2:
        return 1
    return _fibo(n - 1) + _fibo(n - 2)

@timed
def fibo(n: int) -> int:
    return _fibo(n)

fibo(10) # 0.000010 seconds
fibo(20) # 0.000852 seconds
fibo(30) # 0.109152 seconds

class Fibo():
    def __init__(self):
        self.cache = {
            1: 1,
            2: 1,
        }

    @timed
    def calc(self, n: int) -> int:
        if n not in self.cache:
            self.cache[n] = _fibo(n)
        return self.cache[n]
    
fibo_instance = Fibo()
fibo_instance.calc(10) # 0.000011 seconds
fibo_instance.calc(20) # 0.000968 seconds
fibo_instance.calc(30) # 0.081089 seconds

def fibo_closure():
    """This is the closure-based version of the Fibo class defined earlier."""

    cache = {
        1: 1,
        2: 1,
    }

    @timed
    def inner(n: int) -> int:
        if n not in cache:
            cache[n] = _fibo(n)
        return cache[n]

    return inner

fibo_closure_fn = fibo_closure()
fibo_closure_fn(10) # 0.000009 seconds
fibo_closure_fn(20) # 0.000644 seconds
fibo_closure_fn(30) # 0.125525 seconds

@memoized
@timed
def memo_fibo(n: int) -> int:
    return _fibo(n)

memo_fibo(10) # 0.000006 seconds
memo_fibo(20) # 0.000535 seconds
memo_fibo(30) # 0.078442 seconds