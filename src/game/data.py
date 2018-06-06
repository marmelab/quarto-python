GRID_SIZE = 4
PIECES_NUMBER = 16


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


class GameTurn:
    """Definition of a turn of game:
    - player_one_active [True/False] It is False when it's player 2 turn
    - selected_piece [between 0 to 16] It has 0 when no piece is selected yet"""

    def __init__(self):
        self.player_one_active = True
        self.selected_piece = 0


class GameState:
    """Definition of all data of the game at an instant:
    - grid [2 dimension list]
    - remaining_pieces [list of numbers (from 1 to 16)]
    - game_turn [GameTurn]"""

    def __init__(self, initial_state=""):
        self.grid = self.init_grid()
        self.remaining_pieces = self.init_remaining_pieces()
        self.game_turn = GameTurn()
        self.message = ""

    def load_state(self, initial_state):
        try:
            for key, val in initial_state["grid"].items():
                self.place_piece(key, val)

            self.game_turn.player_one_active = initial_state["turn"]["player"] == 1
            self.game_turn.selected_piece = initial_state["turn"]["selected"]
        except (ValueError, TypeError) as e:
            self.message = "[The state to load is not valid] : Ignored"
            self.grid = self.init_grid()
            self.remaining_pieces = self.init_remaining_pieces()
            self.game_turn = GameTurn()

    def place_piece(self, position, piece_id):
        x, y = get_coordinates(position)

        if self.remaining_pieces.count(piece_id) == 1:
            self.grid[y][x] = piece_id
            self.remaining_pieces.remove(piece_id)
        else:
            raise ValueError('Unvalid piece id')

    def init_grid(self):
        return [['.' for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]

    def init_remaining_pieces(self):
        return [i + 1 for i in range(PIECES_NUMBER)]

    def check_piece_availability(self, piece):
        return self.remaining_pieces.count(piece) == 1

    def swich_player(self):
        self.game_turn.player_one_active = not self.game_turn.player_one_active


def get_coordinates(position):
    """Convert a postion of format 'A3' into coodinates x= 0 and y = 2 in the grid"""
    x = 0
    y = 0
    if len(position) != 2:
        raise ValueError('Position string does not represent a valid coordinate')

    x = ord(position[0]) - 65
    y = int(position[1]) - 1
    if y < 0 or y >= GRID_SIZE or x < 0 or x >= GRID_SIZE:
        raise ValueError('Coordinate is out of the grid')

    return x, y
