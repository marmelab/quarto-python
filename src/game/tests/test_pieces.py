import unittest
from ..start import UIRender
from ..data import GameState, GameTurn, PIECES_NUMBER


class TestPiecesMethods(unittest.TestCase):

    def test_init_remaining_pieces_should_return_16_item_array(self):
        remaining_pieces = GameState().init_remaining_pieces()
        self.assertEqual(len(remaining_pieces), PIECES_NUMBER)

    def test_pieces_to_string_shouldnt_render_open_bracket(self):
        pieces_list = GameState().init_remaining_pieces()
        game_turn = GameTurn()
        pieces_display = UIRender().pieces_to_string(pieces_list, game_turn)
        self.assertEqual(pieces_display.count("["), 0)

    def test_pieces_to_string_shouldnt_render_close_bracket(self):
        pieces_list = GameState().init_remaining_pieces()
        game_turn = GameTurn()
        pieces_display = UIRender().pieces_to_string(pieces_list, game_turn)
        self.assertEqual(pieces_display.count("]"), 0)

    def test_pieces_to_string_shouldnt_render_empty_string(self):
        pieces_list = GameState().init_remaining_pieces()
        game_turn = GameTurn()
        pieces_display = UIRender().pieces_to_string(pieces_list, game_turn)
        self.assertGreater(len(pieces_display), 0)

    def test_pieces_selection_fail_when_number_not_in_remaining_list(self):
        game_state = GameState()
        game_state.remaining_pieces.remove(7)
        self.assertEqual(game_state.check_piece_availability(7), False)

    def test_pieces_selection_fail_when_number_in_remaining_list(self):
        game_state = GameState()
        game_state.remaining_pieces.remove(7)
        self.assertEqual(game_state.check_piece_availability(8), True)


if __name__ == '__main__':
    unittest.main()
