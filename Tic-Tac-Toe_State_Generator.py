import collections
import struct

def check_win(board):
    """
    Checks if a player has won the game.
    Args:
        board: A tuple of 9 integers representing the board.
               (0=empty, 1=X, 2=O)
    Returns:
        The winning player (1 or 2), or 0 if there is no winner yet.
    """
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != 0:
            return board[a]
    return 0

def generate_all_states():
    """
    Generates all possible and valid tic-tac-toe game states.
    Returns:
        A set of tuples, where each tuple represents a unique board state.
    """
    initial_board = (0,) * 9
    all_states = {initial_board}
    queue = collections.deque([initial_board])

    while queue:
        current_board = queue.popleft()

        # If there's a winner, this is a terminal state. Don't generate more moves.
        if check_win(current_board):
            continue

        # Determine whose turn it is
        num_x = current_board.count(1)
        num_o = current_board.count(2)
        player = 1 if num_x == num_o else 2

        # Generate next possible states
        for i in range(9):
            if current_board[i] == 0:
                next_board_list = list(current_board)
                next_board_list[i] = player
                next_board = tuple(next_board_list)

                if next_board not in all_states:
                    all_states.add(next_board)
                    queue.append(next_board)

    return all_states

def board_to_int(board):
    """
    Converts a board tuple to a unique integer using base-3 representation.
    This is a compact way to store the state.
    """
    number = 0
    for i in range(9):
        number += board[i] * (3**i)
    return number

def save_states_to_file(states, filename="tictactoe_states.ttts"):
    """
    Saves all game states to a compact binary file.
    Each state is converted to a base-3 integer and stored as a 2-byte
    unsigned short.
    """
    with open(filename, "wb") as f:
        for board_state in states:
            state_as_int = board_to_int(board_state)
            # Pack the integer as a 2-byte unsigned short (big-endian)
            packed_data = struct.pack('>H', state_as_int)
            f.write(packed_data)
    print(f"Successfully saved {len(states)} states to '{filename}'.")


if __name__ == "__main__":
    print("Generating all possible tic-tac-toe game states...")
    all_game_states = generate_all_states()
    print(f"Found {len(all_game_states)} unique game states.")
    save_states_to_file(all_game_states)