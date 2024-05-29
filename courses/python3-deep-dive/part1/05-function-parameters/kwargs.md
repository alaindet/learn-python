# `**kwargs`

- Functions can use extended unpacking for dictionaries to capture all keyword
arguments provided to the function
- Conventionally, the variable for unpacking keyword arguments is `**kwargs`
- The `*` character in the arguments list is not an arguments, it just represents the _end_ of positional arguments
- `**kwargs` can be used even if positional arguments are not exhausted
- There cannot be any other argument after `**kwargs`
- WARNING: To define keyword-only arguments you must exhaust positional arguments
first, by either using `*args` or the `*` separator in the function signature

## Building a function signature in Python

```py
# This is pseudo Python code

# - Two mandatory positional args
# - Variadic optional positional args
# - One mandatory keyword arg
def fn(a, b, *args, d)

# - Variadic optional positional args
# - One mandatory keyword arg
def fn(*args, d)

# - No positional args allowed
# - One mandatory keyword arg
def fn(*, d)

# - One mandatory positional arg
# - Variadic optional positional args
# - One mandatory keyword arg
# - One optional keyword arg
def fn(a, *args, b, c=42)

# - One mandatory keyword arg
# - Variadic optional keyword args
def fn(*, d, **kwargs)

# - Variadic optional keyward args
# NOTE:  There's no need of using the positional arg delimiter *
def fn(**kwargs)

# - Variadic optional positional args
# - Variadic optional keyward args
def fn(*args, **kwargs)
```