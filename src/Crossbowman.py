from Piece import Piece

class Crossbowman(Piece):
    def __init__(self, color) -> None:
        super().__init__("Crossbowman", color)
        self.letter = "Cr"

    def can_move(self, start, end):
        if self.is_orthogonal(start, end):
            print(f"{self.color} {self.type} moves to {end}.")
            return True
        else:
            print("Invalid move, crossbowmen can only move one space orthogonally.")
            return False
        
    def can_attack(self, start, end):
        if self.separated_by_two_spaces_straight(start, end):
            print(f"{self.color} {self.type} attacks {end}!")
            return True
        else:
            print("Invalid attack, crossbowmen can only attack from 2 spaces in a straight line.")
            return False