class FirstHundredGenerator:
    """
    This is a class generator
    You don't need the "yield" keyword on the __next__ method
    """

    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

g = FirstHundredGenerator()

# These...
# print(next(g))
# print(next(g))

# Are equivalent to these...
# print(g.number)
# g.__next__()
# print(g.number)

try:
    while True:
        print(next(g))
except StopIteration:
    print('FirstHundredGenerator stopped')

"""
# NOTES

- All objects having __next__ are ITERATORS
- All GENERATORS are ITERATORS
- Not all iterators are generators
- Iterables and iterators are not the same thing
"""

class FirstFiveIterator:
    """
    This is an iterator that is not a generator
    """
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5]
        self.i = 0
    
    def __next__(self):
        if self.i < len(self.numbers):
            current = self.numbers[self.i]
            self.i += 1
            return current
        else:
            raise StopIteration()