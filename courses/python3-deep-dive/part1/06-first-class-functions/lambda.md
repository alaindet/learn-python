# Lambda functions

- Lambda functions are usually one-liners representing an anonymous function
- Syntax is `lambda [parameters]: expression`
- The parameters are optional
- The evaluted expression is return as the return value of the function
- They're mostly used as one-off functions to be passed directly to higher-order
functions like `map()` and `filter()`


```py
lambda: 42 # Always returns 42 with no parameters
lambda n: n * 2 # Doubles a number
lambda a, b: a + b # Sums two numbers

doubler = lambda n: n * 2 # They can be assigned to variables

sum_factory = lambda a: lambda b: a + b # This is a lambda returning a lambda
sum_with_3 = sum_factory(3)
print(sum_with_3(5)) # 8
```

## Limitations
- You cannot assign anything inside a lambda
- You cannot have type annotations
- You must use one expression but you *can* use line continuation, although that
is frowned upon