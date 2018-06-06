from .turn import Turn
from .tools import GRID_SIZE, PIECES_NUMBER, get_coordinates


class State:
    """Definition of all data of the game at an instant:
    - grid [2 dimension list]
    - remaining_pieces [list of numbers (from 1 to 16)]
    - game_turn [GameTurn]"""

    def __init__(self, initial_state=""):
        self.grid = self.init_grid()
        self.remaining_pieces = self.init_remaining_pieces()
        self.game_turn = Turn()
        self.message = ""

    def load_state(self, initial_state):
        try:
            for key, val in initial_state["grid"].items():
                self.place_piece(key, val)

            self.game_turn.player_one_active = initial_state["turn"]["player"] == 1
            selected_piece = initial_state["turn"]["selected"]
            if self.remaining_pieces.count(selected_piece) == 1:
                self.game_turn.selected_piece = selected_piece
            else:
                raise ValueError
        except (ValueError, TypeError):
            self.message = "[The state to load is not valid] : Ignored"
            self.grid = self.init_grid()
            self.remaining_pieces = self.init_remaining_pieces()
            self.game_turn = Turn()

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
