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

    def init_pieces(self, types, typeCount):
        self.bag.append(PieceFactory().get_piece("Royal", self.clan))
        for type in types:
            self.bag.append(PieceFactory().get_piece(type, self.clan))
            self.bag.append(PieceFactory().get_piece(type, self.clan))
            typeCount[type] -= 2
        self.recruitment = {key:value for (key, value) in typeCount if key in types}

    def draw_units(self):
        if self.bag < 3:
            self.bag = [*self.bag, *self.discard_pile]
            self.discard_pile = []
        self.hand = random.shuffle(self.bag)[0:3]
        return self.hand

    def discard(self, typeToDiscard):
        self.discard_pile.append(PieceFactory().get_piece(typeToDiscard, self.clan))

    def remove_from_hand(self, typeToRemoveFromHand):
        for piece in self.hand:
            if piece.type == typeToRemoveFromHand:
                self.hand.remove(piece)
                break
    
    def place_unit(self, board):
        while True:
            type = input("Piece to place from hand: ")
            if not self.is_in_hand(type) or type == "Royal":
                continue
            positionToPlace = input("Position to place (ex. b8): ")
            if not self.place(positionToPlace, type, board):
                continue
            self.remove_from_hand(type)
            break

    def place(self, positionToPlace, typeToDiscard, board):
        piece = PieceFactory().get_piece(typeToDiscard, self.clan)
        if (not board.is_valid_position(positionToPlace) or 
            not board.is_orthogonal_to_control_zone(positionToPlace, self.clan)):
            print("Oops! Invalid position, it must be orthogonal to a control zone already taken")
            return False
        board.put_piece(positionToPlace, piece)
        return True

    def control_zone(self):
        ...

    def move_unit(self, board):
        while True:
            startPosition = input("From position (ex. a8): ")

            if (not board.is_valid_position(startPosition) or
                not board.is_my_piece(startPosition, self.clan)):
                print("Oops! You input a bad position, the position was empty or you cannot move that piece")
                continue

            type = input("Select a piece of the same type in your hand: ")

            if not self.is_in_hand(type) and type == "Royal" and board.is_piece_from_same_type(self, startPosition, type):
                print("Oops! You input a bad piece type or is Royal piece")
                continue

            endPosition = input("To position (ex. a8): ") 

            if (not board.is_valid_position(endPosition) or
                not board.is_empty(endPosition) or
                not board.can_move(startPosition, endPosition)):
                print("Oops! You input a bad position, the position was empty or you cannot move that piece in that way")
                continue

            board.move_piece(startPosition, endPosition)
            self.remove_from_hand(type)
            self.discard(type)
            
            break

    def recruit_unit(self):
        while True:
            type = input("Piece to discard from hand to recruit the same kind: ")
            if not self.is_in_hand(type):
                print("Oops! This unit does not exist or is not in your hand, choose again")
                continue
            if type == "Royal":
                while True:
                    typeToRecruit = input("Used Royal coin, type the piece you want to recruit: ")
                    if not self.can_recruit(typeToRecruit):
                        print("Oops! You cannot recruit this unit, try again")
                        continue
                    self.recruit(type, typeToRecruit)
            else:
                self.recruit(type, type)
            break

    def recruit(self, typeToDiscard, typeToRecruit):
        self.remove_from_hand(typeToDiscard)
        self.hand.append(PieceFactory().get_piece(typeToDiscard, self.clan))
        self.recruitment[typeToRecruit] -= 1

    def can_recruit(self, type):
        if self.recruitment[type] > 0:
            return True
        return False
    
    def is_in_hand(self, type):
        return type in [piece.type for piece in self.hand]

    def attack_unit(self, board):
        while True:
            startPosition = input("Attack from position (ex. a8): ")
            if (not board.is_valid_position(startPosition) and
                not board.is_my_piece(startPosition, self.clan)):
                print("Oops! You input a bad position, the position was empty or you cannot move that piece")
                continue
            typeToDiscard = input("Select a piece of the same type in your hand: ")
            if not self.is_in_hand(typeToDiscard) and typeToDiscard == "Royal" and board.is_piece_from_same_type(self, startPosition, typeToDiscard):
                print("Oops! You input a bad piece type or is Royal piece or the type does not concur")
                continue
            endPosition = input("To position (ex. a8): ") 
            if (not board.is_valid_position(endPosition) and
                not board.is_empty(endPosition) and
                not board.can_attack(startPosition, endPosition)):
                print("Oops! You input a bad position, the position was empty or you cannot move that piece")
                continue

            board.attack_piece(startPosition, endPosition)
            self.remove_from_hand(type)
            self.discard(type)
            break

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

    def decide_actions(self, board):
        while len(self.hand) > 0:
            while True:
                action = input("Make an action (move/recruit/place/attack/control/initiative/forfeit): ")
                action = action.lower()
                if action == "move":
                    self.move_unit()
                elif action == "recruit":
                    self.recruit_unit()
                elif action == "place":
                    self.place_unit(board)
                elif action == "attack":
                    self.attack_unit()
                elif action == "control":
                    self.control_zone()
                elif action == "initiative":
                    self.take_initiative()
                elif action == "forfeit":
                    self.forfeit()
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
