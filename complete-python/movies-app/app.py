from textwrap import dedent

ACTIONS = {
    'add': 'a',
    'list': 'l',
    'find': 'f',
    'quit': 'q'
}

MENU_PROMPT = dedent(
    f"""

    Actions:
    - Type '{ACTIONS['add']}' to add a movie
    - Type '{ACTIONS['list']}' to list your movies
    - Type '{ACTIONS['find']}' to find a movie by title
    - Type '{ACTIONS['quit']}' to quit

    > """
)

movies = []


def add_movie(movie):
    movies.append(movie)


def find_movie(title):
    needle = title.lower()
    for movie in movies:
        haystack = movie['title'].lower()
        if haystack.find(needle) != -1:
            return movie
    return None


def render_movie(movie):
    title = movie['title']
    year = movie['year']
    director = movie['director']
    return f"- {title} ({year}), by: {director}"


def on_add_movie():
    print('\nAdd a movie')
    movie = {
        'title': input('Enter the movie title: '),
        'director': input('Enter the movie director: '),
        'year': input('Enter the movie release year: ')
    }
    add_movie(movie)


def on_list_movies():
    print('\nHere are all the movies:')
    for movie in movies:
        item = render_movie(movie)
        print(item)


def on_find_movie_by_title():
    print('\nFind a movie by title')
    title = input('Enter the movie title: ')
    movie = find_movie(title)
    if movie:
        print(render_movie(movie))
    else:
        print(f'No movie found with title "{title}"')



def start(): 
    print('\nThe Movies App\n==============')
    selection = input(MENU_PROMPT)
    while selection != ACTIONS['quit']:
        if selection == ACTIONS['add']:
            on_add_movie()
        elif selection == ACTIONS['list']:
            on_list_movies()
        elif selection == ACTIONS['find']:
            on_find_movie_by_title()
        else:
            print('Unknown command. Please try again.')
        selection = input(MENU_PROMPT)
    print('\nQuitting the Movies App')


# Import movies from file
if __name__ == '__main__':
    with open('movies.txt', 'r') as file:
        line = file.readline()
        while (line):
            title, year, director = line.split(';')
            add_movie({ 'title': title, 'director': director, 'year': year })
            line = file.readline()

start()
