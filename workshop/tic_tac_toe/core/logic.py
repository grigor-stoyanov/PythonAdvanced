from tic_tac_toe.core.validators import is_position_in_range, is_place_available, is_winner
from tic_tac_toe.core.helpers import get_row_col, print_current_board_state


def play(players, board, turns):
    turn_count = 0
    while True:
        current_player_name = turns[turn_count % 2]
        current_player_sign = players[current_player_name]
        # read position
        try:
            position = int(input(f"{current_player_name} choose a free position:"))
        except ValueError:
            position = 10
        # check if it is in range and position is available
        if is_position_in_range(position) and is_place_available(board, position):
            row, col = get_row_col(position)
            # place sign
            board[row][col] = current_player_sign
            print_current_board_state(board)

            # check if there is a winner
            if is_winner(board, current_player_sign):
                print(f'{current_player_name} won!')
                exit(0)
        else:
            # read new position for the same player
            turn_count -= 1
        turn_count += 1
