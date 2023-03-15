import Piece

class Archer(Piece):
    def __init__(self, color) -> None:
        super().__init__("Archer", color)
        self.letter = "A"

    def can_move(self, start, end):
        if self.is_orthogonal(start, end):
            print(f"{self.color} {self.type} moves to {end}.")
            return True
        else:
            print("Invalid move, archers can only move one space orthogonally.")
            return False
        
    def can_attack(self, start, end):
        if self.separated_by_two_spaces(start, end):
            print(f"{self.color} {self.type} attacks {end}!")
            return True
        else:
            print("Invalid attack, archers can only attack from 2 spaces.")
            return False

    