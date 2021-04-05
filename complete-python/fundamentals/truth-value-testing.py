"""
https://docs.python.org/3/library/stdtypes.html#truth-value-testing

Truth Value Testing
Any object can be tested for truth value, for use in an if or while condition or as operand of the Boolean operations below.

By default, an object is considered true unless its class defines either a __bool__() method that returns False or a __len__() method that returns zero, when called with the object. 1 Here are most of the built-in objects considered false:

- constants defined to be false: None and False.
- zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
- empty sequences and collections: '', (), [], {}, set(), range(0)
"""

from textwrap import dedent

print(
    dedent(
      f"""
        True is {bool(True)}
        1 is {bool(1)}
        'foo' is {bool('foo')}
        (0,) is {bool((0,))}
        0, is {bool(0,)}

        ===============
        
        False is {bool(False)}
        None is {bool(None)}
        0 is {bool(0)}
        0.0 is {bool(0.0)}
        0j is {bool(0j)}
        '' is {bool('')}
        () is {bool(())}
        [] is {bool([])}
        {{}} is {bool({})}
        set() is {bool(set())}
        range(0) is {bool(range(0))}
      """
    )
)
