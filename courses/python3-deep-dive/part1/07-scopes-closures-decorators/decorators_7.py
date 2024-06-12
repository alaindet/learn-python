"""
This files shows an example of a decorator factory created both via closures
(logger function) and via classes (Logger class)
"""

from functools import wraps


def logger(message: str):
    print('logger')

    def decorator(fn):
        print('logger.decorator')

        @wraps(fn)
        def inner(*args, **kwargs):
            print(message)
            return fn(*args, **kwargs)
        return inner
    return decorator


@logger('This is a lie')
def cake_with_fn_decorator():
    print('cake_with_fn_decorator: There will be cake.')


cake_with_fn_decorator()
cake_with_fn_decorator()
# logger
# logger.decorator
# This is a lie
# cake_with_fn_decorator: There will be cake.
# This is a lie
# cake_with_fn_decorator: There will be cake.


class Logger:
    def __init__(self, message: str):
        print('Logger.__init__')
        self.message = message

    def __call__(self, fn):
        print('Logger.__call__')

        @wraps(fn)
        def inner(*args, **kwargs):
            print(self.message)
            return fn(*args, **kwargs)
        return inner


@Logger('This is a lie')
def cake_with_class_decorator():
    print('cake_with_class_decorator: There will be cake.')


cake_with_class_decorator()
cake_with_class_decorator()
# Logger.__init__
# Logger.__call__
# This is a lie
# cake_with_class_decorator: There will be cake.
# This is a lie
# cake_with_class_decorator: There will be cake.
