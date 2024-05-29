import time


def time_it(fn, *args, **kwargs):
    start = time.perf_counter()
    fn(*args, *kwargs)  # <-- Mind this, just one asterisk for *kwargs
    end = time.perf_counter()
    seconds_took = end - start
    print(f'The function took {seconds_took} seconds')


time_it(print, 1, 2, 3, a=1, b=2, c=3)
