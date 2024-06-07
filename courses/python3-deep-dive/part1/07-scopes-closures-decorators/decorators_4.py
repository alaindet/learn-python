"""
This example shows how to use stacked decorators and how to parametrize decorators
"""

def logger(message: str):
    from functools import wraps

    def decorator(fn):

        @wraps(fn)
        def inner(*args, **kwargs):
            print(message)
            return fn(*args, **kwargs)

        return inner

    return decorator

@logger('Foo')
@logger('Bar')
@logger('Baz')
def dummy():
    print('Dummy')

# Prints
# Foo
# Bar
# Baz
# Dummy
dummy()

# Here is the equivalent example without the @ syntax
def dummy2():
    print('Dummy 2')

dummy2 = logger('Foo')(logger('Bar')(logger('Baz')(dummy2)))

# Prints
# Foo
# Bar
# Baz
# Dummy
dummy()