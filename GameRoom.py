from blackjack import play_blackjack
from tictactoe import play_tictactoe

user_game = input()

if user_game == "b":
    play_blackjack()
elif user_game == "t":
    play_tictactoe()
