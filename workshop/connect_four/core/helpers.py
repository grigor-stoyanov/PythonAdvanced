def four_time_row(mat, sym):
    for row in mat:
        if f'{sym}' * 4 in ''.join(map(str,row)):
            return True
    return False


def print_board(mat):
    for row in mat:
        print(row)
