import random

# Dictionary of categories and their words
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

def choose_word():
    category_name = random.choice(list(categories.keys()))
    word_list = categories[category_name]
    secret_word = random.choice(word_list)
    return category_name, secret_word

def jumble_word(word):
    """Jumble the given word and return the jumbled version."""
    jumbled_word = ''.join(random.sample(word.lower(), len(word)))
    return jumbled_word

def play_word_jumble():
    while True:
        """Main function to play the word unjumble game."""
        category, secret_word = choose_word()
        jumbled_secret = jumble_word(secret_word)
        
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
