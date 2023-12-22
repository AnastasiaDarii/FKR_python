def find(substr, string):
    if len(substr) == 0 or len(string) < len(substr):
        return -1
    if string[:len(substr)] == substr:
        return 0

    res = find(substr, string[1:])
    if res != -1:
        return res + 1
    else:
        return -1


print(find("test", "this is a test string"))