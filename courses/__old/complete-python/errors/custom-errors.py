"""
This is a module docstring
This file is all about custom errors
"""

class CarTypeError(TypeError):
    """
    This is a class docstring
    Exception raised when a Car instance is needed, but not provided
    """

    def __init__(self, message, code):
        """
        This is a method docstring
        Just initialize a CarTypeError
        """
        super().__init__(f'Error code {code}: {message}')
        self.code = code


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
            error_type = car.__class__.__name__
            method = 'Garage#add_car'
            error_message = f'{method} requires a Car istance, {error_type} given'
            raise CarTypeError(error_message, 500)


garage = Garage()
garage.add_car('Car 1')
print(len(garage))
