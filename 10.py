def build_pattern(n):
    if n % 2 == 0:
        return

    for i in range(n):
        row = ""
        for j in range(n):
            if j <= i or j >= n - i - 1 or i == n // 2 or j == n // 2:
                row += "* "
            else:
                row += "  "
        print(row)

n = 7
build_pattern(n)