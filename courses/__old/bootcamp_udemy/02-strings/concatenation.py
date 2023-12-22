movie = 'Blade Runner'
director = 'Ridley Scott'

movie_and_director = movie + ' (' + director + ')'
print(movie_and_director) # Blade Runner (Ridley Scott)

# Implicit concatenation: Only print() and only for literals
print('abc' '123') # abc123
# print('abc' 123) # Raises SyntaxError

print('hello' * 3) # hellohellohello
print('@' * 10) # @@@@@@@@@@

price = '10.5'
print(price * 5) # 10.510.510.510.510.5 (oops!)
print(float(price) * 5) # 52.5 (better)
