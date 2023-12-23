"""\
https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
"""

# Here's one way to create a literal dictionary
person = {
    'name': 'John',
    'age': 30,
}

# Or you can use keyword arguments passed to dict()
same_person = dict(name='John', age=30)

# You can also do this cool thing
same_person_again = dict([['name', 'John'], ['age', 30]])

# Accessing via a key
print(
    person['name'],
    same_person['name'],
    same_person_again['name'],
)

# Uh oh, the key does not exist!
try:
    print(person['favorite_color'])
except KeyError:
    print('Key "favorite_color" does not exist on person')

# Accessing a missing key, example 1
print('nope' in person)  # False

# Accessing a missing key, example 2
print(person.get('nope') is not None)  # False

people = [
    {
        'name': 'John',
        'age': 30,
    },
    {
        'name': 'Jane',
        'age': 28,
    },
]
