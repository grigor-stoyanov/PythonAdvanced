def first_half(n):
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            print(col, end=' ')
        print()


def second_half(n):
    for row in range(n, 0, -1):
        for col in range(1, row):
            print(col, end=' ')
        print()


def print_triangle(n):
    first_half(n)
    second_half(n)