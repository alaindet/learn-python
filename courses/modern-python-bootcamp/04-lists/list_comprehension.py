"""\
List Comprehensions
https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
"""

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# Longer
result1: str = ''

for sound in sounds:
    result1 += sound.capitalize()

print(result1)

# Equivalent, shorter
result2 = ''.join([word.capitalize() for word in sounds])
print(result2)
