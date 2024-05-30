# First-class functions

## First-class
Any first-class object (like an `int` or a `list`), including *functions*, meets
these criteria
- Can be passed as a function argument
- Can be returned from a function
- Can be assigned to a variable
- Can be stored in a data structure (ex.: in a list, tuple or dict)

## Higher-order functions
- Can take a function as argument
- Can return a function

## Docstrings
- A docstring serves as a documentation for a given function
- The docstring is represented as the first unassigned string declared in a function
- Typically, it is declared as a multi-line string literal via triple quotes
- It is stored in the `.__doc__` property of the function object as a string
- It is usually shows on IDE tooltips to quickly document a function
- Bear in mind that indentation of the multi-line string is preserved!
- Docstrings are also used by the `help()` built-in function

```py
def my_func():
    """This is a docstring that's supposed to explain what this function does.
    You can easily add a new line if needed, with triple quotes"""
    pass

print(my_func.__doc__) # This is a docstring [...]

help(my_func)
# my_func()
#     This is a docstring that's supposed to explain what this function does.
#     You can easily add a new line if needed, with triple quotes
```

## Annotations
- Function parameters and the return value can be typed via annotations
- Annotations are stored in the function object in the `__annotations__` property
as dictionary
- As of Python 3.12, they *do not* affect runtime, meaning you can pass an `int`
to a parameter typed as `str` and that's ok, although IDEs are going to complain

```py
def my_func(a: str, b: int) -> None:
    pass

print(my_func.__annotations__)
# {'a': <class 'str'>, 'b': <class 'int'>, 'return': None}
```

- A non-annotated function just has an empty dictionary for `.__annotations_-`

```py
def my_func(a, b):
    pass

print(my_func.__annotations__) # {}
```