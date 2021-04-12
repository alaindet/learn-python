from utils.strings import glue
from app.actions import ACTION, get_actions_menu

MESSAGE = {
    'title': glue(
        'Book Store 1.0',
        '==============',
        ''
    ),

    'menu': glue(
        'Actions',
        '=======',
        get_actions_menu(),
        '',
        'What do you want to do?',
    ),

    'input.error': 'You did not input a valid command.',
    'input.book_name': 'Enter book name',
    'input.book_author': 'Enter book author',

    'action.add_book': 'Adding a book to the collection...',
    'action.list_books': 'Listing all books from the collection...',
    'action.mark_book_as_read': 'Marking a book as read...',
    'action.delete_book': 'Deleting a book from the collection...',
}
