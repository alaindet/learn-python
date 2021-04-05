class Student:
    def __init__(self, name):
        self.name = name


movies = ['Matrix', 'Finding Nemo']
print(movies.__class__) # <class 'list'>


class Garage:
    def __init__(self):
        self.cars = []

my_garage = Garage()
my_garage.cars.append('Car 1')
my_garage.cars.append('Car 2')
print(my_garage.cars)
