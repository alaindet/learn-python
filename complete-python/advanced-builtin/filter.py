people = ['Alice', 'Bob', 'Charlie', 'Darlene', 'Eric', 'Francis']

# # Filter returns a generator
# contains_r = lambda name: 'r' in name
# names_containing_r = filter(contains_r, people)
# for name in names_containing_r:
#     print(name)

# Alternative 1: Condensed alternative
for name in filter(lambda name: 'r' in name, people):
    print(name)

# Alternative 2: Generator comprehension turned into tuple
names_with_r1 = tuple(name for name in people if 'r' in name)
print(names_with_r1)

def my_filter(func, iterable):
    for item in iterable:
        if func(item):
            yield item

# Alternative 3
names_with_r2 = my_filter(lambda name: 'r' in name, people)
print(tuple(names_with_r2))
