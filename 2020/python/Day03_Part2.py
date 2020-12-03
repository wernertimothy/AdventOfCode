import numpy as np

def main():
    map = ReadPuzzleInput("PuzzleInput_Day03.txt")
    slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ]
    trees = CheckSploes(map, slopes)
    print("The answer is", np.prod(trees))

def CheckSploes(map, slopes):
    return [TreeCounter(map, slope) for slope in slopes]

def TreeCounter(map, slope):
    map_width  = len(map[0])
    map_length = len(map)
    tree       = '#'
    row        = 0
    column     = 0
    tree_count = 0
    while row < map_length-1:
        row   += slope[1]
        column = column + slope[0] if column + slope[0] < len(map[0]) else (column - map_width) + slope[0]
        if map[row][column] == tree: tree_count += 1
    return tree_count

def ReadPuzzleInput(my_file):
    with open(my_file, 'r') as f:
        return [line[:-1] for line in f]

if __name__ == "__main__":
    main()