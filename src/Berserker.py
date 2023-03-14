import Piece

class Berserker(Piece):
    def __init__(self, color) -> None:
        super().__init__("Berserker", color)
        self.letter = "B"

    def move(self, start, end):
        if self.is_orthogonal(start, end):
            print(f"{self.color} {self.type} moves to {end}.")
            return True
        else:
            print("Invalid move, berserkers can only move one space orthogonally.")
            return False
        
    def attack(self, start, end):
        if self.is_adjacent(start, end):
            print(f"{self.color} {self.type} attacks {end}!")
            while True:
                wantToAttack = input("You may do another adjacent attack with the berserker, do you want to attack? (Y/N)")
                if wantToAttack.lower() == "y":
                    attackStartPosition = end
                    while True:
                        attackEndPosition = input("enter where you want to attack: ")
                        if not self.is_valid_position(attackEndPosition):
                            print("Invalid position, please enter a valid position.")
                            continue
                        else:
                            if self.is_adjacent(attackStartPosition, attackEndPosition):
                                return True
                            else:
                                print("Invalid attack, berserkers can only attack from adjacent positions.")
                                return False          
                if wantToAttack.lower() == "n":
                    return True
                else:
                    continue
        else:
            print("Invalid attack, berserkers can only attack from adjacent positions.")
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