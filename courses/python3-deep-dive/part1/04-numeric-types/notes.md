# Numbers

- There are five numeric types in Python

## `bool`
- Only has `True` (1) and `False` (0) constants

```python
print(True + True) # 2
# LOL
```

## `int`
All integers, including negative ones, are of `int` type

## `fractions.Fraction`
The `Fraction` type coming from the `fractions` module (https://docs.python.org/3/library/fractions.html), from the docs

> A Fraction instance can be constructed from a pair of integers, from another rational number, or from a string

## `float`
Standard floating-point decimals, they are fast but not precise. From WikiPedia

> Floating-point arithmetic operations, such as addition and division, approximate the corresponding real number arithmetic operations by rounding any result that is not a floating-point number itself to a nearby floating-point number

## `decimal.Decimal`
Comes from the `decimal` module (https://docs.python.org/3/library/decimal.html) and represents decimals in a precise way. From the docs

> The decimal module provides support for fast correctly rounded decimal floating point arithmetic.

## `complex`
Represents a complex number, ex.:

```python
print(10 + 5j, type(10 + 5j))
# (10+5j) <class 'complex'>
```