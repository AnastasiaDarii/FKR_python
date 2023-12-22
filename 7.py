def generate(start, end):
    for number in range(start, end + 1):
        if number % 2 != 0 and number % 7 != 0:
            yield number


print(list(generate(1, 50)))