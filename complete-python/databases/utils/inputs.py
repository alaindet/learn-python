def get_input():
    return input('> ')


def ask_for(*what):
    if isinstance(what, tuple):
        inputs = []
        for something in what:
            user_input = _ask_for_one(something)
            inputs.append(user_input)
        return inputs
    else:
        _ask_for_one(what)


def _ask_for_one(what):
    print(f'Enter {what}:')
    return get_input()
