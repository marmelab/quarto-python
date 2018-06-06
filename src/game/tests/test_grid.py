import unittest
from ..start import GameState, grid_to_string


class TestGridMethods(unittest.TestCase):

    def test_init_grid_should_render_the_correct_amount_of_rows(self):
        grid = GameState().init_grid()
        self.assertEqual(len(grid), GameState.grid_size)

    def test_init_grid_should_render_the_correct_amount_of_columns(self):
        grid = GameState().init_grid()
        self.assertEqual(len(grid[0]), GameState.grid_size)

    def test_init_grid_should_fill_a_matrix_with_dots(self):
        grid = GameState().init_grid()
        i = 0
        nb_places = 0
        while i < 4:
            nb_places += grid[i].count('.')
            i += 1
        self.assertEqual(nb_places, 16)

    def test_grid_to_string_should_create_the_reference_string(self):
        grid = GameState().init_grid()
        grid_display = grid_to_string(grid)
        reference_display = """    A   B   C   D
 1  .   .   .   .  
 2  .   .   .   .  
 3  .   .   .   .  
 4  .   .   .   .  
"""  # noqa
        self.assertEqual(grid_display, reference_display)


if __name__ == '__main__':
    unittest.main()
