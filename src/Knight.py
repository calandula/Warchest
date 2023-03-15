import Piece

class Knight(Piece):
    def __init__(self, color) -> None:
        super().__init__("Knight", color)
        self.letter = "K"

    def can_move(self, start, end):
        if self.is_orthogonal(start, end):
            print(f"{self.color} {self.type} moves to {end}.")
            return True
        else:
            print("Invalid move, knights can only move one space orthogonally.")
            return False
        
    def can_attack(self, start, end):
        if self.is_adjacent(start, end):
            print(f"{self.color} {self.type} attacks {end}!")
            return True
        else:
            print("Invalid attack, knights can only attack from adjacent positions.")
            return False