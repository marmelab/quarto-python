import sys
import subprocess
import getopt
import json
import os
from .piece import pieces_list_definition
from .turn import Turn
from .state import State
from .tools import GRID_SIZE, PIECES_NUMBER, Players


class UIRender:

    """Definition of the user interface and the interactions:"""

    def prompt_piece_selection(self, game_state):
        while True:
            try:
                piece = int(input("Choose the next piece of the opponent : "))
                if game_state.select_piece_for_opponent(piece):
                    return
                game_state.message = "You must choose a number available in the list"
            except ValueError:
                game_state.message = "You have to type number between 1 and " + str(PIECES_NUMBER)
                self.display_game(game_state)
            except KeyboardInterrupt:
                print("\nGame aborted")
                exit()

    def prompt_piece_location(self, game_state):
        while True:
            try:
                position = input("Choose the position to place your piece : ")
                game_state.place_piece(position, game_state.game_turn.selected_piece)
                return
            except ValueError:
                game_state.message = "You have to type a free coordinate using  this format : 'A1'"
                self.display_game(game_state)
            except KeyboardInterrupt:
                print("\nGame aborted")
                exit()

    def prompt_player_name(self, player_id, default_name):
        try:
            name = input("Player " + str(player_id) + ", what is your name (" + default_name + " if empty) ? ")
            if len(name) > 0:
                return name
            return default_name
        except KeyboardInterrupt:
            print("\nGame aborted")
            exit()

    def prompt_restart(self):
        try:
            return input("Let's play another party ? (o/n) ") == 'o'
        except KeyboardInterrupt:
            print("\nGame aborted")
            exit()

    def piece_to_string(self, piece_id):
        piece_display = str(piece_id)
        pieces = list(filter(lambda x: x.id == piece_id, pieces_list_definition))
        if len(pieces) == 1:
            if pieces[0].round_shape:
                if pieces[0].top_hole:
                    piece_display = "○"
                else:
                    piece_display = "●"
            else:
                if pieces[0].top_hole:
                    piece_display = "□"
                else:
                    piece_display = "■"

            if pieces[0].big_size:
                piece_display = "\033[32m" + piece_display
            else:
                piece_display = "\033[91m" + piece_display

            if pieces[0].light_color:
                piece_display = "\033[47m" + piece_display

        return ' ' + piece_display + " \033[0m"

    def grid_to_string(self, grid):
        display_string = '    A    B    C    D\n'
        for i, row in enumerate(grid, start=1):
            display_string += ' '
            display_string += str(i)
            display_string += ' '
            for position in row:
                display_string += self.piece_to_string(position)
                display_string += '  '
            display_string += '\n'
        return display_string

    def pieces_to_string(self, remaining_pieces, game_turn):
        display_string = 'Remaining pieces :\n'
        for piece_id in range(1, PIECES_NUMBER + 1):
            display_string += ' '
            if remaining_pieces.count(piece_id):
                display_string += self.piece_to_string(piece_id) + ' '
                if piece_id >= 10:
                    display_string += ' '
            else:
                if piece_id >= 10:
                    display_string += ' '
                display_string += ' .  '
        display_string += '\n'

        for piece_id in range(1, PIECES_NUMBER + 1):
            display_string += ' '
            if remaining_pieces.count(piece_id):
                display_string += self.selected_piece_to_string(piece_id, game_turn)
            else:
                if piece_id >= 10:
                    display_string += ' '
                display_string += '   '
            display_string += ' '
        return display_string

    def selected_piece_to_string(self, piece_number, game_turn):
        if game_turn.selected_piece == piece_number:
            return "[" + str(piece_number) + "]"
        return " " + str(piece_number) + " "

    def players_to_string(self, game_turn):
        player_1 = self.selected_player_to_string(Players.player1_name, game_turn.player_one_active)
        player_2 = self.selected_player_to_string(Players.player2_name, not game_turn.player_one_active)
        return player_1 + "     " + player_2

    def selected_player_to_string(self, player_name, selected):
        if selected:
            return "=> " + player_name + " <="
        return "   " + player_name + "   "

    def clear_terminal(self):
        subprocess.call(["printf", "'\033c'"])

    def display_game(self, game_state):
        self.clear_terminal()
        print()
        print("\033[32;1mWelcome to Quarto-Py\033[0m")
        print()
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
