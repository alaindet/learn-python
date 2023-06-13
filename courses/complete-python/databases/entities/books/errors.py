class BooksError(Exception):
    pass

class BookAlreadyExistsError(BooksError):
    pass

class BookNotFoundError(BooksError):
    pass
