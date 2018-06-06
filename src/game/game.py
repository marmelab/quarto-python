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
        try :
            initial_state = self.parse_state_from_args(sys.argv)
        except ValueError as e:
            game_state.message = e.args[0]     

        if type(initial_state) is dict:
            game_state.load_state(initial_state)

        if (len(game_state.message) > 0):
            game_state.message += """\nValid sample : --state='{"grid" : {"A2": 10,"C1":3,"D1":12},"turn" :{"player" : 1,"selected" : 7}}'"""

        ui = UIRender()
        while len(game_state.remaining_pieces) > 0:
            ui.display_game(game_state)
            ui.prompt_piece_selection(game_state)
            game_state.swich_player()
            ui.display_game(game_state)
            ui.prompt_piece_location(game_state)

    def parse_state_from_args(self, argv):
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
            raise ValueError("[The state to load is not wellformed] : Ignored")

        return parameter
