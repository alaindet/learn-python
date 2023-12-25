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

vowels = 'aeiouAEIOU'


def contains_vowels(sentence: str) -> bool:
    """\
    This function uses a global variable
    Please note that the "global" keyword is only needed when writing on a global
    variable, but if you only need to read it, there's no need for "global"
    It's still considered better to explicitly refer to global variables via "global",
    although using global variables in functions is not recommended at all
    """
    global vowels  # <-- Look at this!

    for letter in sentence:
        if letter in vowels:
            return True

    return False


print(contains_vowels('xyz'), contains_vowels('HOLA'))  # False True


def create_counter(initial_value=0) -> Callable[[], int]:
    """\
    Here is an example usage for the "nonlocal" keyword. "nonlocal" allows you to
    write on a variable taken from a parent scope, which is not global. Like this
    example, it could be a closure accesing the parent's scope
    """
    counter = initial_value

    def increment_counter() -> int:
        nonlocal counter  # <-- Look at this!
        counter += 1
        return counter

    return increment_counter


c = create_counter(42)
print(c())  # 43
print(c())  # 44


def dummy_fn() -> None:
    """This is just a dummy function"""
    return None


# You can actually access many properties of functions as they're objects
# For example, .__doc__ prints the function's docstring
print(dummy_fn.__doc__)  # This is just a dummy function
