from scraper import books

USER_MENU = """
Select command

- 't' to look at the (t)op rated books
- 'c' to look at the (c)heapest books
- 'n' to show the (n)ext available book on the page
- 'q to (q)uit

Enter your choice: """

books_generator = (book for book in books)

def _sort_books(key, reverse=False):
    return sorted(books, key=key, reverse=reverse)

def _slice_books(sorted_books, limit=5):
    actual_limit = min(limit, len(sorted_books))
    return sorted_books[:actual_limit]

def get_top_rated_books(limit=5):
    sorted_books = _sort_books(lambda book: book.rating, reverse=True)
    return _slice_books(sorted_books, limit)

def get_cheapest_books(limit=5):
    sorted_books = _sort_books(lambda book: book.price, reverse=False)
    return _slice_books(sorted_books, limit)

def on_show_top_rated_books():
    print('\nTop rated books')
    for book in get_top_rated_books():
        print(f'{book.rating}/5', book.name)

def on_show_cheapest_books():
    print('\nCheapest books')
    for book in get_cheapest_books():
        print(f'£{book.price}', book.name)

def on_show_next_book():
    print('\nShow the next book')
    try:
        print(next(books_generator))
    except StopIteration:
        print('No book left')

def on_invalid_command():
    print('Please enter a valid command')

def menu():

    user_choices = {
        't': on_show_top_rated_books,
        'c': on_show_cheapest_books,
        'n': on_show_next_book,
    }

    user_choice = None

    while user_choice != 'q':
        try:
            user_choice = input(USER_MENU)
            handler = user_choices[user_choice]
            handler()
        except KeyError:
            on_invalid_command()

menu()