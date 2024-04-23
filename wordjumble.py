import random

class WordJumbleGame:
    def __init__(self, categories):
        self.categories = categories
        self.times_played = 0

    def choose_word(self):
        category_name = random.choice(list(self.categories.keys()))
        word_list = self.categories[category_name]
        secret_word = random.choice(word_list)
        return category_name, secret_word

    def jumble_word(self, word):
        jumbled_word = ''.join(random.sample(word.lower(), len(word)))
        return jumbled_word

    def play(self):
        while True:
            self.times_played += 1
            category, secret_word = self.choose_word()
            jumbled_secret = self.jumble_word(secret_word)

            print(f"Category: {category}s")
            print(f"Unjumble the {category}: {jumbled_secret}")
            guess = input().strip().title()

            if guess == secret_word:
                print(f"Congratulations! You guessed the {category} correctly.")
            else:
                print(f"Sorry, the correct {category} was '{secret_word}'.")

            print("Would you like to play again? Enter yes or no")
            play_again = input().lower()

            while play_again not in ['yes', 'no']:
                print("Invalid Choice. Enter yes or no")
                play_again = input().lower()

            if play_again == 'no':
                print("Thanks for playing!")
                break

class PlayWordJumble(WordJumbleGame):
    def __init__(self, categories):
        super().__init__(categories)

    def play(self):
        super().play()

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

def play_word_jumble():
    game = PlayWordJumble(categories)
    game.play()
    return game.times_played
