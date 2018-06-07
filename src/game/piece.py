from .tools import EMPTY_POSITION


class Piece:
    """Definition of a game piece by 4 characteristics:
    - RoundShape [True/False]
    - BigSize [True/False]
    - LightColor [True/False]
    - TopHole [True/False]"""

    def __init__(self, id=1, round_shape=False, big_size=False, light_color=False, top_hole=False):
        self.round_shape = round_shape
        self.big_size = big_size
        self.light_color = light_color
        self.top_hole = top_hole
        self.id = id

    def to_string(self):
        return(1, ' : ', self.round_shape, ' - ', self.big_size, ' - ', self.light_color, ' - ', self.top_hole)

    @staticmethod
    def check_line_winning(piece1, piece2, piece3, piece4):
        if EMPTY_POSITION not in (piece1, piece2, piece3, piece4):
            return (piece1 - 1) & (piece2 - 1) & (piece3 - 1) & (piece4 - 1) != 0 \
                or ((piece1 - 1) ^ 15) & ((piece2 - 1) ^ 15) & ((piece3 - 1) ^ 15) & ((piece4 - 1) ^ 15) != 0
        return False


pieces_list_definition = [
        Piece(1, False, False, False, False),
        Piece(2, True, False, False, False),
        Piece(3, False, True, False, False),
        Piece(4, True, True, False, False),
        Piece(5, False, False, True, False),
        Piece(6, True, False, True, False),
        Piece(7, False, True, True, False),
        Piece(8, True, True, True, False),
        Piece(9, False, False, False, True),
        Piece(10, True, False, False, True),
        Piece(11, False, True, False, True),
        Piece(12, True, True, False, True),
        Piece(13, False, False, True, True),
        Piece(14, True, False, True, True),
        Piece(15, False, True, True, True),
        Piece(16, True, True, True, True)
    ]
