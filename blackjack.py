
import random # Loads the random module which gives access to different random number related functions.

""" 
Defines function get_sum which takes a player's hand, in the form of a list, and returns the sum of that hand's cards
depending on the card values given by the get_card_value function.
"""
def get_sum(hand: list) -> int:

    sum_hand = 0
    aces = 0

    for card in hand:
        sum_hand += get_card_value(card, hand)

    return sum_hand

"""
Defines get_card_values function which takes a card (string) and the hand that that card is in (list) as parameters.
If the card is a Jack, Queen, or King, the function returns 10 as that cards value.
If the card is an ace, the function creates a copy of the hand and iterates through the copy, deleting the ace in that hand.
This is done so that the get_sum function can be used to find the sum of the hand without any aces.
Depending on the sum of the hand without aces, the value of the removed ace is determined.
If the sum of the hand without the ace plus 11 is less than or equal to 21, the value of the ace is returned as 11.
If the sum of the hand without the ace plus 11 is greater than 21, the value of the ace is returned as 1.
For all other cards, i.e. the number cards, the returned value is the value of that card's number. (ex: 7H returns 7)

"""
def get_card_value(card: str, hand: list) -> int:

    if card[0] == 'J' or card[0] == 'Q' or card[0] == 'K':
        return 10
    elif card[0] == 'A':
        copy_hand = hand[:]
        for i in range(len(hand)):
            if (hand[i][0] == 'A'):
                copy_hand.pop(i)
        if get_sum(copy_hand) + 11 <= 21:
            return 11
        else:
            return 1
    else:
        if len(card) == 2:
            return int(card[0])
        else:
            return (10 + int(card[1]))

"""
Defines deal function which takes the deck as input. An empty list for the player's hand is initialized.
Two cards are then randomly chosen from the deck and those two cards are removed from the deck so they cannot be chosen again.
the hand is then returned which is a list of length two.
"""
def deal(deck: list) -> list:

    hand = []
    for i in range(2):
        card_index = random.randint(0, len(deck) - 1)
        hand.append(deck[card_index])
        deck.pop(card_index)
    
    return hand

"""
Defines hit function which takes the deck (list) and player's hand (list) as parameters.
Similarly to the deal function, a card is randomly chosen from the deck and added to the players hand.
The chosen card is then removed from the deck so it cannot be chosen again.
This function returns nothing.
"""
def hit(deck: list, hand: list) -> None:

    card_index = random.randint(0, len(deck) - 1)
    hand.append(deck[card_index])
    deck.pop(card_index)

# Defines main function for the main program logic.

def play_blackjack() -> None: 
    while True:
        # List of the deck of cards.
        deck = [
            "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH",
            "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD",
            "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC",
            "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS"
        ]

        print("How many players would you like to play with?") # Player is prompted for a number of players which is assigned to variable num_players.
        num_players = int(input())

        while num_players < 0: # If the player does not input a number of players greater than 0, they are asked to input a valid number until they do.
            print("Please enter a value greater than 0: ")
            num_players = int(input())

        all_hands = [] # Empty list all_hands initialized

        """
        For loop adds a hand to all_hands using the deal function for each of the players.
        Each player is asked to acknowledge that they have seen their cards before the program moves on to the next player's cards.
        """
        for i in range(num_players):
            print(f"Player {i + 1}'s cards:")
            all_hands.append(deal(deck))
            print(all_hands[i])
            print(f"Acknowledge that you have seen your cards player {i + 1} by entering any key.")
            acknowledge = input()
        
        print("Now that everyone knows their cards, let's play!")

        all_points = [] # Empty list all_points initialized

        for i in range(num_players): # For loop iterates num_players times. Each loop represents each player's turn.
            print(f"Player {i + 1}'s cards:")
            print(all_hands[i]) # Outputs the player's hand
            points = 0 # Initializes points variable.
            while True: # Infinite while loop that is only broken when a player sticks or busts.
                print(f"Player {i + 1} would you like to hit or stick?") # Player is asked if they would like to hit or stick.
                move = input().strip().lower() # assigns players input to move variable. Leading and trailing whitespace removed, converted to all lowercase.
                while move != "hit" and move != "stick": # If the player did not input hit or stick, while loop loops until they do.
                    print("Invalid input. Please enter either hit or stick: ")
                    move = input().strip().lower()
                if move == "hit": # If statement runs if the player hits.
                    hit(deck, all_hands[i]) # Hit function adds card to players deck
                    print(f"Player {i + 1}'s cards: ")
                    print(all_hands[i]) # Outputs player's new hand.
                    points = get_sum(all_hands[i]) # Assigns points variable with the sum of the player's hand
                    if points > 21: # If statement runs if the player's points are greater than 21.
                        print(f"Player {i + 1} you have busted. Enter any key to acknowledge this.") # Player is notified that they busted, asked to acknowledge.
                        points = -1 # Player's points now set to busted.
                        acknowledge = input()
                        break # Player busted so their turn is now over. Moves to next player's turn.
                else: # Else statement runs if the player sticks.
                    points = get_sum(all_hands[i]) # Player's points are set to the sum of their hand.
                    break # Player sticks so their turn is now over. Moves to next player's turn.
            all_points.append(points) # After each player's turn, that player's points are added to the all_points list.

        for i in range(num_players):
            if all_points[i] == -1: # For each player, if their points equal -1, they are informed that they busted.
                print(f"Player {i + 1} has busted.")

        all_busted = True # Initializes all_busted Boolean to True.

        for num in all_points: # For loop iterates through each player's points.
            if num > 0: # If at least one player did not bust, the all_busted Boolean is set to False
                all_busted = False

        if all_busted: # If all_busted is True, 'Nobody won.' is output and the program is exited.
            print("Nobody won.")
            exit()

        high_score = max(all_points) # The high_score variable is set to the maximum value of the all_points list.
        winners = [] # Empty winners list is initialized
        for i, score in enumerate(all_points): # For loop iterates through all_points list and counts the number of players who share the highest score, if any.
            if score == high_score:
                winners.append(i + 1)
        
        if len(winners) == 1: # If there is only one player with the highest score, The player is notified and given their score.
            print(f"Player {winners[0]} got the highest score of {high_score}.")
        else: # Else, the two players that tied for the highest are notified of their score.
            print(f"Players {winners[0]} and {winners[1]} tied for the highest score of {high_score}.")
        
        print("Would you like to play again? Enter yes or no")
        play_again = input().lower()

        while play_again not in ['yes', 'no']:
            print("Invalid Choice. Enter yes or no")
            play_again = input().lower()

        if play_again == 'no':
            print("Thanks for playing!")
            break
