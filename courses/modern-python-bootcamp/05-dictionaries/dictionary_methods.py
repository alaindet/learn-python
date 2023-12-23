person = {
    'name': 'John',
    'age': 30,
}

# Clear everything!
person.clear()
print(person)  # Prints {}

# Create a shallow copy of a dictionary
d1 = dict(a=1, b=2, c=3)
d2 = d1.copy()
print(d1 == d2)  # True d1 and d2 are equal
print(d1 is d2)  # False d1 and d2 are not identical
d3 = d1
print(d1 is d3)  # True d1 and d3 are identical as they point to the same dict

# Create a dictionary from a list of keys
# Prints {'a': [1, 2, 3], 'b': [1, 2, 3], 'c': [1, 2, 3]}
print({}.fromkeys(['a', 'b', 'c'], [1, 2, 3]))

# Defaults all keys to None
# Prints {'a': None, 'b': None, 'c': None, 'd': None}
print({}.fromkeys(['a', 'b', 'c', 'd'], None))

print(person.get('name'))  # Prints 'John'
print(person.get('nope'))  # Prints None without raising a KeyError
