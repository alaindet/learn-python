people = (
    {
        'name': 'Alice',
        'location': 'Washington, D.C.'
    },
    {
        'name': 'Bob',
        'location': 'San Francisco'
    },
    {
        'name': 'Charlie',
        'location': 'San Francisco'
    },
    {
        'name': 'Darlene',
        'location': 'San Francisco'
    },
)

location = input('Where are you? > ')

people_nearby = tuple(prsn for prsn in people if location in prsn['location'])

# Alternative 1
# if len(people_nearby) > 0:
#     print('You are not alone')
# else:
#     print('No one that I know of is nearby')

# Alternative 2
# "any" casts every element of a list or a tuple as a boolean then returns True
# if any value is truthy, otherwise returns False 
if any(people_nearby):
    print('You are not alone')
else:
    print('No one that I know of is nearby')

"""
# Falsy values

0
0.0
None
[]
()
{}
False
"""

# All
# Returns True only if all elements of a list or a tuple are truthy

print(all([1, 2, 3])) # True
print(all(('hello', False, 'world'))) # False
