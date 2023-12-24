"""\
Tuples and sequences
https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences

A tuple is a sequence data type, like lists and strings.
- Tuples are used to represent eterogeneous *IMMUTABLE* data, like a SQL table row
- Lists are mutable and tend to have the same type for each element
- Tuples are frequently unpacked by assignment
- Tuples are usually faster than lists (TODO: loaded in stack and not heap?)
- Since tuples are immutable, they can be used as keys of a dictionary!
"""

# Packing values into a tuple
t1 = 'John', 30, 1234567

# Creating an empty tuple
an_empty_tuple = ()

# Creating a 1-element tuple has a strange syntax
one_element_tuple = 42,  # <-- Mind the comma!

# Creating a tuple via tuple() from a list!
t2 = tuple([n**2 for n in range(5)])
print(t2)  # (0, 1, 4, 9, 16)

# Unpacking a tuple
name, age, social_id = t1

# Check if a value exists in a tuple
print(30 in t1)  # True

try:
    t1[0] = 'Jane'
except TypeError:
    print('You cannot mutate a tuple!')

# We can change a value *inside* a tuple though!
t2 = {'a': 1}, 123
t2[0]['a'] = 2
print(t2)  # ({'a': 2}, 123)

# Let's use tuples as keys of a dictionary
d1 = {t1: 111, 'something_else': 222}
print(d1)  # {('John', 30, 1234567): 111, 'something_else': 222}

# Please note: tuples can be used as dict keys ONLY if they contain simple values
# and/or tuples. No compound types (like lists, dicts) can live inside key tuples

# An actually good example of tuples as keys: geographic coordinates
offices = {
    (35.68387, 139.76938): 'Tokyo',
    (41.90244, 12.49203): 'Roma',
    (40.70878, -73.99606): 'New York',
}

# Indexing works exactly like lists
print(t1[0], t1[-1])  # John 1234567

# Slicing works the same as well
print(t1[::-1])  # (1234567, 30, 'John')

# Loops are the same as lists
names = ('Foo', 'Bar', 'Baz')

for name in names:
    print(name)
