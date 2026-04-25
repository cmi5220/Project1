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


def is_draw(board):
    """Return True if the board is full and there is no winner."""
    return all(cell != " " for row in board for cell in row)


def is_valid_coordinate(value):
    """Return True if the string value represents a valid board coordinate."""
    return value.isdigit() and 0 <= int(value) < BOARD_SIZE


def get_player_move(board, player):
    """Prompt the current player until a valid move is entered."""
    while True:
        raw_move = input(f"{PLAYER_NAMES[player]}, enter row and column (0-2 0-2): ").strip()

        if not raw_move:
            print("Input cannot be empty. Please enter two numbers.")
            continue

        parts = raw_move.replace(",", " ").split()
        if len(parts) != 2:
            print("Please enter exactly two values: row and column.")
            continue

        row_text, col_text = parts
        if not (is_valid_coordinate(row_text) and is_valid_coordinate(col_text)):
            print("Coordinates must be whole numbers from 0 to 2.")
            continue

        row = int(row_text)
        col = int(col_text)

        if board[row][col] != " ":
            print("That cell is already occupied. Choose another one.")
            continue

        return row, col

