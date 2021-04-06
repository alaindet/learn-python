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
            errorType = car.__class__.__name__
            raise TypeError(''.join([
                'You must provide a Car to instance toGarage#add_car, ',
                f'{errorType} given'
            ]))


garage = Garage()
garage.add_car('Car 1')
print(len(garage))
