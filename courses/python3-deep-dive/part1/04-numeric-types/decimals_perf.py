"""
The decimal.Decimal class comes at a cost. On average, a Decimal occupies 4x the
bytes, takes 10x time to instantiate and takes 3x more time to perform operations
compared to floats

| Metric                 | float    | Decimal   | Factor |
| ---------------------- | -------- | --------- | ------ |
| size                   | 24 bytes | 104 bytes | ~4x    |
| instantion (1 million) | 0.03 s   | 0.4 s     | ~10x   |
| add (1 million)        | 0.04 s   | 0.12 s    | ~3x    |
| sqrt (1 million)       | 0.12 s   | 2.57 s    | ~20x   |
"""

import math
import sys
import time
from decimal import Decimal
from typing import Callable


def timer(name: str, fn: Callable, iterations=1_000_000) -> None:
    t_i = time.perf_counter()
    for i in range(iterations):
        fn()
    t_f = time.perf_counter() - t_i
    print(f'{name}: took {t_f} seconds to run {iterations} times')


# -----------------------------------------------------------------------------
#
# Size in bytes
#
# -----------------------------------------------------------------------------

print(sys.getsizeof(3.14159))  # 24 bytes
print(sys.getsizeof(Decimal('3.14159')))  # 104 bytes


# -----------------------------------------------------------------------------
#
# Instantiation
#
# -----------------------------------------------------------------------------

def create_floats() -> Callable[[], None]:
    def fn() -> None:
        a = 3.14159
    return fn


def create_decimals() -> Callable[[], None]:
    def fn() -> None:
        b = Decimal('3.14159')
    return fn


timer('Create floats', create_floats())
timer('Create decimals', create_decimals())


# -----------------------------------------------------------------------------
#
# Add operation
#
# -----------------------------------------------------------------------------

def add_floats(sample: float) -> Callable[[], None]:
    def fn() -> None:
        sample + sample
    return fn


def add_decimals(sample: Decimal) -> Callable[[], None]:
    def fn() -> None:
        sample + sample
    return fn


timer('Add floats', add_floats(3.14159))
timer('Add decimals', add_decimals(Decimal('3.14159')))


# -----------------------------------------------------------------------------
#
# Square root operation
#
# -----------------------------------------------------------------------------

def sqrt_float(sample: float) -> Callable[[], None]:
    def inner_sqrt_float() -> None:
        math.sqrt(sample)

    return inner_sqrt_float


def sqrt_decimal(sample: Decimal, n=1) -> Callable[[], None]:
    def inner_sqrt_decimal() -> None:
        sample.sqrt()

    return inner_sqrt_decimal


timer('Square root floats', sqrt_float(3.14159))
timer('Square root decimals', sqrt_float(Decimal('3.14159')))
