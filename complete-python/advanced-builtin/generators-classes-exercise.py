from is_prime import is_prime

class PrimeGenerator:

    def __init__(self, stop):
        self.stop = stop
        self.counter = 0

    def __next__(self):
        while self.counter < self.stop:
            self.counter += 1
            if is_prime(self.counter):
                return self.counter
        raise StopIteration()



try:
    g = PrimeGenerator(100)
    while True:
        print(next(g))
except StopIteration:
    print('PrimeGenerator stopped')