from typing import List, Dict, Union

# Declaring a type
Book = Dict(str, Union(str, int))


def do_nothing() -> None:
    pass


def do_something() -> List[Book]:
    return [
        {
            'id': 1,
            'name': 'Foo',
        },
        {
            'id': 2,
            'name': 'Bar',
        }
    ]


def my_multiply(a: int, b: int) -> int:
    return a * b


print(do_nothing())
print(do_something())
print(my_multiply(3, 5))
