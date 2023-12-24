from typing import Callable


def generic_salute():
    """Example: Accepts nothing, returns nothing"""
    print('Hello to all!')


def salute(name: str) -> None:
    """Example: Accepts an argument"""
    print(f'Hello, {name}')


def get_answer() -> int:
    """Example: Accepts nothing, returns something"""
    return 42


def exponentiate(num: int, power=2) -> int:
    """Example: Default parameter"""
    return num ** power


def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def run_operation(
    a: int,
    b: int,
    operation_fn: Callable[[int | float, int | float], int | float] = add,
) -> int | float:
    """Example: accept a function as arg, defaults to a fallback function"""
    return operation_fn(a, b)


print(run_operation(2, 3, add))  # 5
print(run_operation(2, 3, subtract))  # -1
print(run_operation(2, 3, lambda a, b: a * b))  # 6
print(run_operation(2.1, 3.2, lambda a, b: a ** b))  # 10.74241047739471
