people = ['Alice', 'Bob', 'Charlie', 'Darlene', 'Eric', 'Francis']

def name_contains_a(name):
    return 'a' in name

names_containing_a = filter(name_contains_a, people)

print(names_containing_a)