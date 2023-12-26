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
