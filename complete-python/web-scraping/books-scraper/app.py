from scraper import books

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

print('\nTop rated books')
for book in get_top_rated_books():
    print(f'{book.rating}/5', book.name)

print('\nCheapest books')
for book in get_cheapest_books():
    print(f'£{book.price}', book.name)