import time
from datetime import datetime, UTC
from typing import List, Optional

a = 42  # This is executed right away while executing this file (the module)


def fn1(a):  # <-- This function gets defined while executing the file
    print(a)  # <-- This is not run until "fn1" gets called

# This register "fn2" as a function by creating a function object referencing it
# The "a=10" default parameter is run while executing the module


def fn2(  # <-- This function gets defined while executing the file
    a=10  # <-- This runs ONLY ONCE at "definition time", so as soon as the module runs
          #     This means default values SHOULD be immutable primitive values,
          #     nothing else
):
    print(a)  # <-- This is not run until "fn2" gets called


# Consider this: this logger function should accept a datetime and use the current
# date time if none is provided. WARNING: defining it like this actually stores
# the default value once, when defining the function, not every time you call log(),
# as expected

def log(msg: str, *, dt=datetime.now(UTC)):
    print(f'{dt}: {msg}')


time.sleep(1)
log('One', dt=datetime.now(UTC))

time.sleep(1)
log('Two')

time.sleep(1)
log('Three')

# Prints
# xxxx-xx-xx xx:xx:51.937846+00:00: One
# xxxx-xx-xx xx:xx:50.936489+00:00: Two
# xxxx-xx-xx xx:xx:50.936489+00:00: Three
#
# Explanation
# Despite waiting one second between each log, the first log forces the current
# timestamp by declaring the "dt" keyword arg explicitly, while the subsequent
# logs use the default timestamp.
#
# Oddly enough, "Two" and "Three" happen 1 and 2 seconds AFTER "One" respectively,
# but they show the same exact timestamp, dating BEFORE "One"
# That is because they're leveraging the same fixed timestamp wrongly used as a
# default argument, calculated only once (when log() was defined)


def better_log(msg: str, *, dt: Optional[datetime] = None):
    """This works as intended and calculates the timestamp every time if needed"""
    dt = dt or datetime.now(UTC)
    print(f'[better_log] {dt}: {msg}')


time.sleep(1)
better_log('One', dt=datetime.now(UTC))

time.sleep(1)
better_log('Two')

time.sleep(1)
better_log('Three')

# Prints
# [better_log] xxxx-xx-xx xx:xx:43.096867+00:00: One
# [better_log] xxxx-xx-xx xx:xx:44.097418+00:00: Two
# [better_log] xxxx-xx-xx xx:xx:45.098269+00:00: Three
#
# Now this works as inteded, with the same signature as before

#
# Using a mutable object as a default parameter - HARD NO
# Look at this
#
my_default_arg = [1, 2, 3]


def multiplier(a: int, nums: List[int] = my_default_arg) -> List[int]:
    result = []
    for n in nums:
        result.append(n * a)
    return result

# Despite calling the function the same way, we're mutating an object used as a
# default argument and we're practically changing the default argument value at
# runtime!


print(multiplier(2))  # [2, 4, 6]
my_default_arg.append(4)

print(multiplier(2))  # [2, 4, 6, 8]
my_default_arg.append(5)

print(multiplier(2))  # [2, 4, 6, 8, 10]


# This is somewhat ok
my_default_arg2 = (1, 2, 3)


def multiplier2(a: int, nums: List[int] = my_default_arg2) -> List[int]:
    result = []
    for n in nums:
        result.append(n * a)
    return result


print(multiplier2(2))  # [2, 4, 6]
print(multiplier2(2))  # [2, 4, 6]
print(multiplier2(2))  # [2, 4, 6]
