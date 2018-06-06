import unittest
from ..start import init_remaining_pieces, pieces_to_string, init_game_turn


class TestPiecesMethods(unittest.TestCase):

    def test_init_remaining_pieces_should_return_16_item_array(self):
        remaining_pieces = init_remaining_pieces()
        self.assertEqual(len(remaining_pieces), 16)

    def test_pieces_to_string_shouldnt_render_open_bracket(self):
        pieces_list = init_remaining_pieces()
        game_turn = init_game_turn()
        pieces_display = pieces_to_string(pieces_list, game_turn)
        self.assertEqual(pieces_display.count("["), 0)

    def test_pieces_to_string_shouldnt_render_close_bracket(self):
        pieces_list = init_remaining_pieces()
        game_turn = init_game_turn()
        pieces_display = pieces_to_string(pieces_list, game_turn)
        self.assertEqual(pieces_display.count("]"), 0)

    def test_pieces_to_string_shouldnt_render_empty_string(self):
        pieces_list = init_remaining_pieces()
        game_turn = init_game_turn()
        pieces_display = pieces_to_string(pieces_list, game_turn)
        self.assertGreater(len(pieces_display), 0)


if __name__ == '__main__':
    unittest.main()
