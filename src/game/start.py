import sys
import getopt
import json
from .data import Piece, GameTurn, GameState


def start_game():
    print("Welcome to Quarto-Py")

    parameter, error_message = get_state_parameter(sys.argv)
    pieces_list = Piece.create_pieces_list()

    game_state = GameState(parameter)
    if len(game_state.message) > 0:
        error_message = game_state.message

    if len(error_message) > 0:
        print(error_message)
        print("""Valid sample : --state='{"grid" : {"A2": 10,"C1":3,"D1":12},"turn" :{"player" : 1,"selected" : 7}}'""")

    display_game(game_state)


def get_state_parameter(argv):
    error_message = ""
    if 'quarto.py' in argv[0]:
        argv.pop(0)

    try:
        opts, args = getopt.getopt(argv, "s:", ["state="])
    except getopt.GetoptError:
        parameter = ""
    for opt, arg in opts:
        if opt == "--state":
            parameter = arg
    try:
        parameter = json.loads(parameter)
    except:
        parameter = ""
        error_message = "[The state to load is not wellformed] : Ignored"

    return parameter, error_message


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


def display_game(game_state):
    print()
    print(grid_to_string(game_state.grid))
    print()
    print(players_to_string(game_state.game_turn))
    print()
    print(pieces_to_string(game_state.remaining_pieces, game_state.game_turn))
    