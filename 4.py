def is_regular_polygon(sides):
    sides = list(map(int, sides.split()))
    return "YES" if len(set(sides)) == 1 else "NO"


input_sides = "3 3 3 3"
print(is_regular_polygon(input_sides))  