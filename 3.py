def is_key_or_value_in_dict(dictionary, value):
    if value in dictionary:
        return True
    if value in dictionary.values():
        return True
    return False


my_dict = {'a': 1, 'b': 2, 'c': 3}
print(is_key_or_value_in_dict(my_dict, 'b'))
print(is_key_or_value_in_dict(my_dict, 2))  