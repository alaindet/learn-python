def get_input():
    return input('> ')


def ask_for(*what):
    inputs = []
    for something in what:
        print(f'\nEnter {something}: ')
        user_input = input('> ')
        inputs.append(user_input)
    return inputs
