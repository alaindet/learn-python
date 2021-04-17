def is_prime(n):
    j = 2
    while j < n:
        if n % j == 0:
            return False
        j += 1
    return True