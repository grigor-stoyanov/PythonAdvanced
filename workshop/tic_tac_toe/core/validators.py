from tic_tac_toe.core.helpers import get_row_col


def is_position_in_range(position):
    if 1 <= position <= 9:
        return True
    return False


def is_place_available(board, position):
    row, col = get_row_col(position)
    if board[row][col] == ' ':
        return True
    return False


def is_winner(board, sign):
    for row in board:
        if row.count(sign) == 3:
            return True
    for col in range(len(board)):
        if len([board[row][col] for row in range(len(board)) if board[row][col] == sign]) == 3:
            return True
    if len([board[row][row] for row in range(len(board)) if board[row][row] == sign]) == 3:
        return True
    if len([board[row][len(board) - row - 1] for row in range(len(board)) if
            board[row][len(board) - row - 1] == sign]) == 3:
        return True
    return False
