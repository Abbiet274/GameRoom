import random

# Base class includes main game methods.
class WordJumbleGame:

    # Constructor sets catagories, then times_played to zero.
    def __init__(self, categories):
        self.categories = categories
        self.times_played = 0

    # Chooses a random category, then random word from that catagory, they returns both the catagory and the word.
    def choose_word(self):
        category_name = random.choice(list(self.categories.keys()))
        word_list = self.categories[category_name]
        secret_word = random.choice(word_list)
        return category_name, secret_word

    # Jumbles the chosen word and returns it.
    def jumble_word(self, word):
        jumbled_word = ''.join(random.sample(word.lower(), len(word)))
        return jumbled_word

    # Main game method.
    def play(self):
        while True:
            # Increments times_played each time while loop iterates. 
            self.times_played += 1

            # gets category, word, and jumbled word.
            category, secret_word = self.choose_word()
            jumbled_secret = self.jumble_word(secret_word)

            # Displays category and the jumbled word.
            print(f"Category: {category}s")
            print(f"Unjumble the {category}: {jumbled_secret}")
            # Set's user's guess from input.
            guess = input().strip().title()

            # Tells user if they won or lost.
            if guess == secret_word:
                print(f"Congratulations! You guessed the {category} correctly.")
            else:
                print(f"Sorry, the correct {category} was '{secret_word}'.")

            # Asks user if they want to play again.
            print("Would you like to play again? Enter yes or no")
            play_again = input().lower()

            # Verifies their answer is yes or no.
            while play_again not in ['yes', 'no']:
                print("Invalid Choice. Enter yes or no")
                play_again = input().lower()

            # End game if no.
            if play_again == 'no':
                print("Thanks for playing!")
                break

# Inherited class runs the word jumble game.
class PlayWordJumble(WordJumbleGame):
    def __init__(self, categories):
        super().__init__(categories)

    def play(self):
        super().play()

# Creates categories and their words.
categories = {
    'place': ['New York', 'Los Angeles', 'California', 'Chicago', 'Illinois',  
               'Houston', 'Texas', 'Philadelphia', 'Pennsylvania', 'Phoenix', 
               'Arizona', 'San Antonio', 'San Diego', 'Dallas', 'San Jose', 
               'Austin', 'Jacksonville', 'Florida', 'San Francisco', 
               'Indianapolis', 'Indiana', 'Massachusetts', 'Mississippi'],
    'movie': ["The Godfather", "The Shawshank Redemption", "Raging Bull", 
               "Casablanca", "Citizen Kane", "Gone With The Wind", 
               "The Wizard Of Oz", "Inception"],
    'TA': ["Richard", "John", "Mars", "Aaron", "Brendan", "Jada", "Braylon"],
    'animal': ["Lion", "Elephant", "Tiger", "Giraffe", "Monkey", "Penguin", 
                "Kangaroo", "Dolphin", "Panda", "Zebra", "Eagle", "Ostrich"]
}

# main game function.
def play_word_jumble():

    # Creates instance of PlayWordJumble
    game = PlayWordJumble(categories)
    
    # Runs game.
    game.play()

    return game.times_played
