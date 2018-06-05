import unittest
from ..start import init_grid, creat_grid_string


class TestGridMethods(unittest.TestCase):

    def test_height_4(self):
        grid = init_grid(4)
        self.assertEqual(len(grid), 4)

    def test_width_4(self):
        grid = init_grid(4)
        self.assertEqual(len(grid[0]), 4)

    def test_grid_void(self):
        grid = init_grid(4)
        i = 0
        nb_places = 0
        while i < 4:
            nb_places += grid[i].count('.')
            i += 1
        self.assertEqual(nb_places, 16)

    def test_grid_display(self):
        grid = init_grid(4)
        grid_display = creat_grid_string(grid)
        self.assertEqual(len(grid_display), 68)

    def test_grid_display_lines(self):
        grid = init_grid(4)
        grid_display = creat_grid_string(grid)
        self.assertEqual(grid_display.count('\n'), 4)


if __name__ == '__main__':
    unittest.main()
