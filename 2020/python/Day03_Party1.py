
def main():
    map = ReadPuzzleInput("PuzzleInput_Day03.txt")
    slope = [3, 1]
    trees = TreeCounter(map, slope)
    print("The number of trees is", trees)

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