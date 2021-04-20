from scraper import books

def get_top_rated_books(limit=5):
    sorted_books = sorted(books, key=lambda book: book.rating, reverse=True)
    actual_limit = min(limit, len(sorted_books))
    best_books = sorted_books[:actual_limit]
    return best_books

def get_cheapest_books(limit=5):
    sorted_books = sorted(books, key=lambda book: book.price)
    actual_limit = min(limit, len(sorted_books))
    best_books = sorted_books[:actual_limit]
    return best_books

print('\nTop rated books')
for book in get_top_rated_books():
    print(f'{book.rating}/5', book.name)

print('\nCheapest books')
for book in get_cheapest_books():
    print(f'£{book.price}', book.name)