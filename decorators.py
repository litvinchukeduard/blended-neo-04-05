def input_error(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# KeyError, ValueError, IndexError

# phone Ihor -> no such name -> KeyError

# add Ihor 1234 -> phone is too short -> raise ValueError
# if len(phone) < 10:
#     raise ValueError

# add | add Ihor -> not enough arguments -> ValueError
# name, phone = args
lst = ["Ihor"]
name, phone = lst

# add | add Ihor -> not enough arguments -> IndexError
name = args[0]
phone = args[1]