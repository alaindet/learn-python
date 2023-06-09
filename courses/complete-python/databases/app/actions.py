ACTION = {
    'add_book': {
        'command': 'a',
        'description': 'to (a)dd a new book',
    },
    'list_books': {
        'command': 'l',
        'description': 'to (l)ist all books'
    },
    'mark_book_as_read': {
        'command': 'r',
        'description': 'to mark a book as (r)ead'
    },
    'delete_book': {
        'command': 'd',
        'description': 'to (d)elete a book'
    },
    'quit': {
        'command': 'q',
        'description': 'to (q)uit'
    }
}


def get_actions_menu():
    lines = []
    for name in ACTION:
        action = ACTION[name]
        command = action['command']
        description = action['description']
        line = f"- '{command}' => {description}"
        lines.append(line)
    return '\n'.join(lines)
