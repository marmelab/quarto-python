from .data import Piece


def start_game():
    grid = init_grid()
    display_grid(grid)
    print("Welcome to Quarto-Py")


def init_grid(grid_size=4):
    grid = []
    i = 0
    while i < grid_size:
        grid.append([])
        j = 0
        while j < grid_size:
            grid[i].append('.')
            j += 1
        i += 1
    return grid


def creat_grid_string(grid):
    display_string = ''
    for line in grid:
        for position in line:
            if len(position) < 2:
                display_string += ' '
            display_string += position
            display_string += '  '
        display_string += '\n'
    return display_string


def display_grid(grid):
    print(creat_grid_string(grid))
