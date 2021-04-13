from json import dump, load

def store(path, data):
    with open(path, 'w') as file:
        dump(data, file)

def fetch(path):
    with open(path, 'r') as file:
        return load(file)
