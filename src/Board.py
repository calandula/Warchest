from Piece import Piece

class Board:
    def __init__(self) -> None:
        self.nrows = 5
        self.ncols = 5
        self.zones = {
            (0, 2): 'Crow',
            (1, 0): '@',
            (2, 1): '@',
            (2, 3): '@',
            (3, 4): '@',
            (4, 2): 'Wolf'
        }
        self.board = [
            ['.', '.', 'C', '.', '.'],
            ['@', '.', '.', '.', '.'],
            ['.', '@', '.', '@', '.'],
            ['.', '.', '.', '.', '@'],
            ['.', '.', 'W', '.', '.']
        ]
        self.winner = None

    def print_board(self) -> str:
        rows = "abcde"
        print("  ", end="")
        print(''.join([f"  {i + 1}" for i in range(self.ncols)]) ) 
        print('    --------------')
        for i in range(self.nrows):
            print(f"{rows[i]}|", end="")
            for j in range(self.ncols):
                elem = str(self.board[i][j])
                print(f"  {elem}", end="")
            print("")

    def put_piece(self, position, piece):
        x, y = self.get_coordinates(position)
        self.board[x][y] = piece

    def put_token(self, position, clan):
        x, y = self.get_coordinates(position)
        self.zones[(x, y)] = clan
        self.board[x][y] = clan

    def move_piece(self, start, end):
        x1, y1 = self.get_coordinates(start)
        x2, y2 = self.get_coordinates(end)
        piece = self.board[x1][y1].copy()
        self.board[x1][y1] = '.'
        self.board[x2][y2] = piece

    def remove_piece(self, end):
        x1, y1 = self.get_coordinates(end)
        self.board[x1][y1] = '.'

    def is_my_piece(self, position, clan):
        x, y = self.get_coordinates(position)
        return type(self.board[x][y]) is not str and self.board[x][y].clan == clan
    
    def has_pieces_in_board(self, clan):
        for i in range(self.nrows):
            for j in range(self.ncols):
                if isinstance(self.board[i][j], Piece) and self.board[i][j].clan == clan:
                    return True
        return False

    def is_piece_from_same_type(self, position, type):
        x, y = self.get_coordinates(position)
        return type(self.board[x][y]) is not str and self.board[x][y].type == type

    def is_empty(self, position):
        x, y = self.get_coordinates(position)
        return self.board[x][y] == "."
    
    def is_conquerable(self, position, clan):
        x, y = self.get_coordinates(position)
        return (x, y) in self.zones and self.zones[(x, y)] != clan

    def can_move(self, start, end):
        x, y = self.get_coordinates(start)
        return self.board[x][y].can_move(start, end)
    
    def can_attack(self, start, end):
        x, y = self.get_coordinates(start)
        return self.board[x][y].can_attack(start, end)

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
    
    def is_orthogonal_to_control_zone(self, position, clan):
        x, y = self.get_coordinates(position)
        return (
            self.is_empty(position) and
            ((x > 0 and self.board[x - 1][y] == clan) or
            (y > 0 and self.board[x][y - 1] == clan) or
            (x < self.nrows - 1  and self.board[x + 1][y] == clan) or
            (y < self.ncols - 1 and self.board[x][y + 1] == clan))
            )
    
    def get_winner(self):
        return self.winner
    
    def set_winner(self, winner):
        self.winner = winner
    
    def has_ended(self):
        return not self.winner == None
