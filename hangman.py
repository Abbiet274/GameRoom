
import random # Imports the random module.

def print_gallows(num_wrong_guesses: int) -> None:

    """ Prints gallows depending on the number of wrong guesses.

    Args: man_stages: Dict with the 7 different stages of the gallows (0-6 wrong guesses)
    prints the key which corresponds to the number of wrong guesses the user has.
    
    Return: None.

    """
    str_wrong = str(num_wrong_guesses)

    man_stages = {'0':
    """
        +---+
        |   |
            |
            |
            |
            |
        =========
    """, '1':
    """
        +---+
        |   |
        O   |
            |
            |
            |
        =========
    """, '2':
    """
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========
    """, '3':
    """
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========
    """, '4':
    """
        +---+
        |   |
        O   |
       /|\\  |
            |
            |
        =========
    """, '5':
    """
        +---+
        |   |
        O   |
       /|\\  |
       /    |
            |
        =========
    """, '6':
    """
        +---+
        |   |
        O   |
       /|\\  |
       / \\  |
            |
        =========
    """
    }

    print(man_stages[str_wrong])

def choose_word(category: str) -> str:
        
    """ Chooses word(s) from chosen catagory.

    Args: None.

    Return: Random choice from the catagory given in catagories dict.

    """
    return random.choice(categories[category])

def print_word(word: str, displayed_word: list, guess='-1') -> None:
        
    """ Prints the displayed word, updating if the guessed letter is in word.

    Args: For loop interates len(word) times, setting displayed _word[i] to word[i] if the users guess was correct and
    prints joined displayed word.
    
    Return: None.

    """
    for i in range(len(word)):
        if word[i].lower() == guess:
            displayed_word[i] = word[i]
        
    print(''.join(displayed_word))

# Dict of catagories with words in each catagory.
categories = {
    'places': ['New York', 'Los Angeles', 'California', 'Chicago', 'Illinois',  
        'Houston', 'Texas', 'Philadelphia', 'Pennsylvania', 'Phoenix', 'Arizona', 'San Antonio', 
        'San Diego', 'Dallas', 'San Jose', 'Austin', 'Texas', 'Jacksonville', 'Florida', 
        'San Francisco', 'Indianapolis', 'Indiana', 'Massachusetts', 'Mississippi'],
    'movies': ["The Godfather", "The Shawshank Redemption",
        "Raging Bull", "Casablanca", "Citizen Kane", "Gone With The Wind", "The Wizard Of Oz",
        "Inception"],
    "ta": ["Richard", "John", "Mars", "Aaron", "Brendan", "Jada", "Braylon"]
}

# Main program function.
def play_hangman():
    while True:
        cat = random.choice(list(categories.keys())) # Chooses a random catagory from catagories, assigned to cat.
        
        print(f"\nThe category is: {cat}\n") # Player is told their catagory.

        word = choose_word(cat) # choose_word function run with chosen catagory, word assigned with word(s).
        displayed_word = [] # Initializes empty list displayed_word.

        # For loop iterates len(word) times and appends an "_" to displayed_word for each letter in word and a " " for each space.
        for i in range(len(word)):

            if word[i].isalpha():
                displayed_word.append('_')
            else:
                displayed_word.append(' ')

        
        num_wrong_guesses = 0 # Initializes num_wrong_guesses variable.
        guesses = [] # Initializes empty list guesses.

        print_gallows(num_wrong_guesses) # print_gallows function ran with num_wrong_guesses = 0.
        print_word(word, displayed_word) # print_word function ran with word and displayed_word as inputs.

        playing = True # Initializes playing boolean to True.

        # While loop iterates until playing = False.
        while playing:

            print("Guess a letter: ") # User is asked to guess a letter.
            guess = input().strip().lower() # Users guess is stripped and turned all lowercase, assigned to guess variable.

            # While loop iterates until user inputs a single letter that has not already been guessed, guess assigned as above.
            while (len(guess) != 1) or (guess in guesses):
                if (len(guess) != 1):
                    print("Please enter in just a singular letter")
                    guess = input().strip().lower()
                else:
                    print("You have already guessed that letter!")
                    guess = input().strip().lower()

            guesses.append(guess) # Adds user's guess to list of guesses.
            
            # If the user's guess is in word, the user is informed they are correct and the gallows and word(s) are printed with updated parameters.
            if guess.lower() in word.lower():
                print("Correct!")
                print_gallows(num_wrong_guesses)
                print_word(word, displayed_word, guess)
            # Else, the user is informed that their guess is not in the word, num_wrong_guesses incremented.
            else:
                print(f"There are no {guess}'s")
                num_wrong_guesses += 1
                # If num_wrong_guesses is under 6, the game continues and the gallows and word(s) are printed with updated parameters.
                if num_wrong_guesses < 6:
                    print_gallows(num_wrong_guesses)
                    print_word(word, displayed_word, guess)

            # If the user guesses all of the letter in the word(s) the playing boolean is set to False, stopping the loop, and winner boolean is set to True.
            if '_' not in displayed_word:
                playing = False
                winner = True

            # If num_wrong_guesses is 6, the user used all their guesses, playing and winner booleans are set to False.
            if num_wrong_guesses == 6:
                playing = False
                winner = False
        
        # If winner is true, user is informed that they won.
        if winner:
            print("You have won!")
        # Else: the winner is informed that they lost, they are told the word, the gallows with full man is printed, and the displayed word is printed.
        else:
            print("Gave Over, you are HANGED!")
            print(f"The word was: {word}")
            print("Better luck next time.")
            print_gallows(num_wrong_guesses)
            print_word(word, displayed_word, guess)
        
            print("Would you like to play again? Enter yes or no")
            play_again = input().lower()

            while play_again not in ['yes', 'no']:
                print("Invalid Choice. Enter yes or no")
                play_again = input().lower()

            if play_again == 'no':
                print("Thanks for playing!")
                break
