class RangeWannabeGenerator:
    def __init__(self, stop_at):
        self.number = 0
        self.stop_at = stop_at

    def __next__(self):
        """
        This method defines a class as an "Iterator"
        """
        if self.number <= self.stop_at:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

    def __iter__(self):
        """
        This method defines a class as an "Iterable"
        Allows you to use it in a for loop
        """
        return self

# Example 1
my_iterable_1 = RangeWannabeGenerator(100)
print(sum(my_iterable_1))
my_iterable_2 = RangeWannabeGenerator(10)
for item in my_iterable_2:
    print(item)


class AlternativeIterable:
    """
    This is an alternative way to create an iterable
    """
    def __init__(self):
        self.cars = ['Car 1', 'Car 2', 'Car 3']
    
    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]

# Example 2
my_iterable_3 = AlternativeIterable()
for car in my_iterable_3:
    print(car)