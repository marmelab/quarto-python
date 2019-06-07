import sys
import getopt
import json
import os
from .piece import Piece
from .turn import Turn
from .state import State
from .tools import GRID_SIZE, PIECES_NUMBER
from .players import Players
from .ui import UIRender
from .network import call_api


class Game:

    """Definition of the user interface and the interactions:"""

    def start(self):
        game_state = State()
        ui = UIRender()
        players = Players()

        ui.clear_terminal()
        players_count = ui.prompt_playing_mode()
        if players_count == 1 :
            players.change_player_name(1, ui.prompt_player_name(1, players.player1_name))
            players.change_player_name(2, "Computer")
        elif players_count == 0 :
            players.change_player_name(1, "Computer 1")
            players.change_player_name(2, "Computer 2")
        elif players_count == 2 :
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
            if players_count == 0:
                game_state.game_turn.selected_piece = 1
                while not game_state.check_draw():
                    ui.display_game(game_state, players)
                    
                    if call_api(game_state) == False:
                        game_state.message += "Error, server didn't respond : Game end"
                        break
                    game_state.switch_player()
                    if game_state.check_winner(players):
                        break
            elif players_count == 1:
                while not game_state.check_draw():
                    if game_state.check_winner(players):
                        break
                    ui.display_game(game_state, players)
                    if not game_state.is_selected_piece():
                        if not self.is_computer_turn(players_count, game_state):
                            ui.prompt_piece_selection(game_state, players)
                        game_state.switch_player()
                        ui.display_game(game_state, players)
                    elif self.is_computer_turn(players_count, game_state):
                        game_state.switch_player()
                        ui.display_game(game_state, players)
                    if self.is_computer_turn(players_count, game_state):
                        if call_api(game_state) == False:
                            game_state.message += "Error, server didn't respond : Game end"
                            break
                        if game_state.check_winner(players):
                            break
                    else:
                        ui.prompt_piece_location(game_state, players)
            elif players_count == 2:
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

    def is_computer_turn(self, players_count, game_state):
        return players_count == 0 \
            or (players_count == 1 and not game_state.game_turn.player_one_active)
