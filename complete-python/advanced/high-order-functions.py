from typing import Callable, Optional

print('\n# Example 1')
def greet():
    print('Hello!')

def before_and_after(func: Callable) -> None:
    print('Before...')
    func()
    print('After...')

before_and_after(greet)
before_and_after(lambda: print('Hello'))

print('\n# Example 2')
movies = (
    {'name': 'The Matrix', 'director': 'Wachowski'},
    {'name': 'A Beautiful Day in the Neighborhood', 'director': 'Heller'},
    {'name': 'The Irishman', 'director': 'Scorsese'},
    {'name': 'Klaus', 'director': 'Pablos'},
    {'name': '1917', 'director': 'Mendes'},
)

def find_movie(expected, finder) -> Optional[dict]:
    for movie in movies:
        if finder(movie) == expected:
            return movie
    return None

find_by = input('What property are we searching by (name, director)?: ')
searching_for = input('What are you searching for?: ')
movie = find_movie(searching_for, lambda movie: movie[find_by])
print(movie)