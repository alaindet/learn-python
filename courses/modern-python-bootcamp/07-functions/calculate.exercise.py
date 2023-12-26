from typing import Callable

"""\
Write a function called "calculate" that accepts a list of keyword arguments
- "make_float", a boolean which returns a float if True or an integer if False
- "operation", either 'add', 'subtract', 'multiply', or 'divide'
- "first", a number
- "second", another number
- "message", a string that can be added

The function should return the result of actually running the specified operation
with the first and second keyword arguments. The result of the operation with
the first and second is an integer if the make_float keyword argument is False,
otherwise the result of the operation is a float.

If a message is specified, it should return the message keyword argument plus
the result of the operation. Otherwise, it should return the string "The result
is " joined with the result of the operation.

Examples
calculate(make_float=False, operation='add', message='You just added', first=2, second=4)
# 'You just added 6'

calculate(make_float=True, operation='divide', first=3.5, second=5)
# 'The result is 0.7'
"""


def parse_int(n: int) -> int:
    return int(n)


def parse_float(n: int) -> float:
    return float(n)


def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: int, b: int) -> float:
    return a / b


def calculate(**kwargs) -> str | None:

    prefix = 'The result is'
    if 'message' in kwargs:
        prefix = kwargs['message']

    parser = parse_int
    if 'make_float' in kwargs and kwargs['make_float']:
        parser = parse_float

    operation: str | None = None
    if 'operation' in kwargs:
        operation = kwargs['operation']

    if operation is None:
        return None

    operation_fn: Callable[[int, int], int | float] = None
    match operation:
        case 'add':
            operation_fn = add
        case 'subtract':
            operation_fn = subtract
        case 'multiply':
            operation_fn = multiply
        case 'divide':
            operation_fn = divide
        case _:
            operation_fn = None

    if operation_fn is None:
        return None

    a = kwargs['first']
    b = kwargs['second']

    result = operation_fn(a, b)
    parsed_result = parser(result)

    return f'{prefix} {parsed_result}'


print(
    calculate(
        make_float=False,
        operation='add',
        message='You just added',
        first=2,
        second=4,
    )
)
# 'You just added 6'

print(
    calculate(
        make_float=True,
        operation='divide',
        first=3.5,
        second=5,
    )
)
# 'The result is 0.7'
