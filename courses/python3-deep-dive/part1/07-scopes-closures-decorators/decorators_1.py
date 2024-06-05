"""
Decorators

- A decorator takes a function as an argument
- Returns a closure
- The closure accepts combinations of parameters
- Runs some code in the closure
- The closure calls the decorated function via args passed to the closure
- The closure returns whatever is returned by the decorated function
- It's conveniently called via @, but it's not required
"""

from functools import wraps


def bad_watcher(fn):
    """
    This function acts as a simple decorator, but it screws all the inner
    function's meta data like .__name__, .__doc__ etc.
    """
    def inner(*args, **kwargs):
        print('I am watching you!')
        return fn(*args, **kwargs)
    return inner


def better_watcher(fn):
    """
    This function uses functools.wraps to restore the decorator function's metadata
    """
    def inner(*args, **kwargs):
        print('I am watching you!')
        return fn(*args, **kwargs)
    return wraps(fn)(inner)


def best_watcher(fn):
    """
    This function uses functools.wraps as a decorator
    """
    @wraps(fn)
    def inner(*args, **kwargs):
        print('I am watching you!')
        return fn(*args, **kwargs)

    return inner


def add(a, b):
    return a + b


add = best_watcher(add)

# Prints
# I am watching you!
# 3
print(add(1, 2))


# Equivalently, Python allows to "decorate" functions via @

@best_watcher
def mul(a, b):
    return a * b


# Prints
# I am watching you!
# 200
print(mul(10, 20))


def watcher_with_custom_message(message='I am watching you'):
    """This is a decorator factory, i.e. a function returning a decorator, not
    a straight decorator"""
    def decorator(fn):
        def inner(*args, **kwargs):
            print(message)
            return fn(*args, **kwargs)

        return inner

    return decorator


@watcher_with_custom_message('Some custom message')
def mul_custom(a, b):
    return a * b


# Prints
# Some custom message
# 300
print(mul_custom(10, 30))
