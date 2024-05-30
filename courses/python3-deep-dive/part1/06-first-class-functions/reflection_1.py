def my_func(a: int, b: int) -> int:
    return a + b


# You can (but should you?) attach properties to a function object
# Then, you can read it via introspection/reflection
my_func.category = 'math'
my_func.subcategory = 'arithmetic'

print({
    '__doc__': my_func.__doc__,
    '__annotations__': my_func.__annotations__,
    'category': my_func.category,
    'subcategory': my_func.subcategory,
})
# {
#     '__doc__': None,
#     '__annotations__': {
#         'a': <class 'int'>,
#         'b': <class 'int'>,
#         'return': <class 'int'>
#     },
#     'category': 'math',
#     'subcategory': 'arithmetic'
# }

# The dir() built-in function returns the list of valid attributes for given object
print(dir(my_func))
# Note: there are currently 36 dunder attributes plus custom-defined attributes
# like 'category' and 'subcategory'
#
# Prints
# ['__annotations__', '__builtins__', '__call__', '__class__', '__closure__',
# '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__getstate__',
# '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__',
# '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__',
# '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__',
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'category',
# 'subcategory']

# The function name => 'my_func'
print(my_func.__name__)  # my_func

# Tuple with default for pos args
print(my_func.__defaults__)  # None

# Tuple with default for kwargs
print(my_func.__kwdefaults__)  # None

# Instance of "code" type, which has many attributes, like
# - co_varnames => Tuple with list of param names
# - co_argcount => Number of params without *args and **kwargs
print(my_func.__code__.co_varnames)  # ('a', 'b')
print(my_func.__code__.co_argcount)  # 2

# To make reflection easier, use the "inspect" module
