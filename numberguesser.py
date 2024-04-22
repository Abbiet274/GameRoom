import random

def get_player_guess():
    while True:
        print("\nEnter your guess (between 1 and 100):")
        guess = input()
        if guess.isdigit() and 1 <= int(guess) <= 100:
            return int(guess)
        else:
            print("Invalid input. Please enter a number between 1 and 100.")

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

def play_again():
    print("Do you want to play again? Enter yes or no.")
    again = input().lower().strip()
    while again not in ['yes', 'no']:
        print("Invalid input. Enter yes or no.")
        again = input().lower().strip()
    if again.lower().strip() == 'yes':
        return 'yes'
    return 'no'

def play_number_guesser():

    print("I'm thinking of a number between 1 and 100.")

    times_played = 0
    while True:
        times_played += 1
        attempts = game()

        if play_again() == 'no':
            print("Thanks for playing!")
            break
    
    return times_played
