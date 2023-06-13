from .errors import BookAlreadyExistsError, BookNotFoundError


class BooksRepository():

    def __init__(self, db):
        self.db = db
        self._init_table()
        self.table = 'books'

    def _init_table(self):
        self.db.execute(
            """
            CREATE TABLE IF NOT EXISTS "books" (
                "id"	INTEGER,
                "name"	TEXT NOT NULL UNIQUE,
                "author"	TEXT NOT NULL,
                "read"	INTEGER NOT NULL DEFAULT 0,
                PRIMARY KEY("id" AUTOINCREMENT)
            );
            """
        )

    def add_book(self, name, author):
        book = {
            'name': name,
            'author': author,
            'read': False,
        }

        existing_book = self._find_book_by_name(name)

        if existing_book is not None:
            name = existing_book['name']
            message = f'Book with name "{name}" already exists'
            raise BookAlreadyExistsError(message)

        last_id = self.db.insert(self.table, book)
        book['id'] = last_id

        return book

    def list_books(self):
        logs = []
        books = self.db.select(self.table)

        for book in books:
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

        updated_book = dict(book)
        updated_book['read'] = True

        self.db.update(
            self.table,
            {
                'read': ':read'
            },
            'id = :id',
            {
                ':read': updated_book['read'],
                ':id': updated_book['id'],
            }
        )

        return updated_book

    def delete_book(self, name):
        book = self._find_book_by_name(name)

        if book is None:
            message = f'Book with name "{name}" does not exist'
            raise BookNotFoundError(message)

        self.db.delete(self.table, 'name = :name', {':name': f'%{name}%'})

        return book

    def _find_book_by_name(self, name):

        result = self.db.select(
            self.table,
            '*',
            'name LIKE :name',
            {':name': f'%{name}%'}
        )

        if len(result) == 0:
            return None

        return result[0]
