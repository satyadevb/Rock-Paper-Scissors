
from src.control.play import play_game
from src.utils.constants import Identifiers
import os

if __name__ == '__main__':
    os.system('cls')
    while True:
        game_input = input("Hi, shall we begin the game? (Y/N)\n")
        if game_input.lower() in Identifiers['yes']:
            play_game()
            break
        elif game_input.lower() in Identifiers['no']:
            print("Okay.Closing the game\n")
            break
        else:
            print("\nPlease enter valid input\n")
