"""
Take a look at the code in the problem description where we test if a number is prime.
Refactor the code and put it into the function below to turn the prime_generator() function into a generator.

Implement your generator so that others can get a prime number generator like this:

g = prime_generator(100)    # g can generate prime numbers under 100
next(g) # get next prime like this

Reminder: you don't need to change the function name nor the argument
"""

def is_prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

def prime_generator(bound):
    i = 2
    while i <= bound:
        if is_prime(i):
            yield i
        i += 1

try:
    g = prime_generator(100)
    while True:
        print(next(g))
except StopIteration:
    print('Prime numbers generator stopped')