GRID_SIZE = 4
PIECES_NUMBER = 16
EMPTY_POSITION = '.'


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


def get_coordinates(position):
    """Convert a postion of format 'A3' into coordinates x= 0 and y = 2 in the grid"""
    if len(position) != 2:
        raise ValueError('Position string does not represent a valid coordinate')
    x = ord(position[0]) - 65
    y = int(position[1]) - 1
    if y < 0 or y >= GRID_SIZE or x < 0 or x >= GRID_SIZE:
        raise ValueError('Coordinate is out of the grid')

    return x, y
