import os
import random
from src.model.game import Game

from src.utils.logger import get_logger

logger = get_logger()


def play_game():
    os.system('cls')
    game = Game()
    game.show_description()
    while True:
        print('You can enter Q/quit/X/exit at any time to stop the session and quit the game\n')
        input_str = input('Choices: (R)ock or (P)aper or (S)cissors \nChoose one of them:\n')
        player_move = game.get_valid_move(input_str)
        if player_move in [0, 1, 2]:
            computer_move = random.randint(0, 2)
            game.decide_winner(player_move, computer_move)
        elif player_move == -1:
            #If player wants to quit the game
            logger.info("Quitting the game!\n")
            os.system('cls')
            print("\nThank you for playing\n")
            break
    game.display_stats()
