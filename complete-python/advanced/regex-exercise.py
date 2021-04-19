import re
"""
Our definition of a secure filename is:
- The filename must start with an English letters or a number (a-zA-Z0-9).
- The filename can **only** contain English letters, numbers and symbols among these four: `-_()`.
- The filename must end with a proper file extension among `.jpg`, `.jpeg`, `.png` and `.gif`
"""


def is_filename_safe(filename):
    regex = '^[a-zA-Z0-9][a-zA-Z0-9-_()]*\.(?:jpg|jpeg|png|gif)$'
    return re.match(regex, filename) is not None

tests = [
    ('some-valid-file.png', True),
    ('invalid?filename', False),
    ('could-be-valid-but-wrong-extension.txt', False),
    ('SomethingInTitleCase.gif', True),
    ('Valid(WithParentheses).jpg', True),
]

for test, expected in tests:
    assertion = is_filename_safe(test)
    result = 'PASSED' if assertion == expected else 'NOT PASSED'
    print(result)
