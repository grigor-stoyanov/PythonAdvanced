from connect_four.core.helpers import four_time_row


def is_col_valid(col, board):
    try:
        int(col)
    except ValueError:
        return False
    finally:
        col = int(col) - 1
        if 0 <= col < 6 and board[0][col] == '0':
            return True
    return False


def is_winner(mat, sym):
    if four_time_row(mat, sym):
        return True

    transposed_mat = [
        [
            mat[row][col] for row in range(len(mat))
        ]
        for col in range(len(mat[0]))
    ]
    if four_time_row(transposed_mat, sym):
        return True

    diagonals_mat = [[] for _ in range(len(mat[0]) + len(mat) - 1)]
    second_diagonals_mat = [[] for _ in range(len(diagonals_mat))]
    for i in range(len(mat[0])):
        for j in range(len(mat)):
            diagonals_mat[i + j].append(mat[j][i])
            second_diagonals_mat[i - j + len(mat) - 1].append(mat[j][i])

    diagonals_mat.extend(second_diagonals_mat)
    if four_time_row(diagonals_mat, sym):
        return True


def is_board_full(mat):
    for ele in mat[0]:
        if ele == '0':
            return False
    return True
