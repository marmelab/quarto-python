class Piece:
    """Definition of a game piece by 4 characteristics:
    - RoundShape [True/False]
    - BigSize [True/False]
    - LightColor [True/False]
    - TopHole [True/False]"""

    def __init__(self):
        self.round_shape = True
        self.big_size = True
        self.light_color = True
        self.top_hole = True
        self.id = 1

    @staticmethod
    def create_pieces_list():
        pieces_list = []
        i = 1
        while i <= 16:
            piece = Piece()
            piece.id = i
            if i in [1, 2, 3, 4, 5, 6, 7, 8]:
                piece.round_shape = False
            if i in [1, 2, 3, 4, 11, 12, 13, 14]:
                piece.big_size = False
            if i in [1, 2, 5, 6, 9, 10, 13, 14]:
                piece.light_color = False
            if i in [1, 3, 5, 7, 9, 11, 13, 15, 17]:
                piece.top_hole = False
            pieces_list.append(piece)
            i += 1
        return pieces_list
