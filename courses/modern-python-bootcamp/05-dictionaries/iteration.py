person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'favorite_color': 'blue',
}

# Loop on values
for val in person.values():
    print(val)

# Loop on keys
for key in person.keys():
    print(key)

# Looping on both
# Please note: items() returns a list of tuples (key, value)
for key, val in person.items():
    print(key, val)

# Please note:
# Python 3.7+ guarantees order of items in dict is the same as
# insertion order
