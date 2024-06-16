from collections import namedtuple

# With a simple tuple
person = ('John Titor', 1998)

# Unpackgin works, but order is paramount here and you're forced to use unpacking
# to have readable tuples
name, birth_year = person

# Creating a named tuple
Person = namedtuple('Person', ['name', 'birth_year'])
# Person = namedtuple('Person', ('name', 'birth_year')) # Equivalent 1
# Person = namedtuple('Person', 'name,birth_year') # Equivalent 2
# Person = namedtuple('Person', 'name birth_year') # Equivalent 3
p1 = Person('John Titor', 1998)
print(p1) # Person(name='John', birth_year=1998)
p2 = Person(name='John Titor', birth_year=1998)
print(p2) # Person(name='John Titor', birth_year=1998)
print('Are people equal?', p1 == p2) # True
print('is namedtuple a tuple?', isinstance(p1, tuple)) # True

print(p1.name, p2.birth_year) # John 1990

# Map to a dictionary
print('As a dictionary', p1._asdict()) # {'name': 'John Titor', 'birth_year': 1998}