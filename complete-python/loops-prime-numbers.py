# for n in range(2, 10):
#     for m in range(2, n):
#         if n % m == 0:
#             print(f'{n} equals {n} * {m}')
#             break
#     else:
#         print(f'{n} is a prime number')

def is_prime(prime):
    for n in range(2, prime):
        if prime % n == 0:
            return False
    return True


for n in range(2, 10):
    maybe_prime = '' if is_prime(n) else 'NOT '
    print(f'Number {n} is {maybe_prime}prime')
