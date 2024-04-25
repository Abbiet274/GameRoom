import random # Imports random module.

# get_player_guess function takes no parameters, verifies the user's guess is between 1 and 100, and returns their guess.
def get_player_guess():
    while True:
        print("\nEnter your guess (between 1 and 100):")
        guess = input()
        if guess.isdigit() and 1 <= int(guess) <= 100:
            return int(guess)
        else:
            print("Invalid input. Please enter a number between 1 and 100.")

# game function takes no parameters, selects the random number, and informs the user if their guess is too high or too low.
# If the user's guess is correct, they are informed of the secret number and number if attempts and the loop is broken. 
# Returns the number of attempts.
def game():
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = get_player_guess()
        attempts += 1

        if guess < secret_number:
            print("Too low! Try guessing higher.")
        elif guess > secret_number:
            print("Too high! Try guessing lower.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly.")
            print(f"It took you {attempts} attempts to guess.")
            break

    return attempts

# play_again function takes no parameters, and verifies that the user's answer is yes or no. Returns either yes or no depending on the response.
def play_again():
    print("Do you want to play again? Enter yes or no.")
    again = input().lower().strip()
    while again not in ['yes', 'no']:
        print("Invalid input. Enter yes or no.")
        again = input().lower().strip()
    if again.lower().strip() == 'yes':
        return 'yes'
    return 'no'

# Main game function.
def play_number_guesser():

    print("I'm thinking of a number between 1 and 100.")

    # Initializes times_played to zero.
    times_played = 0

    while True:
        # Increments each time the whole loop iterates.
        times_played += 1

        # runs game and stores users number of attempts. 
        attempts = game()

        # stops program if user no longer wishes to play.
        if play_again() == 'no':
            print("Thanks for playing!")
            break
    
    return times_played
