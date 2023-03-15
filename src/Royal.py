from Piece import Piece

class Royal(Piece):
    def __init__(self, color) -> None:
        super().__init__("Royal", color)