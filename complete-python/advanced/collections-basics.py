"""
Collections summary
- Counter
- defaultdict
- ordereddict
- namedtuple
- deque
"""

from collections import Counter, defaultdict, OrderedDict, namedtuple, deque

print('\nCounter')
device_temp = [13.5, 14.0, 14.0, 14.5, 14.15, 14.5, 15.0, 16.0]
temp_counters = Counter(device_temp)
print(temp_counters)

print('\ndefaultdict')
coworkers = [
    ('Alice', 'MIT'),
    ('Alice', 'Princeton'),
    ('Bob', 'Oxford'),
    ('Charlie', 'Harvard'),
    ('Charlie', 'Berkeley'),
]

# defaultdict accepts a function called "default_factor" and runs it
# if accessing a non-existing attribute of returned dictionary
alma_maters = defaultdict(list)

for coworker, university in coworkers:
    alma_maters[coworker].append(university)

# This removes the default_factory and raises an error
# if accessing a non-existing attribute of dictionary
# alma_maters.default_factory = None

print(alma_maters['Alice'])
# Prints an empy list as for alma_maters.default_factory
print(alma_maters['Darlene'])

# Equivalent
alma_maters = {}
for coworker, university in coworkers:
    if coworker not in alma_maters:
        alma_maters[coworker] = []
    alma_maters[coworker].append(university)

print(alma_maters)

my_company = 'Acme Inc.'

coworkers = (
    'Jen',
    'Li',
    'Charlie',
    'Rhys'
)

other_coworkers = [
    ('Rolf', 'Apple Inc.'),
    ('Anna', 'Google'),
]

coworker_companies = defaultdict(lambda: my_company)

for person, company in other_coworkers:
    coworker_companies[person] = company

print(coworker_companies[coworkers[0]])  # Print default company
print(coworker_companies['Rolf'])


# Not much used since Python 3.7 has ordered dictionaries
print('\nOrderedDict')
ordered = OrderedDict()
ordered['Alice'] = 4
ordered['Bob'] = 35
ordered['Charlie'] = 2
ordered.move_to_end('Alice')
# Weird, moves to the "other end" aka the beginning
ordered.move_to_end('Bob', last=False)
ordered.popitem()  # Removed 'Alice'
print(ordered)


print('\nnamedtuple')

Account = namedtuple('Account', ['name', 'balance'])

# Example: Create a named tuple from arguments
# account = Account('checking', 1850.90)

# Alternative 1: Create a named tuple from a non-named tuple
# unnamed_tuple = ('checking', 1850.90)
# account = Account._make(unnamed_tuple)

# Alternative 2: Create a named tuple via list unpacking
my_list = ('checking', 1850.90)
account = Account(*my_list)

# account = Account('checking', balance=1850.90) # Alternative
print(account.name)
print(account.balance)
print(account._asdict()) # Cast named tuple as dictionary

# # Equivalent
# account = ('checking', 1850.90)
# print(account[0])
# print(account[1])

# Double-ended queue
# Thread-safe, efficient
print('\ndeque')
people_tuple = ('Alice', 'Bob', 'Charlie', 'Darlene', 'Eric')
people = deque(people_tuple)

# On the right
people.append('Frank')
people.pop()

# On the left
people.appendleft('Zachary')
people.popleft()
