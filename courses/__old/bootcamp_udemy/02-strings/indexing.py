movie = 'The Matrix'
print(movie[0]) # 'T'
print(movie[4]) # 'M'
print(movie[len(movie) - 1]) # 'x' (Getting the last element of a string)
print(movie[-1]) # 'x' (Equivalent of above, much more practical
print(movie[:5]) # 'The M'
# print(movie[123]) # Raises IndexError

# Strings are immutable!
# movie[4] = 'F' # Raises TypeError
