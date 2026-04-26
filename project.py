def create_board():
    board = []

    for i in range(3):
        row = []
        for j in range(3):
            row.append(" ")
        board.append(row)

    return board


def print_board(board):
    print()
    print("  0 1 2")

    for i in range(3):
        print(i, end=" ")
        for j in range(3):
            print(board[i][j], end="")
            if j < 2:
                print("|", end="")
        print()
        if i < 2:
            print("  -----")
    print()


def check_winner(board, player):
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True

    for j in range(3):
        if board[0][j] == player and board[1][j] == player and board[2][j] == player:
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False


def is_draw(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True


def get_valid_number(message):
    while True:
        value = input(message)

        if value == "0" or value == "1" or value == "2":
            return int(value)

        print("Invalid Enter 0, 1, or 2.")


def get_player_move(board, player):
    while True:
        print("Player", player, "turn")
        row = get_valid_number("Enter row 0-2: ")
        col = get_valid_number("Enter column 0-2: ")

        if board[row][col] != " ":
            print("That spot is taken, try again.")
        else:
            return row, col


def switch_player(player):
    if player == "X":
        return "O"
    else:
        return "X"


def play_game():
    board = create_board()
    current_player = "X"

    print("Tic-Tac-Toe!")
    print("Players take turns entering a row and column from 0 to 2.")

    while True:
        print_board(board)
        row, col = get_player_move(board, current_player)
        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print("Player", current_player, "wins!")
            break

        if is_draw(board):
            print_board(board)
            print("The game is a draw.")
            break

        current_player = switch_player(current_player)


def play_again():
    while True:
        answer = input("Do you want to play again?: ")
        answer = answer.lower()

        if answer == "y" or answer == "yes":
            return True
        if answer == "n" or answer == "no":
            return False

        print("Enter y or n.")


 
def main():
    while True:
        play_game()

        if play_again() == False:
            print("Thank you for playing")
            break


if __name__ == "__main__":
    main()