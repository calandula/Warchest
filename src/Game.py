from Player import Player
from Board import Board
from RecordManager import RecordManager
import random

class Game:
    def __init__(self) -> None:
        self.bag = {
            "Archer": 4,
            "Knight": 5,
            "Mercenary": 5,
            "Crossbowman": 5,
        }
        self.types = [key for key in self.bag.keys()]

    def init_board(self):
        self.board = Board()

    def init_players(self, name1, name2):
        self.players = [Player(name1, "Wolf", "v"), Player(name2, "Crow", "^")]
        self.turn_player_index = random.randint(0, 1)
        random.shuffle(self.types)
        self.players[0].init_pieces(self.types[0:2], self.bag)
        self.players[1].init_pieces(self.types[2:4], self.bag)

    def play(self):
        while True:
            startGame = input("Start game? (y/n): ")
            if startGame.lower() == 'y':
                print("Who will be playing this time?")
                name1 = input("input name of player 1 who will be the Wolf: ")
                name2 = input("input name of player 2 who will be the Crow: ")
                self.init_players(name1, name2)
                self.init_board()
                while not self.board.has_ended():
                    self.turn()
                    if not self.players[self.turn_player_index].has_initiative():
                        self.turn_player_index = (self.turn_player_index + 1) % 2
                    else:
                        self.players[self.turn_player_index].deactivate_initiative()
                RecordManager("db/scoreboard.json").add_record(self.board.get_winner())
                break
            elif startGame.lower() == 'n':
                print("Thank you! See you next time!")
                break
            else:
                print("Oops! incorrect input")
                continue
        

    def turn(self):
        self.board.print_board()
        self.players[self.turn_player_index].decide_actions(self.board)

game = Game().play()




    