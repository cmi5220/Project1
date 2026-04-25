BOARD_SIZE = 3
PLAYER_NAMES = {"X": "Player X", "O": "Player O"}


def create_board():
    """Create and return an empty 3x3 board."""
    return [[" " for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def print_board(board):
    """Display the current state of the game board."""
    print("\nCurrent board:")
    print("   0   1   2")
    for row_index, row in enumerate(board):
        print(f"{row_index} " + " | ".join(row))
        if row_index < BOARD_SIZE - 1:
            print("  " + "-" * 9)
    print()


def check_winner(board, player):
    """Return True if the given player has won."""
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(BOARD_SIZE):
        if all(board[row][col] == player for row in range(BOARD_SIZE)):
            return True

    if all(board[index][index] == player for index in range(BOARD_SIZE)):
        return True

    if all(board[index][BOARD_SIZE - 1 - index] == player for index in range(BOARD_SIZE)):
        return True

    return False