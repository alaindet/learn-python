"""
- zip() Accepts multiple iterables and returns one iterable which has tuples
as elements
"""

list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]

zipped = zip(list1, list2)

print(zipped)  # <zip object at 0x0000022FA735E6C0>
print(list(zipped))  # [(1, 10), (2, 20), (3, 30), (4, 40)]

# Warning: zip will return an iterable whose length is equal to the SHORTEST
# iterables passed to zip()
zipped2 = zip(list1, list2, [100])
print(list(zipped2))  # [(1, 10, 100)]

zipped3 = zip([6, 5, 4, 3, 2, 1], 'python')
# [(6, 'p'), (5, 'y'), (4, 't'), (3, 'h'), (2, 'o'), (1, 'n')]
print(list(zipped3))

s = 'hello'
indices = range(len(s))
zipped4 = zip(indices, s)
print(list(zipped4))  # [(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]
