import Archer, Knight, Mercenary, Crossbowman, Royal 

class PieceFactory:
    def get_piece(self, type, color):
        if type == 'Archer':
            return Archer(color)
        elif type == 'Knight':
            return Knight(color)
        elif type == 'Crossbowman':
            return Crossbowman(color)
        elif type == 'Mercenary':
            return Mercenary(color)
        else:
            return Royal(color)
