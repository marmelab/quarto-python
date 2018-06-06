GRID_SIZE = 4
PIECES_NUMBER = 16


def get_coordinates(position):
    """Convert a postion of format 'A3' into coordinates x= 0 and y = 2 in the grid"""
    x = 0
    y = 0
    if len(position) != 2:
        raise ValueError('Position string does not represent a valid coordinate')

    x = ord(position[0]) - 65
    y = int(position[1]) - 1
    if y < 0 or y >= GRID_SIZE or x < 0 or x >= GRID_SIZE:
        raise ValueError('Coordinate is out of the grid')

    return x, y
