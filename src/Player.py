import random

class Player:
    def __init__(self, clan) -> None:
        self.clan = clan
        self.bag = []
        self.hand = []
        self.discard_pile = []
        self.recruitment = []
        self.control_token = 4

    def assign_types(self, types, typeCount):
        self.bag.append("royal")
        for type in types:
            self.bag.append(type)
            self.bag.append(type)
            typeCount[type] -= 2

        self.recruitment = {key:value for (key, value) in typeCount if key in types}

    def draw_units(self):
        if self.bag < 3:
            self.bag = [*self.bag, *self.discard_pile]
            self.discard_pile = []
        self.hand = random.shuffle(self.bag)[0:3]

    def discard_unit(self):
        ...
    
    def place_unit(self):
        ...

    def control_zone(self):
        ...

    def move_unit(self):
        ...

    def recruit_unit(self):
        ...

    def attack_unit(self):
        ...

    def take_initiative(self):
        ...
