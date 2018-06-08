import sys
import getopt
import json
import os
from .piece import Piece
from .turn import Turn
from .state import State
from .tools import GRID_SIZE, PIECES_NUMBER, Players
from .ui import UIRender


class Game:

    """Definition of the user interface and the interactions:"""

    def start(self):
        game_state = State()
        ui = UIRender()
        players = Players()

        ui.clear_terminal()
        players.change_player_name(1, ui.prompt_player_name(1, players.player1_name))
        players.change_player_name(2, ui.prompt_player_name(2, players.player2_name))

        initial_state = ""
        try:
            initial_state = self.parse_state_from_args(sys.argv)
        except ValueError as e:
            game_state.message = e.args[0]

        if type(initial_state) is dict:
            game_state.import_state_from_dictionary(initial_state)

        if (len(game_state.message) > 0):
            game_state.message += """\nValid sample : --state='{"grid" : {"A2": 10,"C1":3,"D1":12},"turn" :{"player" : 1,"selected" : 7}}'"""

        replay = True
        while replay:

            while not game_state.check_draw():
                if game_state.check_winner(players):
                    break
                ui.display_game(game_state, players)
                if not game_state.is_selected_piece():
                    ui.prompt_piece_selection(game_state, players)
                    game_state.switch_player()
                    ui.display_game(game_state, players)
                ui.prompt_piece_location(game_state, players)

            ui.display_game(game_state, players)
            replay = ui.prompt_restart()

            if replay:
                game_state = State()

    def parse_state_from_args(self, argv):
        if 'quarto.py' in argv[0]:
            argv.pop(0)
        parameter = ""
        try:
            opts, args = getopt.getopt(argv, "", ["state="])
            for opt, arg in opts:
                if opt == "--state":
                    parameter = json.loads(arg)
        except (getopt.GetoptError, json.decoder.JSONDecodeError, json.JSONDecodeError):
            raise ValueError("[The state to load is not wellformed] : Ignored")

        return parameter
