import unittest
from ..state import State
from ..tools import GRID_SIZE, EMPTY_POSITION
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
            nb_places += grid[i].count(EMPTY_POSITION)
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

    def test_from_dictionary_with_invalid_string_create_empty_grid(self):
        arg = []
        arg.append("""--state={"grid" : {"A2": 10,"C1":3,"D1":12},"turn" :{"player" : 1,"selected" : 7}""")
        initial_state = ""
        try:
            initial_state = Game().parse_state_from_args(arg)
        except ValueError as e:
            e.args
            # do nothing
        game_state = State()
        game_state.from_dictionary(initial_state)
        i = 0
        nb_dots = 0
        while i < 4:
            nb_dots += game_state.grid[i].count(EMPTY_POSITION)
            i += 1
        self.assertEqual(nb_dots, GRID_SIZE*GRID_SIZE)

    def test_place_piece_with_invalid_coordinate(self):
        game_state = State()
        game_state.grid[1][1] = 7
        game_state.remaining_pieces.remove(7)
        try:
            game_state.place_piece('Zy2', 1)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

    def test_place_piece_with_occupied_coordinate(self):
        game_state = State()
        game_state.grid[1][1] = 7
        game_state.remaining_pieces.remove(7)
        try:
            game_state.place_piece('B2', 1)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

    def test_place_piece_with_valid_coordinate(self):
        game_state = State()
        game_state.grid[1][1] = 7
        game_state.remaining_pieces.remove(7)
        try:
            game_state.place_piece('A2', 1)
            self.assertTrue(True)
        except ValueError:
            self.assertTrue(False)

    def test_place_piece_with_invalid_piece(self):
        game_state = State()
        game_state.grid[1][1] = 7
        game_state.remaining_pieces.remove(7)
        try:
            game_state.place_piece('A2', 7)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

    def test_place_piece_with_valid_piece(self):
        game_state = State()
        game_state.grid[1][1] = 7
        game_state.remaining_pieces.remove(7)
        try:
            game_state.place_piece('A2', 6)
            self.assertTrue(True)
        except ValueError:
            self.assertTrue(False)

    def test_place_piece_is_placed_at_good_position(self):
        game_state = State()
        game_state.place_piece('A2', 6)
        self.assertTrue(game_state.grid[1][0] == 6)

    def test_from_dictionary_with_valid_string_place_correct_piece_on_grid(self):
        arg = []
        arg.append("""--state={"grid" : {"A2": 10,"C1":3,"D1":12},"turn" :{"player" : 1,"selected" : 7}}""")
        initial_state = Game().parse_state_from_args(arg)
        game_state = State()
        game_state.from_dictionary(initial_state)
        self.assertEqual(game_state.grid[1][0], 10)

    def test_from_dictionary_with_valid_string_remove_correct_piece_from_remaining_list(self):
        arg = []
        arg.append("""--state={"grid" : {"A2": 10,"C1":3,"D1":12},"turn" :{"player" : 1,"selected" : 7}}""")
        initial_state = Game().parse_state_from_args(arg)
        game_state = State()
        game_state.from_dictionary(initial_state)
        self.assertEqual(game_state.remaining_pieces.count(12), 0)

    def test_from_dictionary_with_valid_string_select_correct_player(self):
        arg = []
        arg.append("""--state={"grid" : {"A2": 10,"C1":3,"D1":12},"turn" :{"player" : 2,"selected" : 7}}""")
        initial_state = Game().parse_state_from_args(arg)
        game_state = State()
        game_state.from_dictionary(initial_state)
        self.assertEqual(game_state.game_turn.player_one_active, False)

    def test_from_dictionary_with_valid_string_select_correct_piece_to_play(self):
        arg = []
        arg.append("""--state={"grid" : {"A2": 10,"C1":3,"D1":12},"turn" :{"player" : 2,"selected" : 7}}""")
        initial_state = Game().parse_state_from_args(arg)
        game_state = State()
        game_state.from_dictionary(initial_state)
        self.assertEqual(game_state.game_turn.selected_piece, 7)


if __name__ == '__main__':
    unittest.main()
