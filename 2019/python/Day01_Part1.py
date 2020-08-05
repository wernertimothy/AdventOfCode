import math

def ammount_of_fuel(mass):
    # devide by 3
    # round down
    # subtract 2
    return math.floor(mass/3) - 2

def total_fuel(my_list):
    # recursively add all up
    if my_list == []:
        return 0
    else:
        return ammount_of_fuel(my_list[0]) + total_fuel(my_list[1:])


# input data from text file
with open('PuzzleInput_Day01.txt', 'r') as f:
    lines = (line.strip() for line in f if line)
    puzzle_input = [float(line) for line in lines]


print("the total fuel is:", total_fuel(puzzle_input))