import Piece

class Cavalry(Piece):
    def __init__(self, color) -> None:
        super().__init__("cavalry", color)

    def move(self, start, end):
        if self.is_orthogonal(start, end):
            print(f"{self.color} {self.type} moves to {end}.")
            while True:
                wantToAttack = input("You may attack adjacent pieces with the cavalry, do you want to attack? (Y/N)")
                if wantToAttack.lower() == "y":
                    attackStartPosition = end
                    while True:
                        attackEndPosition = input("enter where you want to attack: ")
                        if not self.is_valid_position(attackEndPosition):
                            print("Invalid position, please enter a valid position.")
                            continue
                        else:
                            self.attack(attackStartPosition, attackEndPosition)
                            return True
                if wantToAttack.lower() == "n":
                    return True
                else:
                    continue
        else:
            print("Invalid move, cavalry can only move one space orthogonally.")
            return False
        
    def attack(self, start, end):
        if self.is_adjacent(start, end):
            print(f"{self.color} {self.type} attacks {end}!")
            return True
        else:
            print("Invalid attack, cavalry can only attack from adjacent positions.")
            return False
            
    
    def is_adjacent(self, start, end):
        x1, y1 = self.get_coordinates(start)
        x2, y2 = self.get_coordinates(end)
        if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
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