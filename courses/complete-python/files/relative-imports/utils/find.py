# Relative import (starts from this folder)
from .common.filesystem_helpers import save_to_file

# Absolute import equivalent
# from utils.common.filesystem_helpers import save_to_file

class NotFoundError(Exception):
    pass


def find_in(iterable, finder, expected):
    for i in iterable:
        if finder(i) == expected:
            return i
    raise NotFoundError(f'{expected} not found in provided iterable')
