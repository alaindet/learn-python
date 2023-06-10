numbers = [1, 2, 3, 4, 5]

def square(n):
    return n * n

squared1 = map(square, numbers)

print('\nsquared with normal function')
for i in squared1:
    print(i)

squared_lambda = lambda n: n * n
squared2 = map(squared_lambda, numbers)

print('\nsquared with lambda')
for i in squared2:
    print(i)


squared3 = map(lambda n: n * n, [1, 2, 3, 4, 5])

print('\nsquared with inline lambda')
for i in squared3:
    print(i)