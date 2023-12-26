"""\
Lambda Expressions
https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions

- Small anonymous functions can be created with the `lambda` keyword
- Lambda functions can be used wherever function objects are required
- They are syntactically restricted to a single expression
"""


def multiply(a, b):
    return a * b


# Assigning a lambda is not recommended, they just have to be used in place
lambda a, b: a * b  # <-- This is equivalent to `multiply`

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)
# [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

nums1 = [1, 2, 3, 4, 5]
# This returns an iterable, not a list directly!
doubles = map(lambda n: n*2, nums1)
print(doubles)  # <map object at 0x000002350CCFB550>
print(list(doubles))  # [2, 4, 6, 8, 10]

nums2 = [1, 2, 3, 4, 5]
doubles1 = list(map(lambda n: n*2, nums2))  # With list(), map() and lambdas
doubles2 = [n*2 for n in nums2]  # With list comprehension
print(doubles1, doubles2)  # [2, 4, 6, 8, 10] [2, 4, 6, 8, 10]

# Another examples
people = [
    {'name': 'Alice'},
    {'name': 'Bob'},
    {'name': 'Charlie'},
]

names1 = list(map(lambda p: p['name'], people))
names2 = [p['name'] for p in people]
# Prints ['Alice', 'Bob', 'Charlie'] ['Alice', 'Bob', 'Charlie']
print(names1, names2)

# Combining map(), filter() and list()
people = [
    {'email': 'alice@example.com', 'activities': 2},
    {'email': 'bob@example.com', 'activities': 0},
    {'email': 'charlie@example.com', 'activities': 1},
    {'email': 'deliah@example.com', 'activities': 0},
]

inactive_people = list(
    map(
        lambda p: p['email'],
        filter(lambda p: p['activities'] == 0, people),
    ),
)
print(inactive_people)  # ['bob@example.com', 'deliah@example.com']

# Equivalent, more concise and readable
inactive_people2 = [p['email'] for p in people if p['activities'] == 0]
print(inactive_people2)
