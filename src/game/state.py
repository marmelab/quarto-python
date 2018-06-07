from .turn import Turn
from .tools import GRID_SIZE, PIECES_NUMBER, EMPTY_POSITION, get_coordinates


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

    def from_dictionary(self, initial_state_dictionary):
        try:
            for key, val in initial_state_dictionary["grid"].items():
                self.place_piece(key, val)

            self.game_turn.player_one_active = initial_state_dictionary["turn"]["player"] == 1
            selected_piece = initial_state_dictionary["turn"]["selected"]
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
            if not self.check_position_availability(x, y):
                raise ValueError('This position is already occupied on the grid')
            self.grid[y][x] = piece_id
            self.remaining_pieces.remove(piece_id)
        else:
            raise ValueError('Unvalid piece id')

    def init_grid(self):
        return [[EMPTY_POSITION for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]

    def init_remaining_pieces(self):
        return [i + 1 for i in range(PIECES_NUMBER)]

    def check_piece_availability(self, piece_id):
        return self.remaining_pieces.count(piece_id) == 1

    def select_piece_for_opponent(self, piece_id):
        if not self.check_piece_availability(piece_id):
            return False
        self.game_turn.selected_piece = piece_id
        return True

    def check_position_availability(self, x, y):
        return self.grid[y][x] == EMPTY_POSITION

    def switch_player(self):
        self.game_turn.player_one_active = not self.game_turn.player_one_active
