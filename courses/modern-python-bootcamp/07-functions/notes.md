# Functions

## Parameter vs argument
- A parameter is a the variable you're using inside a function
- An argument is something you pass to the function from outside of its definition
- When you call a function, you pass arguments, which become parameters while the function runs

## Arguments and Parameters
- Arguments in Python functions can be defined  as *keyword-only*, *positional-only* or both
- An argument is a value passed to a function when executing it
- A parameter is a local variable scoped to the function that temporarily gets
  the argument's value when executing the function

### `*args`
- `*args` is a conventional function parameter
- It can be named with anything starting with `*`, like `*numbers`
- It gathers all remaining arguments into one single tuple
- It's like variadic functions in other languages

```py
def sum_all(*nums: List[int]) -> int:
    result = 0
    for n in nums:
        result += n
    return result

print(sum_all(1, 2, 3, 4))  # 10
print(sum_all(11, 22, 33, 44, 55, 66))  # 231
```

### `**kwargs`
- `**kwargs` stands for **keyword arguments**
- It gathers all remaining arguments into one single dictionary
- Like `*args`, it can be named with anything starting with `**`, like `**info`

```py
def favorite_colors(**kwargs):
    for person, color in kwargs.items():
        print(f'{person.capitalize()}\'s favorite color is {color.capitalize()}')

favorite_colors(foo='red', bar='green', baz='blue')
# Foo's favorite color is Red
# Bar's favorite color is Green
# Baz's favorite color is Blue
```

### Parameters order
1. Parameters
2. `*args`
3. Default parameters
4. `**kwargs`