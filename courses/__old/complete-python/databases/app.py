from app.messages import MESSAGE
from app.actions import ACTION
from utils.input import get_input, ask_for
from utils.database_connection import DatabaseConnection
from utils.database import Database
from entities.books.repository import BooksRepository


class App():

    def __init__(self, books_repository):
        self.books_repository = books_repository
        self.action = ACTION
        self.message = MESSAGE

    def start(self):
        try:
            print(self.message['app.welcome'])
            self._loop()
        except KeyboardInterrupt:
            print(self.message['app.goodbye'])

    def _loop(self):
        while True:
            try:
                step = self._step()
                if step == False:
                    print(self.message['app.goodbye'])
                    break
            except Exception as e:
                error_message = e.__str__()
                print(f'\n[ERROR] {error_message}')

    def _step(self):
        user_action = self._choose_action()
        if user_action == 'quit':
            return False
        self._process_action(user_action)

    def _choose_action(self):
        print(self.message['app.menu'])
        user_action = get_input()
        for name in self.action:
            if self.action[name]['command'] == user_action:
                return name
        raise ValueError(self.message['input.error'])

    def _process_action(self, user_action):
        method_name = f'_process_{user_action}_action'
        method = getattr(self, method_name)
        method()

    def _process_add_book_action(self):
        print(self.message['action.add_book'])
        book_name, book_author = ask_for('the book name', 'the book author')
        self.books_repository.add_book(book_name, book_author)
        print(self.message['result.add_book'].format(book_name, book_author))

    def _process_list_books_action(self):
        print(self.message['action.list_books'])
        books = self.books_repository.list_books()
        print(books)

    def _process_mark_book_as_read_action(self):
        print(self.message['action.mark_book_as_read'])
        book_name, = ask_for('the book name')
        book = self.books_repository.mark_book_as_read(book_name)
        print(self.message['result.mark_book_as_read'].format(book['name']))

    def _process_delete_book_action(self):
        print(self.message['action.delete_book'])
        book_name, = ask_for('the book name')
        book = self.books_repository.delete_book(book_name)
        print(self.message['result.delete_book'].format(book['name']))


# Manual dependency injection here
db_connection = DatabaseConnection()
db = Database(db_connection)
books_repository = BooksRepository(db)
app = App(books_repository)

app.start()
