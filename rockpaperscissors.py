# Function get's user's choice of rock, paper, or scissors. Verifies that their answer is one of the three.
# Returns the user's choice.
def get_player_choice(player_number):
    print(f"Player {player_number}, enter 'rock', 'paper', or 'scissors': ")
    choice = input().lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        choice = input().lower()
    return choice

# If both players have the same choice, it's a tie.
# informs which player won if choices are different depending on game rules.
def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "It's a tie!"
    elif (player1_choice == 'rock' and player2_choice == 'scissors') or (player1_choice == 'paper' and player2_choice == 'rock') or (player1_choice == 'scissors' and player2_choice == 'paper'):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

# Main game function.
def play_rps():

    # Intializes times_played variable.
    times_played = 0

    while True:

        # Increments times_played each time the loop iterates.
        times_played += 1

        # gets each player's choice.
        player1_choice = get_player_choice(1)
        player2_choice = get_player_choice(2)
        
        # Informs who won.
        print(determine_winner(player1_choice, player2_choice))

        # Asks if the players want to play again.
        print("Play again? Enter yes or no")
        play_again = input().lower()

        # Verifies the answer is yes or no.
        while play_again not in ['yes', 'no']:
            print("Invalid Choice. Enter yes or no")
            play_again = input().lower()

        # If no, ends game.
        if play_again == 'no':
            print("Thanks for playing!")
            break

    return times_played