import Piece

class Crossbowman(Piece):
    def __init__(self, color) -> None:
        super().__init__("Crossbowman", color)
        self.letter = "Cr"

    def move(self, start, end):
        if self.is_orthogonal(start, end):
            print(f"{self.color} {self.type} moves to {end}.")
            return True
        else:
            print("Invalid move, crossbowmen can only move one space orthogonally.")
            return False
        
    def attack(self, start, end):
        if self.separated_by_two_spaces_straight(start, end):
            print(f"{self.color} {self.type} attacks {end}!")
            return True
        else:
            print("Invalid attack, crossbowmen can only attack from 2 spaces in a straight line.")
            return False
        
    def separated_by_two_spaces_straight(self, start, end):
        x1, y1 = self.get_coordinates(start)
        x2, y2 = self.get_coordinates(end)
        if (abs(x1 - x2) == 2 and abs(y1 - y2) == 0) or (abs(x1 - x2) == 0 and abs(y1 - y2) == 2):
            return True
        else:
            return False

    def is_orthogonal(self, start, end):
        x1, y1 = self.get_coordinates(start)
        x2, y2 = self.get_coordinates(end)
        if x1 == x2 or y1 == y2:
            return True
        else:
            return False