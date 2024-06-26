"""
Author: Abbie Thompson
Date: 4/24/2024
Assignment: RPG Project: The Game Room
Course: CPSC1050

THE GAME ROOM DESCRIPTION: The Game Room is a terminal bases RPG game that allows the user to roam the game room and play a variety of game.
These games include Blackjack, Tic-Tac-Toe, Hangman, Magic Squares, Rock Paper Scissors, Number Guesser, and Word Jumble.
The user must start at the Blackjack table, but they are then able to stay or jump from table to table by requesting through the Game Master.
The number of times each game is played is recorded and saved to a json file, which is displayed once the user exit's the Game Room
by typing "exit" instead of their next table.

GitHub Link: https://github.com/Abbiet274/GameRoom

"""
# Imports functions from each game module, random module, and json module.

import json
import random
from blackjack import play_blackjack
from tictactoe import play_tictactoe
from hangman import play_hangman
from magicsquares import play_magic_squares
from rockpaperscissors import play_rps
from numberguesser import play_number_guesser
from wordjumble import play_word_jumble

# Function to print out the Game Room Map.
def print_map():
    print("""
        Game Room Map:
 _______   _______   _______
|       | |       | |Number |
|Hangman| |R.P.S. | |Guesser|
|_______| |_______| |_______|
 _______             _______   
|  Tic  |           | Magic | 
|Tac Toe|           |Squares| 
|_______|           |_______| 
 _______             _______  
| Black |           | Word  |
| Jack  |           |Jumble | 
|_______|           |_______| 
    o
   /|\\ <- You are here!
   / \\ 

""")

# Defines custom exception class which handles any table not found errors.
class ExitNotFoundError(Exception):

    # Constructor with paramenters table_name and message with default argument "Table not found."
    # Sets message and table_name within the class.
    def __init__(self, table_name, message="Table not found"):
        self.message = message
        self.table_name = table_name
    
    # __str__ method returns the table name and message.
    def __str__(self):
        return f"{self.table_name} -> {self.message}"

# Defines Table class which will be used to represent tables within the game room map.
class Table():

    # Constructor with parameters name, rules, and exits.
    # Sets name, rules, and exits within the class.
    def __init__(self, name, rules, exits):
        self.name = name
        self.rules = rules
        self.exits = exits
    
    # Getter method returns table name.
    def get_name(self):
        return self.name

    # Getter method returns table rules.
    def get_rules(self):
        return self.rules

    # Getter method returns table exits.
    def get_exits(self):
        return self.exits

    # List exits method joins the exits in exits list with a newline and returns that string.
    def list_exits(self):
        return '\n'.join(self.exits)
    
    # __str__ method returns a string containg the name and rules for the game.
    def __str__(self):
        return f"{self.name} Master: Hey! You've reached the {self.name} table! Here are some rules...\n\n{self.rules}\n"

# Defines the GameRoomMap class which manages the map of tables.
class GameRoomMap():

    # Contructor with no paramenters.
    # Initializes empty map dictionary within the class.
    def __init__(self):
        self.map = {}
    
    # Add table method takes the table obeject as a paramenter.
    # Adds the lowercase name of the table as the key and the table object as the value.
    def add_table(self, table):
        self.map[table.name.lower()] = table

    # Getter method takes the table name as a paramenter.
    # If the table exits in the map, returns the table object for that given name.
    # If not, ExitNotFoundError is raised with table_name as the argument.
    def get_table(self, table_name):
        if table_name.lower() in self.map.keys():
            return self.map[table_name.lower()]
        else:
            raise ExitNotFoundError(table_name)

# Defines main program function.
def game_room():

    # Initializes CameRoomMap instance game_room_map.
    game_room_map = GameRoomMap()

    # Creates 7 Table objects for each of the games and passes the name, rules, and exits for each.
    blackjack_table = Table("Blackjack", "The goal of the game is to get a hand total as close to 21 as possible without going over. Each player receives two cards initially, and cards are valued by their face value (2-10), with face cards worth 10 and Aces worth 1 or 11. Decide whether to 'hit' (take another card) or 'stick' (keep your current hand) to reach a total close to 21. If you exceed 21, you bust. After all players finish, the players are notified who won, if anyone tied, and who busted. Have fun!", ["Tic Tac Toe"])
    ttt_table = Table("Tic Tac Toe", "The game is played on a 3x3 grid where two players take turns marking spaces with their symbol (X or O). The objective is to get three of your symbols in a row horizontally, vertically, or diagonally. Players alternate turns placing their symbol in any empty grid space. The first player to create a row of three of their symbols wins the game. If all spaces are filled without a winner, the game ends in a tie. Have fun!", ["Blackjack", "Hangman"])
    hangman_table = Table("Hangman", "The goal of the game is to guess the given word(s), whose letters are represented by underlines, before being hung. You get six guesses before you lose! If you guess correctly, the letter you guess replaces the corresponding underscore. If you guess all of the letters, you win! If not, you are hanged… Have fun!", ["Tic Tac Toe", "Rock Paper Scissors"])
    rps_table = Table("Rock Paper Scissors", "In this game, each player selects either Rock, Paper, or Scissors. Rock beats Scissors, Scissors beats Paper, and Paper beats Rock. Players reveal their choices simultaneously, and the winner is determined based on the previously mentioned rules. Have fun!", ["Hangman", "Number Guesser"])
    num_guess_table = Table("Number Guesser", "In this game, you will attempt to guess a random number between 1 and 100. After guessing, you will be told if your guess was too high or too low. After each round, the game displays the number of attempts it took to guess correctly. You can choose whether you would like to play more than one round. The objective is to guess the number in the fewest attempts possible. Have fun!", ["Rock Paper Scissors", "Magic Squares"])
    magic_table = Table("Magic Squares", "The objective of the game is to arrange numbers within a grid so that each row, column, and diagonal adds up to the same sum. To start, select a grid size (for example, 3x3, 4x4, 5x5, etc.). You'll begin with an empty grid of the chosen size. Your task is to fill in every cell of the grid with numbers from 1 to n^2 (where n is the size of the grid) such that no number is repeated within the same grid. As you fill in the grid, ensure that each row, column, and diagonal totals to the same sum. You will then be notified if the square is magic or not. Have fun!", ["Number Guesser", "Word Jumble"])
    wordj_table = Table("Word Jumble", "In this game, you will be given a jumbled word from a random category. Your task is to unscramble the letters to guess the correct word related to that category. If you guess correctly, you win! Have fun!", ["Magic Squares"])

    # Adds all tables in the house to the game room map.
    game_room_map.add_table(blackjack_table)
    game_room_map.add_table(ttt_table)
    game_room_map.add_table(hangman_table)
    game_room_map.add_table(rps_table)
    game_room_map.add_table(num_guess_table)
    game_room_map.add_table(magic_table)
    game_room_map.add_table(wordj_table)

    # Opens previously saved game data (number of times each game has been played.).
    # If no game data exits, the times played for each game is set to zero.
    try:
        with open("timesplayed.json", "r") as file:
            times_played = json.load(file)
    except FileNotFoundError:
        print('file reset')
        times_played = {"Blackjack": 0, "Tic Tac Toe": 0, "Hangman": 0, "Rock Paper Scissors": 0, "Number Guesser": 0, "Magic Squares": 0, "Word Jumble": 0}

    # Welcomes user to Game Room and informs them that they are starting at the Backjack table.
    print("\nWelcome to the Game Room! You are currently at the blackjack table. To leave the Game Room, please type 'exit,' instead of your next game.\n")

    # Displays Game Room map.
    print_map()

    # Initializes the current table (blackjack) and gets it from the game_room_map.
    current_table = game_room_map.get_table("Blackjack")

    # Displays the details of the current table.
    print(current_table)

    # increments the number of times the user plays Blackjack.
    times_played["Blackjack"] += play_blackjack()

    # Displays the tables which are reachable from the Blackjack table.
    print(f"\nReachable Tables:\n{blackjack_table.list_exits()}")

    # Initializes exiting bool to False.
    exiting = False

    # Loops until the user wishes to exit the Game Room.
    while not exiting:

        # The game master prompts the user for their next table choice.
        print(f"\n{current_table.get_name()} Master: What table would you like to choose next? \n(Enter 'exit' if you would like to leave.)")

        # Sets users exit choice to user_exit, makes lowercase and strips leading trailing whitespace.
        user_exit = input().lower().strip()

        # Sets the available exits for the current table to exits.
        exits = current_table.get_exits()

        # If the user typed "exit," the while loop will stop, program terminates.
        if user_exit == "exit":
            
            # Informs user that they are exiting the Game Room.
            print(f"{current_table.get_name()} Master: All right! I will show you to the exit... thanks for playing!")

            # Sets exiting bool to True.
            exiting = True

        elif user_exit.title() in exits:

            # If the user's choice of exit is not available for the current table, except block runs.
            try:

                # Sets the given exit as the new current table.
                current_table = game_room_map.get_table(user_exit)

                # Outputs the details of the new current table.
                print(f"\n{current_table}")

                # Game master asks the user if they would like to stay at the table they have chosen or if they would like to jump to a new one.
                print(f"{current_table.get_name()} Master: Would you like to stay at this table? Or would you like to jump to a new table without playing?")
                answer = input().lower().strip()

                # Ensures that the user responds with either stay or jump.
                while answer not in ['stay', 'jump']:
                    responses = ["Sorry, I'm not quite sure what you wanna do... A simple 'stay' or 'jump' will do!", "What was that? I didn't quite hear you.", "Answer with either 'stay' or 'jump!'"]
                    print(f"{current_table.get_name()} Master: {random.choice(responses)}")
                    answer = input().lower().strip()

                # If the user would like to jump to a new table, the user is given the new list of reachable tables, and the while loop is continued from the top.
                if answer == "jump":
                    print(f"\nReachable Tables:\n{current_table.list_exits()}")
                    continue

                # Initializes variable times to zero.
                times = 0

                # Depending on the chosen table name, the corresponding game function is called.
                # Each of the game functions returns the number of times they were played, therefore that number is assigned to the times variable.
                if user_exit.title() == "Blackjack":
                    times = play_blackjack()
                elif user_exit.title() == "Tic Tac Toe":
                    times = play_tictactoe()
                elif user_exit.title() == "Hangman":
                    times = play_hangman()
                elif user_exit.title() == "Rock Paper Scissors":
                    times = play_rps()
                elif user_exit.title() == "Number Guesser":
                    times = play_number_guesser()
                elif user_exit.title() == "Magic Squares":
                    times = play_magic_squares()
                elif user_exit.title() == "Word Jumble":
                    times = play_word_jumble()

                # Sets the existing number of times played for the chosen table to current_times.
                current_times = times_played[current_table.get_name()]

                # Sets the times_played for the chosen table to the current number of times plus the new number of times.
                times_played[current_table.get_name()] = current_times + times

                # Displays the new reachable tables based on the chosen table.
                print(f"\nReachable Tables:\n{current_table.list_exits()}")
                
            except ExitNotFoundError as e:
                
                # Handles table not found error using ExitNotFoundError class.
                print(e)

        # Runs if the table is not in the Game Room at all.
        else:

            # Informs the user that the table was not found.
            print(f"{user_exit} -> Table not found")

    # Writes the newly collected game data to the timesplayed.json file.
    # Informs the user that the game session data was saved.
    with open("timesplayed.json", "w") as file:
        json.dump(times_played, file, indent=4)
        print("Game session data saved.\nBelow is the total number of times each game has been played:")

    # Reads the new times_played data from the timesplayed.json file and assigns it to the all_data variable.
    with open("timesplayed.json", "r") as file:
        all_data = json.load(file) 

    # Displays the newly saved times_played data.
    for name, count in all_data.items():
        print(f"   {name}: {count}")

# Runs main program function.                
if __name__ == "__main__":
    game_room()