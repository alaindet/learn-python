def readAge() -> int:
    while (True):
        try:
            age_input = input('How old are you? > ')
            return int(age_input)
        except ValueError:
            print('Invalid input')

def bounce(age: int) -> None:
    if age < 18:
        print('Sorry, you\'re too young.')
    elif age < 21:
        print('Ok, enter, but you need a wristband.')
    else:
        print('Ok, you can enter and have a drink.')

age = readAge()
bounce(age)
