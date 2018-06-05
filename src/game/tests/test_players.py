import unittest
from ..start import players_to_string, init_game_turn


class TestPlayersMethods(unittest.TestCase):

    def test_init_game_turn_should_start_with_player_1(self):
        game_turn = init_game_turn()
        self.assertEqual(game_turn.player_one_active, True)

    def test_init_game_turn_should_start_without_selected_piece(self):
        game_turn = init_game_turn()
        self.assertEqual(game_turn.selected_piece, 0)

    def test_players_to_string_should_create_a_fixed_string(self):
        game_turn = init_game_turn()
        players_display = players_to_string(game_turn)
        reference_string = "=> Player 1 <=     Player 2"
        self.assertEqual(players_display, reference_string)


if __name__ == '__main__':
    unittest.main()
