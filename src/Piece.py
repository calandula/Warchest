class Piece:
    def __init__(self, type, color) -> None:
        self.type = type
        self.color = color
        self.captured = False
        
    def get_move(self):
        while True:
            start = input("Enter the starting position of the piece (ex. a8): ")
            end = input("Enter the ending position of the piece (ex. b8): ")
            if not self.is_valid_position(start) or not self.is_valid_position(end):
                    print("Invalid position, please enter a valid position.")
                    continue
            return start, end
        
    def move(self, start, end):
        pass

    def attack(self, start, end):
        pass

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
    
    