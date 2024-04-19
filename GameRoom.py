
from blackjack import play_blackjack
from tictactoe import play_tictactoe

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

# Defines Table class which will be used to represent tables within the adventure map.
class Table():

    # Constructor with parameters name, description, and exits.
    # Sets name, description, and exits within the class.
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits
    
    # Getter method returns table name.
    def get_name(self):
        return self.name

    # Getter method returns table description.
    def get_description(self):
        return self.description

    # Getter method returns table exits.
    def get_exits(self):
        return self.exits

    # List exits method joins the exits in exits list with a newline and returns that string.
    def list_exits(self):
        return '\n'.join(self.exits)
    
    # __str__ method returns a string containg the name, description, and exits of the table.
    def __str__(self):
        return f"{self.name}: {self.description}\n\nExits:\n{self.list_exits()}"

# Defines the AdventureMap class which manages the map of tables.
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
def main():

    # Initializes AdventureMap instance.
    game_room_map = GameRoomMap()

    # Adds all tables in the house to the adventure map.
    game_room_map.add_table(Table("Blackjack", "", ["Tic Tac Toe"]))
    game_room_map.add_table(Table("Tic Tac Toe", "", ["Blackjack", "Hangman"]))
    game_room_map.add_table(Table("Hangman", "", ["Tic Tac Toe", "Rock Paper Scissors"]))
    game_room_map.add_table(Table("Rock Paper Scissors", "", ["Hangman", "Number Guesser"]))
    game_room_map.add_table(Table("Number Guesser", "", ["Rock Paper Scissors", "Magic Squares"]))
    game_room_map.add_table(Table("Magic Squares", "", ["Number Guesser", "Word Jumble"]))
    game_room_map.add_table(Table("Word Jumble", "", ["Magic Squares"]))

    # Welcomes user to Game Room.
    print("\nWelcome to the Game Room! Starting at the Blackjack Table. To leave the Game Room, please type exit to jump out of the nearest window.\n")

    # Initializes the current table (blackjack) and gets it from the game_room_map.
    current_table = game_room_map.get_table("Blackjack")

    # Displays the details of the current table.
    print(current_table)

    # Initialies exiting bool to False.
    exiting = False

    # Loops until the user wishes to exit the house.
    while not exiting:

        # Prompts user for exit choice.
        print("Please choose an exit:")

        # Sets users exit choice to user_exit, makes lowercase and strips leading trailing whitespace.
        user_exit = input().lower().strip()

        # Sets the available exits for the current table to exits.
        exits = current_table.get_exits()

        # If the user typed "exit," the while loop will stop, program terminates.
        if user_exit == "exit":
            
            # Informs user that they are exiting the house.
            print("Exiting the house out of the nearest window... thanks for the tour!")

            # Sets exiting bool to True.
            exiting = True
        
        elif user_exit.title() in exits:

            # If the user's choice of exit is not available for the current table, except block runs.
            try:

                # Sets the given exit as the new current table.
                current_table = game_room_map.get_table(user_exit)

                # Outputs the details of the new current table.
                print(current_table)

                if user_exit.title() == "Blackjack":
                    play_blackjack()
                elif user_exit.title() == "Tic Tac Toe":
                    play_tictactoe()

                elif user_exit.title() == "Hangman":
                elif user_exit.title() == "Rock Paper Scissors":
                elif user_exit.title() == "Number Guesser":
                elif user_exit.title() == "Magic Squares":
                elif user_exit.title() == "Word Jumble":


            
            except ExitNotFoundError as e:
                
                # Handles table not found error using ExitNotFoundError class.
                print(e)

        # Runs if the table is not in the house at all.
        else:

            # Informs the user that the table was not found.
            print(f"{user_exit} -> Table not found")

# Runs main program function.                
if __name__ == "__main__":
    main()