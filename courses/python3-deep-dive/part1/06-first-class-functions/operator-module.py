"""
The operator module is just a collection of convenient frequently used functions
so that you don't have to redefine them as lambdas every time. Functions include

- add(a, b)
- mul(a, b)
- pow(a, b)
- mod(a, b)
- floordiv(a, b)
- neg(a)
- lt(a, b)
- le(a, b)
- gt(a, b)
- ge(a, b)
- eq(a, b)
- ne(a, b)
- is_(a, b) # NOTE: this implements "a is b" expression as a function, mind the _
- is_not(a, b)

# These have a trailing underscore to differentiate them from the Python keywords
- and_(a, b)
- or_(a, b)
- not_(a, b)

- concat(a, b)
- contains(a, b) # Functional equivalent of "in"
- countOf(s, val) # Mind the camelCase
- getitem(s, i) # Returns index i of a sequence s
- setitem(s, i val) # Sets value val at index i of sequence s (mutable)
- delitem(s, i) # Removes element at index i of sequence s

# It's a partial: returns a function accepting a sequence and returning the i-th element
- itemgetter(i)

# It's a partial: returns a function returning attributes from objects
- attrgetter()
"""

import operator
from functools import reduce

# itemgetter
get_third_element = operator.itemgetter(2)
s = [1, 2, 3, 4]
print(get_third_element(s)) # 3

# itemgetter with multiple arguments
multi_getter = operator.itemgetter(1, 3, 5)
s = [11, 22, 33, 44, 55, 66, 77, 88, 99]
word = 'abcdefghi'
print(multi_getter(s)) # (22, 44, 66)
print(multi_getter(word)) # ('b', 'd', 'f')

class MyClass:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def foo(self, foo: str):
        print('MyClass.foo', self.a, self.b, self.c, foo)

d1 = MyClass(a=1, b=2, c=3)

# You can use getattr() to extract attributes via their literal name
print('getattr', getattr(d1, 'a')) # 1

agetter = operator.attrgetter('a')
print(agetter(d1)) # 1

multi_agetter = operator.attrgetter('a', 'c')
print(multi_agetter(d1)) # (1, 3)

# Inline
print(operator.attrgetter('b')(d1)) # 2

# Ugly but works
upper = operator.attrgetter('upper')
print(upper('hello')()) # HELLO

# With reduce
print(reduce(operator.mul, [1, 2, 3, 4])) # 24

# methodcaller()
foo = operator.methodcaller('foo', 'Hello')
foo(d1)