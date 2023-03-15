import Piece

class Mercenary(Piece):
    def __init__(self, color) -> None:
        super().__init__("Mercenary", color)
        self.letter = "M"

    def can_move(self, start, end):
        if self.is_orthogonal(start, end):
            print(f"{self.color} {self.type} moves to {end}.")
            return True
        else:
            print("Invalid move, mercenaries can only move one space orthogonally.")
            return False
        
    def can_attack(self, start, end):
        if self.is_adjacent(start, end):
            print(f"{self.color} {self.type} attacks {end}!")
        else:
            print("Invalid attack, mercenaries can only attack from adjacent positions.")
            return False