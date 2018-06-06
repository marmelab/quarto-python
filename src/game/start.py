from .data import Piece, GameTurn


def start_game():
    print("Welcome to Quarto-Py")

    pieces_list = Piece.create_pieces_list()

    grid = init_grid()
    remaining_pieces = init_remaining_pieces()
    game_turn = init_game_turn()

    display_game(grid, remaining_pieces, game_turn)


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


def init_remaining_pieces(pieces_number=16):
    list_pieces = []
    i = 0
    while i < pieces_number:
        i += 1
        list_pieces.append(i)
    return list_pieces


def init_game_turn():
    game_turn = GameTurn()
    return game_turn


def grid_to_string(grid):
    display_string = '    A   B   C   D\n'
    i = 1
    for line in grid:
        display_string += ' '
        display_string += str(i)
        display_string += ' '
        for position in line:
            position = str(position)
            if len(position) < 2:
                display_string += ' '
            display_string += position
            display_string += '  '
        display_string += '\n'
        i += 1
    return display_string


def pieces_to_string(remaining_pieces, game_turn):
    display_string = 'Remaining pieces :\n'
    i = 1
    for piece in remaining_pieces:
        display_string += ' '
        display_string += selected_piece_to_string(piece, game_turn)
        display_string += ' '
    return display_string


def selected_piece_to_string(piece_number, game_turn):
    if game_turn.selected_piece == piece_number:
        return "[" + str(piece_number) + "]"
    return str(piece_number)


def players_to_string(game_turn):
    player_1 = selected_player_to_string('Player 1', game_turn.player_one_active)
    player_2 = selected_player_to_string('Player 2', not game_turn.player_one_active)
    return player_1 + "     " + player_2


def selected_player_to_string(player_name, selected):
    if selected:
        player_name = "=> " + player_name + " <="
    return player_name


def display_game(grid, remaining_pieces, game_turn):
    print()
    print(grid_to_string(grid))
    print()
    print(players_to_string(game_turn))
    print()
    print(pieces_to_string(remaining_pieces, game_turn))
