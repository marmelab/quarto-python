import sys
import getopt
import json
import os
from .data import Piece, GameTurn, GameState, PIECES_NUMBER


class UIRender:

    """Definition of the user interface and the interactions:"""

    def start_game(self):
        print("Welcome to Quarto-Py")

        initial_state, error_parsing = self.get_state_parameter(sys.argv)
        pieces_list = Piece.create_pieces_list()

        game_state = GameState()

        if len(error_parsing) > 0:
            game_state.message = error_parsing
        elif type(initial_state) is dict:
            game_state.load_state(initial_state)

        if (len(game_state.message) > 0):
            game_state.message += """\nValid sample : --state='{"grid" : {"A2": 10,"C1":3,"D1":12},"turn" :{"player" : 1,"selected" : 7}}'"""

        while len(game_state.remaining_pieces) > 0:
            self.display_game(game_state)
            self.prompt_piece_selection(game_state)
            game_state.swich_player()
            self.display_game(game_state)
            self.prompt_piece_location(game_state)

    def prompt_piece_selection(self, game_state):
        while True:
            try:
                piece = int(input("Choose the next piece of the opponent : "))
                valid_piece = game_state.check_piece_availability(piece)
                if valid_piece:
                    break
                game_state.message = "You must choose a number available in the list"
                self.display_game(game_state)

            except ValueError:
                game_state.message = "You have to type number between 1 and " + str(PIECES_NUMBER)
                self.display_game(game_state)
            except KeyboardInterrupt:
                print("\nGame aborted")
                exit()
        game_state.game_turn.selected_piece = piece

    def prompt_piece_location(self, game_state):
        position = input("Choose the position to place your piece : ")
        # basic remove of the piece to end correctly the "while", but will be replace by real placement for next story
        game_state.remaining_pieces.remove(game_state.game_turn.selected_piece)

    def get_state_parameter(self, argv):
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
        except json.JSONDecodeError:
            parameter = ""
            error_message = "[The state to load is not wellformed] : Ignored"

        return parameter, error_message

    def grid_to_string(self, grid):
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

    def pieces_to_string(self, remaining_pieces, game_turn):
        display_string = 'Remaining pieces :\n'
        for i in range(1, PIECES_NUMBER + 1):
            display_string += ' '
            if remaining_pieces.count(i):
                display_string += self.selected_piece_to_string(i, game_turn)
            else:
                display_string += ' . '
            display_string += ' '
        return display_string

    def selected_piece_to_string(self, piece_number, game_turn):
        if game_turn.selected_piece == piece_number:
            return "[" + str(piece_number) + "]"
        return str(piece_number)

    def players_to_string(self, game_turn):
        player_1 = self.selected_player_to_string('Player 1', game_turn.player_one_active)
        player_2 = self.selected_player_to_string('Player 2', not game_turn.player_one_active)
        return player_1 + "     " + player_2

    def selected_player_to_string(self, player_name, selected):
        if selected:
            player_name = "=> " + player_name + " <="
        return player_name

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_game(self, game_state):
        self.clear_terminal()
        print()
        print(self.grid_to_string(game_state.grid))
        print()
        print(self.players_to_string(game_state.game_turn))
        print()
        print(self.pieces_to_string(game_state.remaining_pieces, game_state.game_turn))
        print()
        if len(game_state.message) > 0:
            print(game_state.message)
            game_state.message = ""
