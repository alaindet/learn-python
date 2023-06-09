class Student:
    def __init__(self, name):
        self.name = name


movies = ['Matrix', 'Finding Nemo']
# print(movies.__class__) # <class 'list'>


class Garage:

    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]

    def __repr__(self):
        """
        Interacts with debugger
        Gets called when printing the class, only if __str__ is not defined
        """
        return f'<Garage {self.cars}>'

    def __str__(self):
        return f'This garage has {len(self)} cars'

my_garage = Garage()
my_garage.cars.append('Car 1')
my_garage.cars.append('Car 2')

# Uses __len__
# print(len(my_garage))
# for car in my_garage:
#     print(car)

# Uses __getitem__
# print(my_garage[0])

# Uses __str__
print(my_garage)
