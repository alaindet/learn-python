from app.messages import MESSAGE
from app.actions import ACTION
from utils.inputs import get_input, ask_for
from utils.books.repository import BooksRepository


class AppQuitException(Exception):
    pass

class App():

    def __init__(self, books_repository):
        self.books_repository = books_repository
        self.action = ACTION
        self.message = MESSAGE

    # TODO: Simplify
    def run(self):
        try:
            print(self.message['app.welcome'])
            while True:
                try:
                    self.step()
                except AppQuitException as e:
                    print(self.message['app.goodbye'])
                    break
                except Exception as e:
                    error_message = e.__str__()
                    print('\n' + error_message)
        except KeyboardInterrupt as e:
            print(self.message['app.goodbye'])

    def step(self):
        user_action = self._choose_action()
        if user_action == 'quit':
            print(self.message['app.goodbye'])
            raise AppQuitException();
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

    def _process_list_books_action(self):
        print(self.message['action.list_books'])
        books = self.books_repository.list_books()
        print(books)

    def _process_mark_book_as_read_action(self):
        print(self.message['action.mark_book_as_read'])
        book_name, = ask_for('the book name')
        self.books_repository.mark_book_as_read(book_name)

    def _process_delete_book_action(self):
        print(self.message['action.delete_book'])
        book_name, = ask_for('the book name')
        self.books_repository.delete_book(book_name)


# Manage dependencies
books_repository = BooksRepository()

app = App(books_repository)
app.run()
