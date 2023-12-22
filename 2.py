def to_hex(number):
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a non-negative integer")
    return format(number, 'x')

test_number = 16
print(to_hex(test_number))