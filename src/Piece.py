class Piece:
    def __init__(self, type, clan) -> None:
        self.type = type
        self.clan = clan
        self.captured = False
        
    def get_move(self):
        while True:
            start = input("Enter the starting position of the piece (ex. a8): ")
            end = input("Enter the ending position of the piece (ex. b8): ")
            if not self.is_valid_position(start) or not self.is_valid_position(end):
                    print("Invalid position, please enter a valid position.")
                    continue
            return start, end
        
    def can_move(self, start, end):
        raise NotImplementedError

    def can_attack(self, start, end):
        raise NotImplementedError

    def is_valid_position(self, position):
        columns = "abcde"
        rows = "12345"
        if len(position) != 2:
            return False
        column, row = position
        if column not in columns or row not in rows:
            return False
        return True
    
    def get_coordinates(self, position):
        column, row = position
        x = ord(column) - 97
        y = int(row) - 1
        return x, y
    
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
    
    def __str__(self) -> str:
        return self.letter + self.clan[0].lower()

    def __repr__(self) -> str:
        return self.type
    
    