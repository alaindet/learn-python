f = lambda x, *args, y, **kwargs: (x, args, y, kwargs)

print(f)  # <function <lambda> at 0x000001D4D4398A40>
print(f(1, 2, 3, y=4, b=5, c=6))  # (1, (2, 3), 4, {'b': 5, 'c': 6})

the_answer = lambda: 42
print(the_answer())  # 42
print(the_answer())  # 42
print(the_answer())  # 42


def my_square(n: int) -> int:
    return n**2


sq = my_square
print(my_square)  # <function my_square at 0x000001ACC9E8D260>
print(sq)  # <function my_square at 0x000001ACC9E8D260>
print(lambda n: my_square(n))  # <function <lambda> at 0x0000029BC9A7D3A0>


def apply(fn, *args, **kwargs):
    return fn(*args, **kwargs)


print(apply(lambda *args: [x * 2 for x in args], 1, 2, 3, 4))  # [2, 4, 6, 8]

# Pass a lambda to built-in sorted() function
a = [2, 1, 6, 4]
print(a, sorted(a))  # [2, 1, 6, 4] [1, 2, 4, 6]

b = [
    {"name": "Bob", "age": 30},
    {"name": "Alice", "age": 20},
    {"name": "Charlie", "age": 40},
]

# [
#   {'name': 'Alice', 'age': 20},
#   {'name': 'Bob', 'age': 30},
#   {'name': 'Charlie', 'age': 40}
# ]
print(sorted(b, key=lambda person: person["age"]))

# [
#   {'name': 'Charlie', 'age': 40}
#   {'name': 'Bob', 'age': 30},
#   {'name': 'Alice', 'age': 20 },
# ]
print(sorted(b, key=lambda person: person["age"], reverse=True))

def dist_sq(x: complex) -> float:
    return (x.real)**2 + (x.imag)**2

c_nums = [3+3j, 1-1j, 0, 3+0j]
print(sorted(c_nums, key=dist_sq)) # [0, (1-1j), (3+0j), (3+3j)]

# Equivalent
print(sorted(c_nums, key=lambda x: (x.real)**2 + (x.imag)**2))