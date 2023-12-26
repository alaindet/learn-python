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
