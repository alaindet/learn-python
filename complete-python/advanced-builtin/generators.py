def hundred_numbers():
    """
    Yields None when finished
    """
    nums = []
    i = 0
    while i < 4:
        yield i
        i += 1
    return nums

generator = hundred_numbers()
print(next(generator)) # 0
print(next(generator)) # 1
print(list(generator)) # [2, 3] NOTE: It gives the rest, not all


def create_dummy_generator():
    yield 1
    yield 2
    yield 3

try:
    dummy_generator = create_dummy_generator()
    print(next(dummy_generator))
    print(next(dummy_generator))
    print(next(dummy_generator))
    print(next(dummy_generator)) # <-- This breaks the code
except StopIteration:
    print('Iteration stopped')


# Generator comprehension
my_gen = (x for x in [1, 2, 3, 4, 5])

try:
    while True:
        print(next(my_gen))
except StopIteration:
    print('my_gen stopped')