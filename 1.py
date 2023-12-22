def repeat_string(input_string, num_times):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string.")
    if not isinstance(num_times, int):
        raise ValueError("Number of times must be an integer.")
    if num_times < 0:
        raise ValueError("Number of times must be non-negative.")

    return input_string * num_times

test_string = "Python"
test_times = 3
print(repeat_string(test_string, test_times))