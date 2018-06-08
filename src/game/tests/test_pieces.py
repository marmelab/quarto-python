import unittest
from ..state import State
from ..turn import Turn
from ..tools import PIECES_NUMBER
from ..ui import UIRender
from ..piece import Piece


class TestPiecesMethods(unittest.TestCase):

    def test_init_remaining_pieces_should_return_16_item_array(self):
        remaining_pieces = State().init_remaining_pieces()
        self.assertEqual(len(remaining_pieces), PIECES_NUMBER)

    def test_pieces_to_string_shouldnt_render_open_bracket(self):
        pieces_list = State().init_remaining_pieces()
        game_turn = Turn()
        pieces_display = UIRender().pieces_to_string(pieces_list, game_turn)
        self.assertEqual(pieces_display.count(" ["), 0)

    def test_pieces_to_string_shouldnt_render_close_bracket(self):
        pieces_list = State().init_remaining_pieces()
        game_turn = Turn()
        pieces_display = UIRender().pieces_to_string(pieces_list, game_turn)
        self.assertEqual(pieces_display.count("] "), 0)

    def test_pieces_to_string_shouldnt_render_empty_string(self):
        pieces_list = State().init_remaining_pieces()
        game_turn = Turn()
        pieces_display = UIRender().pieces_to_string(pieces_list, game_turn)
        self.assertGreater(len(pieces_display), 0)

    def test_pieces_selection_fail_when_number_not_in_remaining_list(self):
        game_state = State()
        game_state.remaining_pieces.remove(7)
        self.assertEqual(game_state.check_piece_availability(7), False)

    def test_pieces_selection_fail_when_number_in_remaining_list(self):
        game_state = State()
        game_state.remaining_pieces.remove(7)
        self.assertEqual(game_state.check_piece_availability(8), True)

    def test_pieces_winning_by_round_shape(self):
        self.assertEqual(Piece.check_line_winning(4, 6, 10, 8), True)

    def test_pieces_winning_by_square_shape(self):
        self.assertEqual(Piece.check_line_winning(3, 5, 7, 11), True)

    def test_pieces_winning_by_big_size(self):
        self.assertEqual(Piece.check_line_winning(8, 12, 15, 16), True)

    def test_pieces_winning_by_small_size(self):
        self.assertEqual(Piece.check_line_winning(6, 9, 10, 13), True)

    def test_pieces_winning_by_light_color(self):
        self.assertEqual(Piece.check_line_winning(5, 6, 7, 13), True)

    def test_pieces_winning_by_dark_color(self):
        self.assertEqual(Piece.check_line_winning(1, 2, 3, 4), True)

    def test_pieces_winning_by_top_hole(self):
            self.assertEqual(Piece.check_line_winning(9, 10, 11, 12), True)

    def test_pieces_winning_by_top_flat(self):
        self.assertEqual(Piece.check_line_winning(5, 6, 7, 8), True)

    def test_pieces_no_winning(self):
        self.assertEqual(Piece.check_line_winning(8, 14, 15, 16), True)

    def test_is_selected_piece(self):
        game_state = State()
        game_state.game_turn.selected_piece = 3
        self.assertEqual(game_state.is_selected_piece(), True)

    def test_is_not_selected_piece(self):
        game_state = State()
        self.assertEqual(game_state.is_selected_piece(), False)


if __name__ == '__main__':
    unittest.main()
