import random
import PieceFactory

class Player:
    def __init__(self, clan, emblem) -> None:
        self.clan = clan
        self.letter = self.clan[0]
        self.emblem = emblem
        self.bag = []
        self.hand = []
        self.discard_pile = []
        self.recruitment = {}
        self.control_tokens = 4
        self.has_initiative = False

    def assign_types(self, types, typeCount):
        self.bag.append("Royal")
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
        return self.hand

    def discard_unit(self):
        ...
    
    def place_unit(self, board):
        while True:
            typeToDiscard = input("Piece to place from hand: ")
            if not self.is_in_hand(typeToDiscard) and typeToDiscard == "Royal":
                print("Oops! This unit does not exist, is not in your hand or is the Royal, choose again")
                continue
            self.remove_piece_from_hand(typeToDiscard, False)
            positionToPlace = input("Position to place (ex. b8): ")
            if not self.place(positionToPlace, type, board):
                continue
            break

    def place(self, positionToPlace, type, board):
        piece = PieceFactory(type, self.clan)
        if (not board.is_valid_position(self, positionToPlace) and 
            not board.is_orthogonal_to_control_zone(self, positionToPlace, self.clan)):
            return False
        board.put_piece(self, positionToPlace, piece)
        return True

    def control_zone(self):
        ...

    def move_unit(self):
        ...

    def recruit_unit(self):
        while True:
            typeToDiscard = input("Piece to discard from hand to recruit the same kind: ")
            if not self.is_in_hand(typeToDiscard):
                print("Oops! This unit does not exist or is not in your hand, choose again")
                continue
            if typeToDiscard == "Royal":
                while True:
                    typeToRecruit = input("Used Royal coin, type the piece you want to recruit: ")
                    if not self.can_recruit(typeToRecruit):
                        print("Oops! You cannot recruit this unit, try again")
                        continue
                    self.recruit(typeToDiscard, typeToRecruit)
            else:
                self.recruit(typeToDiscard, typeToDiscard)
            break

    def recruit(self, typeToDiscard, typeToRecruit):
        self.remove_piece_from_hand(typeToDiscard)
        self.recruitment[typeToRecruit] -= 1

    def can_recruit(self, type):
        if self.recruitment[type] > 0:
            return True
        return False
    
    def is_in_hand(self, type):
        return type in self.hand

    def attack_unit(self):
        ...

    def take_initiative(self):
        while True:
            typeToDiscard = input("Piece to discard from hand: ")
            if not self.is_in_hand(typeToDiscard):
                print("Oops! This unit does not exist or is not in your hand, choose again")
                continue
            self.initiative(typeToDiscard)
            break

    def initiative(self, typeToDiscard):
        self.remove_piece_from_hand(typeToDiscard)
        self.initiative = True

    def remove_piece_from_hand(self, typeToDiscard, isDiscarded=True):
        self.hand.remove(typeToDiscard)
        if isDiscarded:
            self.discard_pile.append(typeToDiscard)

    def decide_actions(self, board):
        while len(self.hand) > 0:
            while True:
                action = input("Make an action (move/recruit/place/attack/control/initiative/forfeit): ")
                action = action.lower()
                if action == "move":
                    ...
                elif action == "recruit":
                    self.recruit_unit()
                elif action == "place":
                    self.place_unit(board)
                elif action == "attack":
                    ...
                elif action == "control":
                    ...
                elif action == "initiative":
                    self.take_initiative()
                elif action == "forfeit":
                    ...
                else:
                    print("Oops! This action does not exist!")
                    continue
                break
            print(f"Hand: {self.hand.join(', ')}")
        
            

    def print_status(self):
        print(f"========= {self.clan} ({self.emblem}) =========")
        print(f"Hand: {self.draw_units.join(', ')}")
        print(f"Recruitment pieces: {[f'{k} = {v}' for (k, v) in self.recruitment.items()].join(', ')}")
        print("Discard pile:")
        print(f"{self.discard_pile.join(', ')}")
        print(f"Control tokens: {self.control_tokens}")
