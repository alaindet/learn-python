class BookStore():
    def __init__(self, books=[]):
        self.books = books
        self.current_id = 1

    def add_book(self, name, author):
        print('Adding a book to the store...') # Log
        book = {
            'id': self.current_id,
            'name': name,
            'author': author,
            'read': False
        }
        self.current_id += 1
        self.books.append(book)

    def list_books(self):
        print('Listing all books from the store...') # Log
        return self.books

    def mark_book_as_read(self, name):
        print('Marking a book as read...') # Log
        book = self._find_book_by_name(name)
        book['read'] = True
        self._update_book(book)

    def delete_book(self, name):
        print('Deleting a book from store...') # Log
        self.books = [i for i in self.books if i['name'] != book['name']]

    def _find_book_by_name(self, name):
        print('Finding book by name...') # Log
        for book in self.books:
            if name == book['name']:
                return book
        return None

    def _update_book(self, book):
        print('Updating book on store...') # Log
        self.books = [book for i in self.books if i['id'] == book['id']]
