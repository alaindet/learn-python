from utils.string import glue
from app.actions import get_actions_menu

MESSAGE = {
    'app.welcome': glue(
        '',
        'Book Store 1.0',
        '==============',
    ),

    'app.menu': glue(
        '',
        'Actions',
        '=======',
        get_actions_menu(),
        '',
        'What do you want to do?',
    ),

    'app.goodbye': '\nShutting down the Book Store 1.0...',

    'input.error': 'You did not input a valid command.',

    'action.add_book': '\nAdding a book to the collection...',
    'action.list_books': '\nListing all books from the collection...',
    'action.mark_book_as_read': '\nMarking a book as read...',
    'action.delete_book': '\nDeleting a book from the collection...',

    'result.add_book': '\nBook "{}" by author "{}" was added to the collection',
    'result.mark_book_as_read': '\nBook "{}" was marked as read',
    'result.delete_book': '\nBook "{}" was deleted from the collection'

}
