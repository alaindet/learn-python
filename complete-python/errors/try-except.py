class Car:
    def __init__(self, maker, model):
        self.maker = maker
        self.model = model

    def __repr__(self):
        return f'<Car {self.maker} {self.model}>'


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError('Car argument required')
        self.cars.append(car)


garage = Garage()
car1 = Car('Maker 1', 'Car 1')

try:
    garage.add_car(car1)
except TypeError:
    print('You did not provide a Car')
except ValueError:
    print('In case any ValueError happens')
finally:
    print('Whatever happens, run this anyway')
