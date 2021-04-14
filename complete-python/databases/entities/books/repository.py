from time import time_ns
from pathlib import Path

import utils.json
from .errors import BookAlreadyExistsError, BookNotFoundError

class BooksRepository():

    def __init__(self, db):
        self.books = []
        self.db = db
        self.storage_path = self._init_storage_path()
        self._fetch_books()

    def _init_table(self):
        self.db.execute(
            """
            CREATE TABLE IF NOT EXISTS (
                id PRIMARY KEY,
                name,
                author,
                read
            )
            """
        );

    def _init_storage_path(self):
        this_dir = Path(__file__).parent
        return Path(this_dir, 'data.json').absolute()

    def add_book(self, name, author):
        book = self._find_book_by_name(name)

        if book is not None:
            message = f'Book with name "{name}" already exists'
            raise BookAlreadyExistsError(message)

        new_book = {
            'id': time_ns(),
            'name': name,
            'author': author,
            'read': False
        }

        self.books.append(new_book)
        self._store_books()

        return new_book

    def list_books(self):
        logs = []

        for book in self.books:
            logs.append('\n'.join([
                '',
                f"* | {book['name']} (by {book['author']})",
                 '  | ----------',
                f"  | ID: {book['id']}",
                f"  | Already Read: {'YES' if book['read'] else 'NO'}"
            ]))

        return '\n'.join(logs)

    def mark_book_as_read(self, name):
        book = self._find_book_by_name(name)

        if book is None:
            message = f'Book with name "{name}" does not exist'
            raise BookNotFoundError(message)

        book['read'] = True
        self._update_book(book)
        self._store_books()

        return book

    def delete_book(self, name):
        book = self._find_book_by_name(name)

        if book is None:
            message = f'Book with name "{name}" does not exist'
            raise BookNotFoundError(message)

        self.books = [i for i in self.books if i['name'] != book['name']]
        self._store_books()

        return book

    def _find_book_by_name(self, name):
        for book in self.books:
            if name in book['name']:
                return book
        return None

    def _update_book(self, book):
        self.books = [book if b['id'] == book['id'] else b for b in self.books]

    def _store_books(self):
        utils.json.store(self.storage_path, self.books)

    def _fetch_books(self):
        self.books = utils.json.fetch(self.storage_path)
