import unittest
from ..state import State
from ..tools import GRID_SIZE
from ..game import Game
from ..ui import UIRender


class TestGridMethods(unittest.TestCase):

    def test_init_grid_should_render_the_correct_amount_of_rows(self):
        grid = State().init_grid()
        self.assertEqual(len(grid), GRID_SIZE)

    def test_init_grid_should_render_the_correct_amount_of_columns(self):
        grid = State().init_grid()
        self.assertEqual(len(grid[0]), GRID_SIZE)

    def test_init_grid_should_fill_a_matrix_with_dots(self):
        grid = State().init_grid()
        i = 0
        nb_places = 0
        while i < GRID_SIZE:
            nb_places += grid[i].count('.')
            i += 1
        self.assertEqual(nb_places, GRID_SIZE*GRID_SIZE)

    def test_grid_to_string_should_create_the_reference_string(self):
        grid = State().init_grid()
        grid_display = UIRender().grid_to_string(grid)
        reference_display = """    A   B   C   D
 1  .   .   .   .  
 2  .   .   .   .  
 3  .   .   .   .  
 4  .   .   .   .  
"""  # noqa
        self.assertEqual(grid_display, reference_display)

    def test_load_state_with_invalid_string_create_empty_grid(self):
        arg = []
        arg.append("""--state={"grid" : {"A2": 10,"C1":3,"D1":12},"turn" :{"player" : 1,"selected" : 7}""")
        initial_state = ""
        try:
            initial_state = Game().parse_state_from_args(arg)
        except ValueError as e:
            e.args
            # do nothing
        game_state = State()
        game_state.load_state(initial_state)
        i = 0
        nb_dots = 0
        while i < 4:
            nb_dots += game_state.grid[i].count('.')
            i += 1
        self.assertEqual(nb_dots, GRID_SIZE*GRID_SIZE)

    def test_load_state_with_valid_string_place_correct_piece_on_grid(self):
        arg = []
        arg.append("""--state={"grid" : {"A2": 10,"C1":3,"D1":12},"turn" :{"player" : 1,"selected" : 7}}""")
        initial_state = Game().parse_state_from_args(arg)
        game_state = State()
        game_state.load_state(initial_state)
        self.assertEqual(game_state.grid[1][0], 10)

    def test_load_state_with_valid_string_remove_correct_piece_from_remaining_list(self):
        arg = []
        arg.append("""--state={"grid" : {"A2": 10,"C1":3,"D1":12},"turn" :{"player" : 1,"selected" : 7}}""")
        initial_state = Game().parse_state_from_args(arg)
        game_state = State()
        game_state.load_state(initial_state)
        self.assertEqual(game_state.remaining_pieces.count(12), 0)

    def test_load_state_with_valid_string_select_correct_player(self):
        arg = []
        arg.append("""--state={"grid" : {"A2": 10,"C1":3,"D1":12},"turn" :{"player" : 2,"selected" : 7}}""")
        initial_state = Game().parse_state_from_args(arg)
        game_state = State()
        game_state.load_state(initial_state)
        self.assertEqual(game_state.game_turn.player_one_active, False)

    def test_load_state_with_valid_string_select_correct_piece_to_play(self):
        arg = []
        arg.append("""--state={"grid" : {"A2": 10,"C1":3,"D1":12},"turn" :{"player" : 2,"selected" : 7}}""")
        initial_state = Game().parse_state_from_args(arg)
        game_state = State()
        game_state.load_state(initial_state)
        self.assertEqual(game_state.game_turn.selected_piece, 7)


if __name__ == '__main__':
    unittest.main()
