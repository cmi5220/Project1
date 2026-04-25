BOARD_SIZE = 3
PLAYER_NAMES = {"X": "Player X", "O": "Player O"}


def create_board():
    """Create and return an empty 3x3 board."""
    return [[" " for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def print_board(board):
    print("\nCurrent board:")
    print("   0   1   2")
    for row_index, row in enumerate(board):
        print(f"{row_index} " + " | ".join(row))
        if row_index < BOARD_SIZE - 1:
            print("  " + "-" * 9)
    print()