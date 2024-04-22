def print_board(board: list) -> None:

    """
    Prints the displayed board using the 2D list board

    Args: nested for loops add | and _ to create the board string which will be printed to display the board.

    Return: None
    """
    brd_str = ''

    for row in board:
        brd_str += '|'
        for col in row:
            if col == '':
                brd_str += ' _ '
            else:
                brd_str += ' ' + col + ' '
            brd_str += '|'
        brd_str += '\n'
    
    print(brd_str)

def check_winner(board: list) -> bool:

    """
    Checks to see if any row, column, or diagonal as three common symbols X or O.

    Args: for loops and if statements which check for a winner

    Return: True if there are three common symbols X or O in the rows, columns, and diagonals. Else, False.
    """

    for row in board:
        if row[0] == row[1] == row[2] != '':
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return True
    if board[0][0] == board[1][1] == board[2][2] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
        return True
    return False

def input_row_col() -> tuple:

    """
    Validates users row and column input.

    Args: while loop which loops until user inputs a valid row and column.

    Return: tuple of the valid row and column values.
    """

    invalid = True

    while invalid:
        user_input = input()
        split_input = user_input.split()
        if len(split_input) != 2:
            print("Please enter valid row and col numbers from 1 to 3:")
            continue
        row_str = split_input[0]
        col_str = split_input[1]
        if not row_str.isdigit() or not col_str.isdigit():
            print("Please enter valid row and col numbers from 1 to 3:")
            continue
        row = int(row_str)
        col = int(col_str)
        if row not in range(1, 4) or col not in range(1, 4):
            print("Please enter valid row and col numbers from 1 to 3:")
            continue
        invalid = False 
    return (int(row_str), int(col_str))

# Main program function.
def play_tictactoe():

    times_played = 0
    # While loop iterates until the player does not want to play anymore.
    while True:
        times_played += 1

        # Introduces the player and provides an example of the game input.
        print("When prompted, enter desired row and column numbers")
        print("""Example: 1 3

| _ | _ | X |
| _ | _ | _ |
| _ | _ | _ |
        """)

        board = [['','',''],['','',''],['','','']] # Initializes empty game board
        players = ['X', 'O'] # Initializes list of player symbols X and O.
        current_player = 0 # Initializes current_player variable which represents the index of the players list.

        print("Player X starts!") # Indicates starting player.
        
        print_board(board) # Prints the initial empty board.

        # While loop iterates until a player wins or there is a tie.
        times_played = 0
        while True:
            player = players[current_player] # Sets the current player.
            print(f"Enter row and column for player {player}")
            row, col = input_row_col() # Sets each value in the tuple returned by input_row_col to the variables row and col.

            # While loop iterates until the player inputs a valid row and col that is not already taken.
            while board[row - 1][col - 1] != '':
                print("That spot is full!\nPlease enter valid row and col numbers from 1 to 3:")
                row, col = input_row_col()

            # Updates the board with the players move.
            board[row - 1][col - 1] = player
            print()
            print_board(board) # Prints the updated board.

            # If a player has won, they are notified, and the game ends.
            if check_winner(board):
                print(f"Player {player} WINS!")
                break

            # If there is a tie, the players are notified, and the game ends.
            if all(board[i][j] != '' for i in range(3) for j in range(3)):
                print("It's a TIE!")
                break

            # Sets current player to the opposite player.
            current_player = (current_player + 1) % 2

        # Prompts the player if they would like to play again.
        print("Do you want to play again? Y or N")
        again = input().strip().lower() # assigns users input, stripping it and making it lowercase.

        # While loop iterates until the user enters 'y' or 'n.'
        while again != 'y' and again != 'n':
            print("Please enter valid input: Y or N")
            print("Do you want to play again? Y or N")
            again = input().strip().lower()

        # If they do not want to play again, the infinite loop is broken.
        if again == 'n':
            break

    return times_played