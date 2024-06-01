"""
A Callable is, simply, anything that can be called via parentheses
- A function is callable
- A method is a callable
- An object implementing .__call__ is a callable
- The built-in callable() function returns a boolean telling you if the arg is callable
"""

print(callable(print))  # True
print(callable(id))  # True
print(callable('foo'.upper))  # True
print(callable(str.upper))  # True
print(callable(callable))  # True

print(callable(42))  # False
print(callable('bar'))  # False


class MySum:
    _inner = 10

    def __init__(self, inner: int):
        self._inner = inner

    @property
    def inner(self) -> int:
        return self._inner

    def __call__(self, n: int) -> int:
        return self._inner + n


sum_five = MySum(5)
print(callable(MySum))  # True
print(callable(sum_five))  # True

# These are equivalent. One is ugly though
print(sum_five(2))  # 7
print(sum_five.__call__(2))  # 7
