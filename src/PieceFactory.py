import Archer, Berserker, Cavalry, Crossbowman, Royal 

class PieceFactory:
    def __init__(self, type, color):
        if type == 'Archer':
            return Archer(color)
        elif type == 'Berserker':
            return Berserker(color)
        elif type == 'Crossbowman':
            return Crossbowman(color)
        elif type == 'Cavalry':
            return Cavalry(color)
        else:
            return Royal(color)
