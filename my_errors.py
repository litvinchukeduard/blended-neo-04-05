
class PhoneValidationError(Exception):
    pass

class NameValidationError(ValueError):
    pass

def input_error(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# raise PhoneValidationError



try:
    raise PhoneValidationError
except PhoneValidationError:
    print('Wrong phone!')
except ValueError:
    print("Wrong name!")
except Exception:
    print("exception!")
