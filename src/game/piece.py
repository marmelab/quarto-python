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
    def create_pieces_list():
        pieces_list = []
        pieces_list.append(Piece(1, False, False, False, False))
        pieces_list.append(Piece(2, True, False, False, False))
        pieces_list.append(Piece(3, False, True, False, False))
        pieces_list.append(Piece(4, True, True, False, False))
        pieces_list.append(Piece(5, False, False, True, False))
        pieces_list.append(Piece(6, True, False, True, False))
        pieces_list.append(Piece(7, False, True, True, False))
        pieces_list.append(Piece(8, True, True, True, False))
        pieces_list.append(Piece(9, False, False, False, True))
        pieces_list.append(Piece(10, True, False, False, True))
        pieces_list.append(Piece(11, False, True, False, True))
        pieces_list.append(Piece(12, True, True, False, True))
        pieces_list.append(Piece(13, False, False, True, True))
        pieces_list.append(Piece(14, True, False, True, True))
        pieces_list.append(Piece(15, False, True, True, True))
        pieces_list.append(Piece(16, True, True, True, True))
        return pieces_list

    @staticmethod
    def check_line_winning(piece1, piece2, piece3, piece4):
        return (piece1 - 1) & (piece2 - 1) & (piece3 - 1) & (piece4 - 1) != 0 \
            or ((piece1 - 1) ^ 15) & ((piece2 - 1) ^ 15) & ((piece3 - 1) ^ 15) & ((piece4 - 1) ^ 15) != 0
