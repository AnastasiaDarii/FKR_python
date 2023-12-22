def check_multiples_of_three(func):
    def wrapper(*args, **kwargs):
        if all(arg % 3 == 0 for arg in args if isinstance(arg, (int, float))):
            return func(*args, **kwargs)
        else:
            raise ValueError("Помилка")
    return wrapper


@check_multiples_of_three
def multiply(a, b):
    return a * b


try:
    print(multiply(9, 3))
    print(multiply(10, 3))
except ValueError as e:
    print(e)