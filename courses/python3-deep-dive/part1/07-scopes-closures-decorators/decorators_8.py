"""
Monkey patching means to add or change behavior of a given class or function at
runtime
"""

from fractions import Fraction

# Monkey patching in action
Fraction.speak = lambda self, msg: f'Fraction says: {msg}'
f = Fraction(3, 7)
print(f.speak('Hi there, I am 3/7')) # Fraction says: Hi there, I am 3/7

# Monkey patching again
Fraction.is_integral = lambda self: self.denominator == 1
f2 = Fraction(42, 1)
print(f'Is {f2} integral? {f2.is_integral()}') # Is 42 integral? True

# Monkey patching with a decorator
def decorate_with_speak(cls):
    cls.speak = lambda self, msg: f'Decorator: {cls.__name__} says: {msg}'
    return cls

Fraction = decorate_with_speak(Fraction)
f3 = Fraction(5, 8)
print(f3.speak('Hello there')) # Decorator: Fraction says: Hello there
print(f.speak('Hi there, I am 3/7')) # Decorator: Fraction says: Hi there, I am 3/7


class Person:
    pass