from enum import Enum
from functools import wraps


class Role(Enum):
    Basic = 0
    Admin = 1

user_role: Role = Role.Basic # <--

class AuthException(Exception):
    def __init__(self, role: Role):            
        message = f'Auth Error: role {role} required'
        super().__init__(message)

def auth(role: Role):
    """This is the base decorator factory for authorization"""
    def decorator(fn):
        @wraps(fn)
        def inner(*args, **kwargs):
            global user_role
            if user_role is not role:
                raise AuthException(role)
            return fn(*args, **kwargs)
        return inner
    return decorator

def is_basic_user(fn):
    """A pre-defined auth decorator for basic users"""
    return auth(Role.Basic)(fn)

def is_admin(fn):
    """A pre-defined auth decorator for admins"""
    return auth(Role.Admin)(fn)

# @auth(Role.Basic)
@is_basic_user
def create_posts():
    print('create_posts')

# @auth(Role.Admin)
@is_admin
def delete_posts():
    print('delete_posts')

# Prints
# create_posts
try:
    create_posts()
except AuthException as err:
    print(err)

# Prints
# Auth Error: role Role.Admin required
try:
    delete_posts()
except AuthException as err:
    print(err)