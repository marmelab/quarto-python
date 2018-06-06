class Piece:
    """Definition of a game piece by 4 characteristics:
    - RoundShape
    - BigSize
    - LightColor
    - TopHole"""

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
    - player_one_active is False when it's player 2 turn
    - selected_piece has 0 when no pice is selected yet"""

    def __init__(self):
        self.player_one_active = True
        self.selected_piece = 0


class GameState:
    """Definition of all data of the game at an instant:
    - grid
    - remaining_pieces
    - game_turn"""

    def __init__(self, parameter=""):
        self.grid = GameState.init_grid()
        self.remaining_pieces = GameState.init_remaining_pieces()
        self.game_turn = GameState.init_game_turn()
        self.message = ""
        if type(parameter) is dict:
            self.load_state(parameter)

    def load_state(self, parameter):
        try:
            for key, val in parameter["grid"].items():
                self.place_piece(key, val)

            self.game_turn.player_one_active = parameter["turn"]["player"] == 1
            self.game_turn.selected_piece = parameter["turn"]["selected"]
        except:
            self.message = "[The state to load is not valid] : Ignored"
            self.grid = GameState.init_grid()
            self.remaining_pieces = GameState.init_remaining_pieces()
            self.game_turn = GameState.init_game_turn()

    def place_piece(self, position, piece_id):
        x, y = get_coordinates(position)
        if self.remaining_pieces.count(piece_id) == 1:
            self.grid[y][x] = piece_id
            self.remaining_pieces.remove(piece_id)
        else:
            raise ValueError('Unvalid piece id')

    @staticmethod
    def init_grid(grid_size=4):
        grid = []
        i = 0
        while i < grid_size:
            grid.append([])
            j = 0
            while j < grid_size:
                grid[i].append('.')
                j += 1
            i += 1
        return grid

    @staticmethod
    def init_remaining_pieces(pieces_number=16):
        list_pieces = []
        i = 0
        while i < pieces_number:
            i += 1
            list_pieces.append(i)
        return list_pieces

    @staticmethod
    def init_game_turn():
        game_turn = GameTurn()
        return game_turn


def get_coordinates(position):
    x = 0
    y = 0
    if len(position) == 2:
        x = ord(position[0]) - 65
        y = int(position[1]) - 1
        if y < 0 or y > 3 or x < 0 or x > 3:
            raise ValueError('Unvalid coordinate')
    else:
        raise ValueError('Unvalid coordinate')
    return x, y
