from utils.books.errors import BookAlreadyExistsError, BookNotFoundError


class BooksRepository():
    def __init__(self, books=[]):
        self.books = books
        self.current_id = 1

    def add_book(self, name, author):
        book = self._find_book_by_name(name)

        if book is not None:
            message = f'Book with name "{name}" already exists'
            raise BookAlreadyExistsError(message)

        new_book = {
            'id': self.current_id,
            'name': name,
            'author': author,
            'read': False
        }

        self.current_id += 1
        self.books.append(new_book)

    def list_books(self):
        return self.books

    def mark_book_as_read(self, name):
        book = self._find_book_by_name(name)

        if book is None:
            message = f'Book with name "{name}" does not exist'
            raise BookNotFoundError(message)

        if book is not None:
            book['read'] = True
            self._update_book(book)

    def delete_book(self, name):
        book = self._find_book_by_name(name)

        if book is None:
            message = f'Book with name "{name}" does not exist'
            raise BookNotFoundError(message)

        self.books = [i for i in self.books if i['name'] != book['name']]

    def _find_book_by_name(self, name):
        for book in self.books:
            # Checks substring in string
            if name in book['name']:
                return book
        return None

    def _update_book(self, book):
        self.books = [book for i in self.books if i['id'] == book['id']]
