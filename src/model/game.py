import os
from src.model.score import Score
from src.utils.constants import numtomoveMap, Identifiers
from src.utils.logger import get_logger

logger = get_logger()


class Game:

    def __init__(self):
        self.score = Score()

    def get_valid_move(self, move):
        """Find corresponding move for the input"""
        move = move.lower()
        while True:
            try:
                if move in Identifiers['rock']:
                    os.system('cls')
                    logger.info("Rock selected by the player")
                    return 0
                elif move in Identifiers['paper']:
                    os.system('cls')
                    logger.info("Paper selected by the player")
                    return 1
                elif move in Identifiers['scissors']:
                    os.system('cls')
                    logger.info("Scissors selected by the player")
                    return 2
                elif move in Identifiers['quit']:
                    while True:
                        quit_value = input("Are you sure you want to quit:(Y/N)\n")
                        if quit_value.lower() in Identifiers['yes']:
                            return -1
                        elif quit_value.lower() in Identifiers['no']:
                            os.system('cls')
                            return
                        else:
                            os.system('cls')
                            print("\nPlease enter a valid input\n")
                else:
                    raise ValueError
            except ValueError as e:
                os.system('cls')
                print("\nPlease enter a valid move\n")  # logger.error("Please enter a valid move\n")
                return

    def decide_winner(self, player_move, computer_move):
        """Decide the game winner"""
        print("\nYour move:" + numtomoveMap[player_move] + "\t\tComputer's move:" + numtomoveMap[
            computer_move] + "\n")
        self.score.increase_games()
        if player_move - computer_move in [1, -2]:
            print('You win!\n')
            self.score.increase_wins()
        elif player_move - computer_move in [-1, 2]:
            print('Computer wins!\n')
            self.score.increase_losses()
        else:
            print('The game is a tie!\n')
            self.score.increase_ties()

    def show_description(self):
        """Show how the game is played"""
        print("The game is played as follows:\nYou have to choose from Rock/Paper/Scissors\n")
        print("To pick Rock, enter R or Rock\nTo pick Paper, enter P or Paper\nTo pick Scissors, enter S or Scissors\n")
        print("The Computer will pick one of the moves randomly\n")
        print("\nThe rules are:\nRock beats Scissors\nScissors beats Paper\nPaper beats Rock\n")
        print("Your stats will be displayed at the end of the game\n")
        # print("You can enter Q/quit/X/exit at any time to stop the session and quit the game\n")

    def display_stats(self):
        """"Display the number of wins,losses,ties and games in one session"""
        print("Here are your game statistics\n")
        print(f'\nGames played: {self.score.games}\n')
        print(f'\nNumber of wins: {self.score.wins}\n')
        print(f'\nNumber of losses: {self.score.losses}\n')
        print(f'\nNumber of ties: {self.score.ties}\n')
