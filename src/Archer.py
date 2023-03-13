import Piece

class Archer(Piece):
    def __init__(self, color) -> None:
        super().__init__("archer", color)

    def move(self, start, end):
        if self.is_orthogonal(start, end):
            print(f"{self.color} {self.type} moves to {end}.")
            return True
        else:
            print("Invalid move, archers can only move one space orthogonally.")
            return False
        
    def attack(self, start, end):
        if self.separated_by_two_spaces(start, end):
            print(f"{self.color} {self.type} attacks {end}!")
            return True
        else:
            print("Invalid attack, archers can only attack from 2 spaces.")
            return False
            
    
    def is_adjacent(self, start, end):
        x1, y1 = self.get_coordinates(start)
        x2, y2 = self.get_coordinates(end)
        if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
            return True
        else:
            return False
        
    def separated_by_two_spaces(self, start, end):
        x1, y1 = self.get_coordinates(start)
        x2, y2 = self.get_coordinates(end)
        if abs(x1 - x2) + abs(y1 - y2) == 2:
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

    def get_coordinates(self, position):
        column, row = position
        x = ord(column) - 97
        y = int(row) - 1
        return x, y

    