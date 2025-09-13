import collections
import json

# This check_win function remains the same.
def check_win(board):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
        (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != 0:
            return board[a]
    if 0 not in board:
        return 'draw' # Return 'draw' for a tie
    return 0

# This state generation function remains the same.
def generate_all_states():
    # ... (This function is identical to your original one) ...
    initial_board = (0,) * 9
    all_states = {initial_board}
    queue = collections.deque([initial_board])
    while queue:
        current_board = queue.popleft()
        if check_win(current_board):
            continue
        num_x = current_board.count(1)
        num_o = current_board.count(2)
        player = 1 if num_x == num_o else 2
        for i in range(9):
            if current_board[i] == 0:
                next_board_list = list(current_board)
                next_board_list[i] = player
                next_board = tuple(next_board_list)
                if next_board not in all_states:
                    all_states.add(next_board)
                    queue.append(next_board)
    return all_states

# This integer conversion function remains the same.
def board_to_int(board):
    number = 0
    for i in range(9):
        number += board[i] * (3**i)
    return number

# --- NEW MINIMAX LOGIC ADDED HERE ---
memo = {} # Use memoization to speed up minimax calculations significantly

def minimax(board, player):
    """
    Minimax function to determine the score of a board state.
    """
    state_key = (board, player)
    if state_key in memo:
        return memo[state_key]

    winner = check_win(board)
    if winner != 0:
        if winner == 1: return -1 # X (player 1) wins, bad for O
        if winner == 2: return 1  # O (player 2) wins, good for O
        if winner == 'draw': return 0

    scores = []
    for i in range(9):
        if board[i] == 0:
            new_board = list(board)
            new_board[i] = player
            # The other player is 1 if current is 2, and vice-versa (3 - player)
            scores.append(minimax(tuple(new_board), 3 - player))

    result = max(scores) if player == 2 else min(scores)
    memo[state_key] = result
    return result

def find_best_move(board, player):
    """
    Finds the best move for a given player from a board state.
    """
    best_score = -2  # A score lower than any possible outcome
    move = -1
    for i in range(9):
        if board[i] == 0:
            new_board = list(board)
            new_board[i] = player
            score = minimax(tuple(new_board), 3 - player)
            
            # This logic is for player O (AI). We want to maximize O's score.
            # Minimax returns -1 if X wins, so we need to find the move
            # that leads to the highest score for O.
            if score > best_score:
                best_score = score
                move = i
    return move

# --- MODIFIED SAVE FUNCTION ---
def solve_and_save_states(states, filename="tictactoe_ai_brain.json"):
    """
    Analyzes all states with Minimax and saves the optimal move for each
    state to a JSON file. We only need to calculate moves for player 2 (O),
    assuming the AI is always O.
    """
    solved_states = {}
    print("Solving all game states...")
    for board_state in states:
        # We only need to find a move if the game isn't over
        if check_win(board_state) == 0:
            num_x = board_state.count(1)
            num_o = board_state.count(2)
            
            # It's O's turn (player 2)
            if num_x > num_o:
                state_int = board_to_int(board_state)
                best_move = find_best_move(board_state, 2)
                solved_states[state_int] = best_move

    with open(filename, "w") as f:
        json.dump(solved_states, f)
    
    print(f"Successfully saved solved AI brain with {len(solved_states)} states to '{filename}'.")


if __name__ == "__main__":
    print("Generating all possible tic-tac-toe game states...")
    all_game_states = generate_all_states()
    print(f"Found {len(all_game_states)} unique game states.")
    # Run the new solve and save function
    solve_and_save_states(all_game_states)
