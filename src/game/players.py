class Players:

    """Definition of the users names:"""

    def __init__(self, initial_state=""):
        self.player1_name = "Player 1"
        self.player2_name = "Player 2"

    def change_player_name(self, player_id, player_name):
        if player_id == 1:
            self.player1_name = player_name
        if player_id == 2:
            self.player2_name = player_name
