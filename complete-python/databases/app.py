from utils.database import BookStore
from utils.inputs import get_input
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
        print(self.message['menu'])
        return get_input()

    def _process_action(self, user_action):
        try:
            method_name = f'_process_{user_action}_action'
            self[method_name]()
        except:
            print(self.message['input.error'])

    def _process_add_book_action():
        print(self.message['action.add_book'])
        book_name, book_author = _ask_for('book_name', 'book_author')
        book_store.add_book(book_name, book_author)

    def _process_list_books_action():
        print(self.message['action.list_books'])
        books = book_store.list_books()
        print(books)

    def _process_mark_book_as_read_action():
        print(self.message['action.mark_book_as_read'])
        book_name = self._ask_for('book_name')
        book_store.mark_book_as_read(book_name)

    def _process_delete_book_action():
        print(self.message['action.delete_book'])
        book_name = self._ask_for('book_name')
        book_store.delete_book(book_name)

    def _ask_for(self, *questions):
        if isinstance(questions, tuple):
            inputs = []
            for question in questions:
                user_input = self._ask_for_one(question)
                inputs.append(user_input)
            return inputs
        else:
            self._ask_for_one(questions)

    def _ask_for_one(self, question):
        message_key = f'input.{question}'
        print(self.message[message_key])
        return get_input()


book_store = BookStore()
app = Apop(book_store)
app.run()
