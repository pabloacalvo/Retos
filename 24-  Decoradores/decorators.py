import functools
from utils import is_authenticated, is_valid_password


def authenticate_class(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        print(f"Class: {args}")
        if is_authenticated(*args):
            return cls(*args, **kwargs)
        else:
            raise Exception("Unauthorized user")
    return wrapper

def validate_password(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Func: {func}")
        pwd = args[0].password
        if is_valid_password(pwd):
            print("Password ok")
            return func(*args, **kwargs)
        else:
            raise Exception("Invalid password")
    return wrapper