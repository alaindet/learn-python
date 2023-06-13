def greet(name='General Kenobi'):
    """
    Here's a function with an argument and a default parameter
    """
    print(f'Hello there! {name}!')


greet('Alain')


def i_am_empty():
    """
    A function with no return implicitly returns None
    """
    pass


print(i_am_empty())


def calculate_mpg(car):
    return car['mileage'] / car['fuel_consumed']


def get_car_name(car):
    return f"{car['maker']} {car['model']}"


def print_car_info(car):
    mpg = calculate_mpg(car)
    name = get_car_name(car)
    print(f'{name} does {mpg} miles per gallon')


car = {
    'maker': 'Ford',
    'model': 'Fiesta',
    'mileage': 23_000,
    'fuel_consumed': 460
}

print_car_info(car)


# Default values
default_y = 3

def add(x, y=default_y):
    """
    Default values are copied upon function definition
    Changing them later does not alter the default values defined
    """
    return x + y

print(add(2))
default_y = 4
print(add(2)) # default parameter is still 3 as it got stored


# Use function expressions

def greet():
    print('Hello')

hello = greet

hello()


students = [
    {'name': 'Alice', 'grades': (67, 90, 95, 100)},
    {'name': 'Bob', 'grades': (56, 78, 80, 90)},
    {'name': 'Jen', 'grades': (98, 90, 95, 99)},
    {'name': 'Anne', 'grades': (100, 100, 95, 100)}
]

operations = {
    'average': lambda seq: sum(seq) / len(seq),
    # 'total': lambda seq: sum(seq),
    'total': sum,
    'top': max
}

for student in students:
    name = student['name']
    grades = student['grades']
    print(f'\nStudent: {name}')
    operation_name = input("Enter 'average', 'total' or 'top': ")
    try:
        operation_fn = operations[operation_name]
        print(operation_fn(grades))
    except KeyError as error:
        print(f'You did not select any operation for {name}')
