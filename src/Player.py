import random
from PieceFactory import PieceFactory
from Board import Board

class Player:
    def __init__(self, name, clan, emblem) -> None:
        self.clan = clan
        self.letter = self.clan[0]
        self.emblem = emblem
        self.name = name
        self.bag = []
        self.hand = []
        self.discard_pile = []
        self.recruitment = {}
        self.control_tokens = 4
        self.control_zones = []
        self.initiative = False

    def init_pieces(self, types, typeCount):
        self.bag.append(PieceFactory().get_piece("Royal", self.clan))
        for type in types:
            self.bag.append(PieceFactory().get_piece(type, self.clan))
            self.bag.append(PieceFactory().get_piece(type, self.clan))
            typeCount[type] -= 2
        random.shuffle(self.bag)
        self.hand = self.bag[0:3]
        self.recruitment = {key:value for (key, value) in typeCount.items() if key in types}

    def has_units_to_recruit(self):
        return min([value for value in self.recruitment.values()]) > 0

    def draw_units(self):
        if len(self.bag) < 3:
            self.bag = [*self.bag, *self.discard_pile]
            self.discard_pile = []
        random.shuffle(self.bag)
        self.hand = self.bag[0:3]

    def discard(self, typeToDiscard):
        self.discard_pile.append(PieceFactory().get_piece(typeToDiscard, self.clan))

    def remove_from_hand(self, typeToRemoveFromHand):
        for piece in self.hand:
            if piece.type == typeToRemoveFromHand:
                self.hand.remove(piece)
                break
    
    def place_unit(self, board: Board):
        while True:
            if self.control_tokens == 5:
                print("You cannot place a unit since you do not have any control zones")
                break

            type = input("Piece to place from hand or change move with 'change': ")

            if type == "change":
                break

            if not self.is_in_hand(type) or type == "Royal":
                print("Oops! You do not have this type of piece in your hand... remember the Royal cannot battle!")
                continue
            positionToPlace = input("Position to place (ex. b8): ")
            if not self.place(positionToPlace, type, board):
                continue
            self.remove_from_hand(type)
            break

    def place(self, positionToPlace, typeToDiscard, board: Board):
        piece = PieceFactory().get_piece(typeToDiscard, self.clan)
        if (not board.is_valid_position(positionToPlace) or 
            not board.is_orthogonal_to_control_zone(positionToPlace, self.letter)):
            print("Oops! Invalid position, it must be orthogonal to a control zone already taken")
            return False
        board.put_piece(positionToPlace, piece)
        return True

    def control_zone(self, board: Board):
        while True:

            startPosition = input("please, select the position of the unit you want it to control the zone or input 'change': ")

            if startPosition == "change":
                break

            if (not board.is_conquerable(startPosition, self.clan) or
                not board.is_my_piece(startPosition, self.clan)):
                print("Oops! You input a bad position, the position was empty or you cannot move that piece")
                continue

            type = input("Select a piece to discard for controlling: ")

            if not self.is_in_hand(type):
                print("Oops! You input a bad piece")
                continue

            self.remove_from_hand(type)
            self.discard(type)
            board.put_token(startPosition, self.letter)
            self.control_tokens -= 1
            if self.control_tokens == 0:
                board.set_winner(self.name)
            
            break

    def move_unit(self, board: Board):
        while True:
            startPosition = input("enter a position (ex. a3) or change move with 'change': ")

            if startPosition == "change":
                break

            if (not board.is_valid_position(startPosition) or
                not board.is_my_piece(startPosition, self.clan)):
                print("Oops! You input a bad position, the position was empty or you cannot move that piece")
                continue

            type = input("Select a piece of the same type in your hand: ")

            if not self.is_in_hand(type) and type == "Royal" and board.is_piece_from_same_type(self, startPosition, type):
                print("Oops! You input a bad piece type or is Royal piece")
                continue

            endPosition = input("To position (ex. a3): ") 

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
            type = input("Piece to discard from hand to recruit the same kind or change move with 'change': ")

            if type == "change":
                break

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
                    break
            else:
                self.recruit(type, type)
            break

    def recruit(self, typeToDiscard, typeToRecruit):
        self.remove_from_hand(typeToDiscard)
        self.bag.append(PieceFactory().get_piece(typeToDiscard, self.clan))
        self.recruitment[typeToRecruit] -= 1

    def can_recruit(self, type):
        if type in self.recruitment and self.recruitment[type] > 0:
            return True
        return False
    
    def is_in_hand(self, type):
        return type in [piece.type for piece in self.hand]

    def attack_unit(self, board):
        while True:
            startPosition = input("Attack from position (ex. a3) or change move with 'change': ")

            if startPosition == "change":
                break
            
            if (not board.is_valid_position(startPosition) and
                not board.is_my_piece(startPosition, self.clan)):
                print("Oops! You input a bad position, the position was empty or you cannot move that piece")
                continue
            typeToDiscard = input("Select a piece of the same type in your hand: ")
            if not self.is_in_hand(typeToDiscard) and typeToDiscard == "Royal" and board.is_piece_from_same_type(self, startPosition, typeToDiscard):
                print("Oops! You input a bad piece type or is Royal piece or the type does not concur")
                continue
            endPosition = input("To position (ex. a3): ") 
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
            print("You will use your Royal unit for taking the initiative")

            if not self.is_in_hand("Royal"):
                print("Oops! You can't take the initiative since you do not have a Royal unit")
                break

            self.remove_from_hand("Royal")
            self.initiative = True
            break

    def deactivate_initiative(self):
        self.initiative = False

    def has_initiative(self):
        return self.initiative
    
    def get_control_tokens(self):
        return self.control_tokens == 0
    
    def initiative(self, typeToDiscard):
        self.remove_from_hand(typeToDiscard)
        self.initiative = True

    def decide_actions(self, board: Board):
        self.draw_units()
        self.print_status()
        while len(self.hand) > 0 and not self.has_lost(board) and board.get_winner() is None:
            while True:
                action = input("Make an action (move/recruit/place/attack/control/initiative): ")
                action = action.lower()
                if action == "move":
                    self.move_unit(board)
                elif action == "recruit":
                    self.recruit_unit()
                elif action == "place":
                    self.place_unit(board)
                elif action == "attack":
                    self.attack_unit(board)
                elif action == "control":
                    self.control_zone(board)
                elif action == "initiative":
                    self.take_initiative()
                else:
                    print("Oops! This action does not exist!")
                    continue

                break
            self.print_hand()
        
    def has_lost(self, board: Board):
        return (len(self.bag) == 0 and
                len(self.hand) == 0 and
                not self.has_units_to_recruit() and
                not board.has_pieces_in_board(self.clan))
    
            
    def print_status(self):
        print(f"========= {self.clan} ({self.emblem}) =========")
        print(f"Hand: {str(self.hand)}")
        print(f"Recruitment pieces: {', '.join([f'{k} = {v}' for (k, v) in self.recruitment.items()])}")
        print("Discard pile:")
        print(f"{str(self.discard_pile)}")
        print(f"Control tokens: {self.control_tokens}")

    def print_hand(self):
        print(f"Hand: {str(self.hand)}")
