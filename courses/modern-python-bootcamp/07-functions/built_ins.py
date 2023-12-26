"""\
Python built-in functions (as of Python 3.12)
https://docs.python.org/3/library/functions.html#built-in-functions

Built-in Functions (71)

A               E               L               R
abs()           enumerate()     len()           range()
aiter()         eval()          list()          repr()
all()           exec()          locals()        reversed()
anext()                                         round()
any()           F               M           
ascii()         filter()        map()           S
                float()         max()           set()
B               format()        memoryview()    setattr()
bin()           frozenset()     min()           slice()
bool()                                          sorted()
breakpoint()    G               N               staticmethod()
bytearray()     getattr()       next()          str()
bytes()         globals()                       sum()
                                O               super()
C               H               object()
callable()      hasattr()       oct()           T
chr()           hash()          open()          tuple()
classmethod()   help()          ord()           type()
compile()       hex()                           
complex()                       P               V
                I               pow()           vars()
D               id()            print()         
delattr()       input()         property()      Z
dict()          int()                           zip()
dir()           isinstance()                    
divmod()        issubclass()                    _
                iter()                          __import__()
"""

from typing import List

# Examples for map()
nums = [1, 2, 3, 4, 5]
# Note: map() returns an iterator, which has to be exhausted and converted into
# a list via list() built-in function
doubled = list(map(lambda n: n*2, nums))
doubled_lc = [n*2 for n in nums]
print(doubled, doubled_lc)  # [2, 4, 6, 8, 10] [2, 4, 6, 8, 10]

# Silly example demonstrating the iterable
for n in map(lambda n: n+1, range(10)):
    print(n)

# Examples for filter()
odds = list(filter(lambda n: n % 2 == 1, nums))
odds_lc = [n for n in nums if n % 2 == 1]
print(odds, odds_lc)  # [1, 3, 5] [1, 3, 5]

# Examples for all() and any()
people = [
    {'name': 'Alice', 'activities': 2},
    {'name': 'Bob', 'activities': 0},
    {'name': 'Charlie', 'activities': 1},
    {'name': 'Deliah', 'activities': 0},
]
are_all_active = all([p['activities'] for p in people])
print(are_all_active)  # False, since Bob and Deliah have 0 activities
are_inactives = any([not p['activities'] for p in people])
print(are_inactives)  # True

are_any_odds = any([n % 2 == 1 for n in [1, 2, 3, 4, 5]])
print(are_any_odds)  # True

are_all_odds = all([n % 2 == 1 for n in [1, 3, 6, 7, 9]])
print(are_all_odds)  # False, because 6 is even

# Examples for sorted() - Sorts a copy of a sequence and returns it
nums2 = [4, 1, 5, 3, 2]
nums3 = sorted(nums2)
print(nums2)  # [4, 1, 5, 3, 2]
print(nums3)  # [1, 2, 3, 4, 5]
print(sorted(nums2, reverse=True))  # [5, 4, 3, 2, 1]
print(sorted((3, 69, 42, 2)))  # [2, 3, 42, 69]

# Prints
# Alice has 2 activities
# Charlie has 1 activities
active = [p for p in people if p['activities'] != 0]
most_active = sorted(active, key=lambda p: p['activities'], reverse=True)
for person in most_active:
    print(f"{person['name']} has {person['activities']} activities")

# Examples for min() and max()
print(max(1, 42, 2))  # 42
print(max([99, 3, 4]))  # 99
print(max('hello', 'world'))  # world

print(min(1, 42, 2))  # 1
print(min([99, 3, 4]))  # 3
print(min('hello', 'world'))  # hello

# Custom value
names = [p['name'] for p in people]
shortest_names = min(len(name) for name in names)
print(shortest_names)  # 3 (the shortest name, which is 'Bob')

# This is much better since the key allows you to transform and compare data
# Without altering it, or creating a generator
longest_names = max(names, key=lambda name: len(name))
print(longest_names)  # Charlie


def is_palindrome(sentence: str) -> bool:
    """An example of reversed() usage"""
    s_normal = sentence.strip().lower().replace(' ', '')
    s_reversed = ''.join(reversed(s_normal))
    return s_normal == s_reversed


print(is_palindrome('I Topi Non Avevano Nipoti'))  # True

for n in reversed(range(3)):
    print(n)  # Prints 2, then 1, then 0


# Examples for len() - Works on any sequence type!
# Prints 5 4 4 5 4 2
print(
    len('hello'),  # Works on strings
    len((1, 2, 3, 4)),  # Works on tuples
    len([1, 2, 3, 4]),  # Works on lists
    len(range(5)),  # Works on range objects
    len({1, 2, 3, 4}),  # Works on sets
    len({'foo': 1, 'bar': 2}),  # Works on dictionaries
)

# len() just calls .__len__() dunder method on given objects, really
# Prints 5 5
print(
    len('hello'),
    'hello'.__len__(),  # Equivalent
)


class DeckOfCards:

    def __init__(self, data):
        self.data = data

    def __len__(self) -> int:
        """Note: we're implementing __len__ so calling len() on DeckOfCards works"""
        return len(self.data)

    def __str__(self) -> str:
        """Note: we're implementing __str__ so DeckOfCards can be converted to str"""
        return f'The deck has {self.__len__()} cards'


deck = DeckOfCards([c for c in range(52)])
print(len(deck))  # Prints 52
print(deck)  # Prints 'The deck has 52 cards'

# Examples for abs(), sum() and round()
print(abs(-5), abs(42))  # 5 42

print(
    sum((1, 2, 3, 4)),
    sum([1, 2, 3, 4]),
    sum(range(1, 5)),
    sum([1, 2, 3, 4], start=10),
    sum([1, 2, 3, 4], 20),
)  # 10 10 10 20 30

print(round(10/3))  # 3
print(round(20/3))  # 7
print(round(20/3, ndigits=5))  # 6.66667
print(round(20/3, 3))  # 6.667

# Examples for zip()
# Loops in parallel on 2+ sequences and returns a tuple with all current loop
# items from each sequence

scores = [7, 6, 9, 7, 10, 5, 8]
letters = 'abcdefg'

for letter, score in zip(letters, scores):
    print(f'Letter: {letter}, Score: {score}')
    # Letter: a, Score: 7
    # Letter: b, Score: 6
    # Letter: c, Score: 9
    # Letter: d, Score: 7
    # Letter: e, Score: 10
    # Letter: f, Score: 5
    # Letter: g, Score: 8

# Prints{'a': 7, 'b': 6, 'c': 9, 'd': 7, 'e': 10, 'f': 5, 'g': 8}
scores_registry = {letter: score for letter, score in zip(letters, scores)}
print(scores_registry)

# Note: zip() stops at the shortest sequence, if sequences have different lengths
word1 = 'abcdefghi'
word2 = 'abcdef'
# Prints ['aa', 'bb', 'cc', 'dd', 'ee', 'ff'] <-- Notice 'ghi' from word1 are ignored
print([f'{l1}{l2}' for l1, l2 in zip(word1, word2)])

# Advanced zip() example
students = ['Alice', 'Bob', 'Charlie']
midterms = [80, 91, 78]
finals = [98, 89, 53]

highest_scores = {s: max(m, f) for s, m, f in zip(students, midterms, finals)}
print(highest_scores)  # {'Alice': 98, 'Bob': 91, 'Charlie': 78}


def avg(*args: List[int]) -> float:
    return sum(args) / len(args)


avg_scores = {s: avg(m, f) for s, m, f in zip(students, midterms, finals)}
print(avg_scores)
