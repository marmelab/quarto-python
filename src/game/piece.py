class Piece:
    """Definition of a game piece by 4 characteristics:
    - RoundShape [True/False]
    - BigSize [True/False]
    - LightColor [True/False]
    - TopHole [True/False]"""

    def __init__(self):
        self.round_shape = False
        self.big_size = False
        self.light_color = False
        self.top_hole = False
        self.id = 1

    @staticmethod
    def create_pieces_list():
        pieces_list = []
        i = 0
        while i < 16:
            piece = Piece()
            piece.id = i + 1
            if i in [1, 3, 5, 9, 7, 11, 13, 15]:
                piece.round_shape = True
            if i in [2, 3, 6, 10, 7, 11, 14, 15]:
                piece.big_size = True
            if i in [4, 5, 6, 12, 7, 13, 14, 15]:
                piece.light_color = True
            if i in [8, 9, 10, 12, 11, 14, 13, 15]:
                piece.top_hole = True
            pieces_list.append(piece)
            i += 1
        return pieces_list

    @staticmethod
    def check_line_winning(piece1, piece2, piece3, piece4):
            return (piece1 - 1) & (piece2 - 1) & (piece3 - 1) & (piece4 - 1) != 0
