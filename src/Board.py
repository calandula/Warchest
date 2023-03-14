import Piece

class Board:
    def __init__(self) -> None:
        self.nrows = 5
        self.ncols = 5
        self.board = [
            ['.', '.', 'C', '.', '.'],
            ['@', '.', '.', '.', '.'],
            ['.', '@', '.', '@', '.'],
            ['.', '.', '.', '.', '@'],
            ['.', '.', 'W', '.', '.']
        ]

    def print_board(self) -> str:
        print(self.board)

    def put_piece(self, position, piece):
        x, y = self.get_coordinates(position)
        self.board[x][y] = piece.letter

    def get_coordinates(self, position):
        column, row = position
        x = ord(column) - 97
        y = int(row) - 1
        return x, y
    
    def is_valid_position(self, position):
        columns = "abcde"
        rows = "12345"
        if len(position) != 2:
            return False
        column, row = position
        if column not in columns or row not in rows:
            return False
        return True
    
    def is_orthogonal_to_control_zone(self, start, clan):
        x, y = self.get_coordinates(start)
        return (
            (x > 0 and self.board[x - 1][y] == clan) or
            (y > 0 and self.board[x][y - 1] == clan) or
            (x < self.nrows - 1  and self.board[x + 1][y] == clan) or
            (y < self.ncols - 1 and self.board[x][y + 1] == clan)
            )