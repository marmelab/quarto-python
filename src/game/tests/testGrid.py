import unittest
from ..start import init_grid, create_grid_string


class TestGridMethods(unittest.TestCase):

    def test_init_grid_should_render_the_correct_amount_of_rows(self):
        grid = init_grid(4)
        self.assertEqual(len(grid), 4)

    def test_init_grid_should_render_the_correct_amount_of_columns(self):
        grid = init_grid(4)
        self.assertEqual(len(grid[0]), 4)

    def test_init_grid_should_fill_a_matrix_with_dots(self):
        grid = init_grid(4)
        i = 0
        nb_places = 0
        while i < 4:
            nb_places += grid[i].count('.')
            i += 1
        self.assertEqual(nb_places, 16)

    def test_creat_grid_string_should_create_a_fixed_sized_string(self):
        grid = init_grid(4)
        grid_display = create_grid_string(grid)

        reference_display = """    A   B   C   D
 1  .   .   .   .  
 2  .   .   .   .  
 3  .   .   .   .  
 4  .   .   .   .  
"""  # noqa
        self.assertEqual(grid_display, reference_display)


if __name__ == '__main__':
    unittest.main()
