f = lambda x, *args, y, **kwargs: (x, args, y, kwargs)

print(f) # <function <lambda> at 0x000001D4D4398A40>
print(f(1, 2, 3, y=4, b=5, c=6)) # (1, (2, 3), 4, {'b': 5, 'c': 6})

the_answer = lambda: 42
print(the_answer()) # 42
print(the_answer()) # 42
print(the_answer()) # 42

def my_square(n: int) -> int:
    return n ** 2

sq = my_square
print(my_square) # <function my_square at 0x000001ACC9E8D260>
print(sq) # <function my_square at 0x000001ACC9E8D260>
print(lambda n: my_square(n)) # <function <lambda> at 0x0000029BC9A7D3A0>