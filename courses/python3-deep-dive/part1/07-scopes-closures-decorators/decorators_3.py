def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print(f'{run_dt}: called {fn.__name__}')
        return result

    return inner


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


@timed
@logged
def dummy():
    pass


# 2024-06-06 19:44:27.949044+00:00: called dummy
# dummy() took 0.000049 seconds
dummy()
