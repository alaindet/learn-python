# Tuples

| Tuples           | Lists            | Strings       | 
| ---------------- | ---------------- | ------------- |
| order matters    | order matters    | order matters |
| hetero/homo type | hetero/homo type | homo type     |
| indexable        | indexable        | indexable     |
| iterable         | iterable         | iterable      |
| immutable        | mutable          | immutable     |

## Named tuples

- It's a data structure fit for representing immutable data as tuples, with the
added efficiency of giving names to tuple values
- Using a class is easier, but a class has methods, mutable state, inheritance
and much more things you don't need if you only want to make tuples more readable
- Also, classes lead to more boilerplate, like being forced to implement `__repr__`
to say the least, maybe also `__eq__` and `__lt__`
- A `namedtuple()` is class factory function returning a specialized subclass of `tuple` with a name and named properties
- By convention, a named tuple name should be the same as its variable name
- Fields can be passed as any `Iterable`, so
  - As a list of strings (ex.: `['name', 'age']`)
  - As a tuple of strings (ex.: `('name', 'age')`)
  - As a string with comma-separated fields (ex.: `'name,age')`)
  - As a string with whitespace-separated fields (ex.: `'name age')`)
- **BEWARE!**: you cannot use strings starting with underscore for fields, ex.: `'name, _age'` raises an error `ValueError: Field names cannot start with an underscore`


```py
Person = namedtuple('Person', ['name', 'birth_year'])
p = Person('John', 1990)
print(p) # Person(name='Alain', birth_year=1990)
```