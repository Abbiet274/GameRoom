
def get_player_choice(player_number):
    print(f"Player {player_number}, enter 'rock', 'paper', or 'scissors': ")
    choice = input().lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        choice = input().lower()
    return choice

def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "It's a tie!"
    elif (player1_choice == 'rock' and player2_choice == 'scissors') or (player1_choice == 'paper' and player2_choice == 'rock') or (player1_choice == 'scissors' and player2_choice == 'paper'):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def play_rps():
    times_played = 0
    while True:
        times_played += 1
        player1_choice = get_player_choice(1)
        player2_choice = get_player_choice(2)
        print(determine_winner(player1_choice, player2_choice))
        print("Play again? Enter yes or no")
        play_again = input().lower()
        while play_again not in ['yes', 'no']:
            print("Invalid Choice. Enter yes or no")
            play_again = input().lower()
        if play_again == 'no':
            print("Thanks for playing!")
            break
    return times_played