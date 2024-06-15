# Parentheses are optional for tuples in most occasions (except with tuples used
# as function arguments for example)
from math import sqrt
from random import uniform


london = ('London', 'UK', 8_780_000)
new_york = 'New York', 'USA', 8_500_000

# Unpacking
name, state, population = london

# Unpacking only first
name, *_ = london

# Unpacking only last
*_, population = london

# Somewhat realistic results from a database query: a list of tuples
cities = [
    ('London', 'UK', 8_780_000),
    ('New York', 'USA', 8_500_000),
    ('Beijing', 'China', 21_000_000),
]

# You can do meaningful unpacking since order is guaranteed in a tuple
for name, state, population in cities:
    print({
        'name': name,
        'state': state,
        'population': population,
    })

# Only print names
for name, *_ in cities:
    print(name)

# Sum populations
total = 0
for *_, population in cities:
    total += population

print(total) # 38_280_000

# Better
# total = sum([city[2] for city in cities])
total = sum(city[2] for city in cities) # Equivalent without square brackets
print(total) # 38_280_000


def random_shot(radius):
    """
    This simulates a random shot in a square of side = 2 * radius and checks if
    the shot hit the circle inscribed in the square or not. If called many times,
    the hits / attemps ratio approximates to PI/4
    """
    random_x = uniform(-radius, radius)
    random_y = uniform(-radius, radius)
    in_circle = sqrt(random_x ** 2 + random_y ** 2) <= radius

    return random_x, random_y, in_circle

attempts = 100_000
hits = 0
radius = 1
for i in range(attempts):
    *_, in_circle = random_shot(radius)
    if in_circle:
        hits += 1

print(f'PI appromixation: {4 * hits / attempts}')
# Multiple runs for 100_000 attemps
# 3.13256
# 3.13196
# 3.13916
# 3.14484
# 3.13800
# 3.13980
# 3.13196
# 3.14980
# AVERAGE = 3.13851