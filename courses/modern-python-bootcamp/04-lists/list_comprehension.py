from typing import List

"""\
List Comprehensions
https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

A listcomp is an expression returnig a list, encased in square brackets,
having a target expression, a "for" expression and any number of optional "for"
and/or "if" expressions

They are a concise and idiomatic way to manipulate or create lists
If a listcomp doesn't fit in a line though, don't force it!
"""

# Example 1
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# Is equivalent to
# squares = []
# for x in range(5):
#     squares.append(x**2)

# Example 2


def capitalize_words(sentence: str) -> str:
    return ' '.join([word.capitalize() for word in sentence.split(' ')])


print(capitalize_words('foo bar baz'))  # 'Foo Bar Baz'

# Turn into booleans
# Prints [False, False, False, True, True, True, False, False]
some_vals = [0, [], '', 1, 42, True, None, False]
print([bool(v) for v in some_vals])

# Conditionals!
# You can use conditionals to filter...
# Give me the squares of all multiples of 11 up to 50
squares_multiples = [n*n for n in range(51) if n % 11 == 0]
print(squares_multiples)  # Prints [0, 121, 484, 1089, 1936]

# ...or you can use conditionals to apply different expressions!
# Given me the first 10 numbers, with even numbers squared
even_squared = [n**2 if n % 2 == 0 else n for n in range(1, 11)]
print(even_squared)  # Prints [1, 4, 3, 16, 5, 36, 7, 64, 9, 100]


def strip_vowels(sentece: str) -> str:
    return ''.join([letter for letter in sentece if letter not in 'aeiouAEIOU'])


print(strip_vowels('This Is A Sentence'))  # Prints 'Ths s  Sntnc'

# Nested list comprehensions!
# Let's create a A*B 2D map full of zeros


def create_2d_map(width: int, height: int) -> List[List[int]]:
    # This is a list comprehension having a list comprehension as target expression
    return [[0 for row in range(width)] for col in range(height)]


print(create_2d_map(10, 3))
