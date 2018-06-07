import sys
import getopt
import json
import os
from .piece import Piece
from .turn import Turn
from .state import State
from .tools import GRID_SIZE, PIECES_NUMBER
from .ui import UIRender


class Game:

    """Definition of the user interface and the interactions:"""

    def start(self):
        pieces_list = Piece.create_pieces_list()
        game_state = State()

        initial_state = ""
        try:
            initial_state = self.parse_state_from_args(sys.argv)
        except ValueError as e:
            game_state.message = e.args[0]

        if type(initial_state) is dict:
            game_state.from_dictionary(initial_state)

        if (len(game_state.message) > 0):
            game_state.message += """\nValid sample : --state='{"grid" : {"A2": 10,"C1":3,"D1":12},"turn" :{"player" : 1,"selected" : 7}}'"""

        ui = UIRender()
        while not game_state.check_draw():
            if game_state.check_winner():
                break
            ui.display_game(game_state)
            if not game_state.is_selected_piece():
                ui.prompt_piece_selection(game_state)
                game_state.switch_player()
                ui.display_game(game_state)
            ui.prompt_piece_location(game_state)

        ui.display_game(game_state)

    def parse_state_from_args(self, argv):
        if 'quarto.py' in argv[0]:
            argv.pop(0)

        try:
            opts, args = getopt.getopt(argv, "", ["state="])
            for opt, arg in opts:
                if opt == "--state":
                    parameter = arg
            parameter = json.loads(parameter)
        except (getopt.GetoptError, UnboundLocalError, json.decoder.JSONDecodeError, json.JSONDecodeError):
            parameter = ""
            raise ValueError("[The state to load is not wellformed] : Ignored")

        return parameter
