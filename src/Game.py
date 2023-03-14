import Player
import random
import Board
import RecordManager

class Game:
    def __init__(self) -> None:
        self.players = [Player("Wolf", "v"), Player("Crow", "^")]
        self.bag = {
            "Archer": 4,
            "Berserker": 4,
            "Cavalry": 4,
            "Crossbowman": 5,
        }
        self.types = [key for key in self.bag.keys()]
        self.game_over = False
        self.turn_player_index = 0
        self.board = Board()
        randomizedTypes = random.shuffle(self.types)
        self.players[0].assign_types(randomizedTypes[0:2], self.bag)
        self.players[1].assign_types(randomizedTypes[2:4], self.bag)

    def play(self):
        while True:
            startGame = input("Start game? (y/n):")
            if startGame.lower() == 'y':
                while not self.game_over:
                    ...
            elif startGame.lower() == 'n':
                print("Thank you! See you next time!")
                break
            else:
                print("Oops! incorrect input")
                continue

    def turn(self):
        self.board.print_board()
        self.players[self.turn_player_index].print_status()
        self.players[self.turn_player_index].decide_actions(self.board)



    