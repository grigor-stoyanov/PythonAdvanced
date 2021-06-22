from connect_four.core.helpers import print_board
from connect_four.core.validators import is_col_valid, is_winner, is_board_full


def play(board, column, current_player, players):
    if is_col_valid(column, board):
        column = int(column) - 1
        for row in range(-1, -len(board), -1):
            if board[row][column] == '0':
                board[row][column] = current_player[-1]
                break
        print_board(board)
        if is_winner(board, current_player[-1]):
            print(f'The winner is {current_player}')
            return True
        if is_board_full(board):
            print(f'Game over!')
            return True
        return False
    print('Invalid input')
    players.rotate(-1)
    return False
