import time


def time_it(fn, *args, rep=1, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    seconds_took = end - start
    print(f'The function took {seconds_took} seconds')


time_it(print, 1, 2, 3, sep=',', rep=5)


def pow_1(n, *, start=1, end):
    results = []
    for i in range(start, end):
        results.append(n**i)
    return results


def pow_2(n, *, start=1, end):
    """Using list comprehension"""
    return [n**i for i in range(start, end)]


def pow_3(n, *, start=1, end):
    """Using a generator. This returns a generator, but DOES NOT calculate
    anything"""
    return (n**i for i in range(start, end))


def pow_4(n, *, start=1, end):
    return list(pow_3(n, start=start, end=end))


print(pow_1(2, end=10))  # [2, 4, 8, 16, 32, 64, 128, 256, 512]
print(pow_2(2, end=10))  # [2, 4, 8, 16, 32, 64, 128, 256, 512]

# <generator object pow_3.<locals>.<genexpr> at 0x0000024F8420F370>
print(pow_3(2, end=10))

print(list(pow_3(2, end=10)))  # [2, 4, 8, 16, 32, 64, 128, 256, 512]

# List comprehensions run a little faster because they're usually optimized
# by the JIT compiler and this results in less byte code
time_it(pow_1, 2, end=20_000, rep=5)  # ~2.11 seconds
time_it(pow_2, 2, end=20_000, rep=5)  # ~2.00 seconds

# This runs much faster because it just returns a generator,
# but it DID NOT calculate any value yet
time_it(pow_3, 2, end=20_000, rep=5)  # ~0.00001 seconds

# This is in line with everything else as casting a generator to a list forces it
# to exhaust (calculate) all the items in the list
time_it(pow_4, 2, end=20_000, rep=5)  # ~1.99s
