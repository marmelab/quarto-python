class Turn:
    """Definition of a turn of game:
    - player_one_active [True/False] It is False when it's player 2 turn
    - selected_piece [between 0 to 16] It has 0 when no piece is selected yet"""

    def __init__(self):
        self.player_one_active = True
        self.selected_piece = 0
