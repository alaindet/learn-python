from utils.strings import glue
from app.actions import ACTION, get_actions_menu

MESSAGE = {
    'title': glue(
        'Book Store 1.0',
        '==============',
        ''
    ),

    'menu': glue(
        '',
        'Actions',
        '=======',
        get_actions_menu(),
        '',
        'What do you want to do?',
    ),

    'input.error': '\nYou did not input a valid command.',

    'action.add_book': '\nAdding a book to the collection...',
    'action.list_books': '\nListing all books from the collection..',
    'action.mark_book_as_read': '\nMarking a book as read...',
    'action.delete_book': '\nDeleting a book from the collection...',
}
