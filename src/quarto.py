def main():
    print("Welcome to Quarto-Py")
    startGame()


def startGame():
    grid = initGrid()
    displayGrid(grid)
    print("Game Started")


def initGrid(gridSize=4):
    grid = []
    i = 0
    while i < gridSize:
        grid.append([])
        j = 0
        while j < gridSize:
            grid[i].append('.')
            j += 1
        i += 1
    return grid


def displayGrid(grid):
    for line in grid:
        for position in line:
            #Separator not working, to fix
            print(position, sep=" | ", end='', flush=True)
        print('\n')


main()
