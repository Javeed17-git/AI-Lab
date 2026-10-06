# Tic-Tac-Toe using Minimax Algorithm

# Check if a player has won
def check_winner(board, player):
    # Rows
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True

    # Columns
    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return True

    # Diagonals
    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


# Check whether the game is over
def terminal_test(board, computer, human):
    if check_winner(board, computer):
        return True

    if check_winner(board, human):
        return True

    # Board full
    for row in board:
        if "_" in row:
            return False

    return True


# Utility function
def utility(board, computer, human):
    if check_winner(board, computer):
        return 1

    if check_winner(board, human):
        return -1

    return 0


# Return all possible moves
def actions(board):
    moves = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                moves.append((i, j))

    return moves


# Apply a move and return a new board
def result(board, action, player):
    new_board = [row[:] for row in board]

    row, col = action
    new_board[row][col] = player

    return new_board


# MAX-VALUE
def max_value(board, computer, human):
    if terminal_test(board, computer, human):
        return utility(board, computer, human)

    value = float("-inf")

    for action in actions(board):
        new_board = result(board, action, computer)

        value = max(
            value,
            min_value(new_board, computer, human)
        )

    return value


# MIN-VALUE
def min_value(board, computer, human):
    if terminal_test(board, computer, human):
        return utility(board, computer, human)

    value = float("inf")

    for action in actions(board):
        new_board = result(board, action, human)

        value = min(
            value,
            max_value(new_board, computer, human)
        )

    return value


# MINIMAX-DECISION
def minimax_decision(board, computer, human):
    best_action = None
    best_value = float("-inf")

    for action in actions(board):
        new_board = result(board, action, computer)

        value = min_value(new_board, computer, human)

        if value > best_value:
            best_value = value
            best_action = action

    return best_action


# Check whether the human has an immediate winning move
def has_winning_move(board, player):
    for action in actions(board):
        new_board = result(board, action, player)

        if check_winner(new_board, player):
            return True

    return False


# Print board
def print_board(board):
    for row in board:
        print(" ".join(row))


# Main program
def main():

    # Read board
    board = []

    for _ in range(3):
        board.append(input().split())

    # Read computer's symbol
    computer = input().strip().upper()

    # Automatically determine human's symbol
    if computer == "X":
        human = "O"
    else:
        human = "X"

    # Check if human currently has a winning move
    human_can_win = has_winning_move(board, human)

    # Find best move using Minimax
    move = minimax_decision(board, computer, human)

    # No moves available
    if move is None:
        print_board(board)
        print("Game Draw")
        return

    row, col = move

    # Computer makes the move
    board[row][col] = computer

    # Display computer's move
    print(f"Computer places {computer} in position ({row + 1},{col + 1})")

    # Display board
    print_board(board)

    # Check game result
    if check_winner(board, computer):
        print("Computer Wins")

    elif check_winner(board, human):
        print("Human Wins")

    elif not actions(board):
        print("Game Draw")

    elif human_can_win:
        print("Human's winning move is blocked.")

    else:
        print("Game continues")


if __name__ == "__main__":
    main()

