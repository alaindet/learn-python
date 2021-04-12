from utils.database import BookStore
from utils.inputs import get_input, ask_for
from app.messages import MESSAGE
from app.actions import ACTION, get_actions_menu


class App():

    def __init__(self, book_store):
        self.book_store = book_store
        self.action = ACTION
        self.message = MESSAGE

    def run(self):
        print(self.message['title'])
        user_action = None
        while user_action != self.action['quit']['command']:
            user_action = self._choose_action()
            self._process_action(user_action)

    def _choose_action(self):
        try:
            print(self.message['menu'])
            user_action = get_input()
            for name in self.action:
                if self.action[name]['command'] == user_action:
                    return name
            raise ValueError(self.message['input.error'])
        except ValueError as e:
            print(e)

    def _process_action(self, user_action):
        try:
            method_name = f'_process_{user_action}_action'
            method = getattr(self, method_name)
            method()
        except AttributeError as e:
            print(f'There is no method with name {method}')

    def _process_add_book_action(self):
        print(self.message['action.add_book'])
        book_name, book_author = ask_for('the book name', 'the book author')
        book_store.add_book(book_name, book_author)

    def _process_list_books_action(self):
        print(self.message['action.list_books'])
        books = book_store.list_books()
        print(books)

    def _process_mark_book_as_read_action(self):
        print(self.message['action.mark_book_as_read'])
        book_name = ask_for('the book name')
        book_store.mark_book_as_read(book_name)

    def _process_delete_book_action(self):
        print(self.message['action.delete_book'])
        book_name = ask_for('the book name')
        book_store.delete_book(book_name)


book_store = BookStore()
app = App(book_store)
app.run()
