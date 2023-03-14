import Player
import random
import Board

class Game:
    def __init__(self) -> None:
        self.players = [Player("Wolf"), Player("Crow")]
        self.bag = {
            "archer": 4,
            "berserker": 4,
            "cavalry": 4,
            "crossbowman": 5,
        }
        self.types = [key for key in self.bag.keys()]
        self.game_over = False
        self.turn_player_index = 0
        self.players[0].assign_types(random.shuffle(self.types)[0:2], self.bag)
        self.players[1].assign_types(random.shuffle(self.types)[2:4], self.bag)



    