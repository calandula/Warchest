from Archer import Archer
from Knight import Knight
from Mercenary import Mercenary
from Crossbowman import Crossbowman
from Royal import Royal

class PieceFactory:
    def get_piece(self, type, clan):
        if type == 'Archer':
            return Archer(clan)
        elif type == 'Knight':
            return Knight(clan)
        elif type == 'Crossbowman':
            return Crossbowman(clan)
        elif type == 'Mercenary':
            return Mercenary(clan)
        else:
            return Royal(clan)
