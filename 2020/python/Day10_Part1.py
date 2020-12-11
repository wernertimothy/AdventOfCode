
def main():
    adapters = ReadPuzzleInput("PuzzleInput_Day10.txt")
    joltDiffs = connectAddapters(adapters)
    print("The answer is", joltDiffs[0]*joltDiffs[1])

def connectAddapters(adapters):
    current_adapter = 0
    one_jolt_diff   = 0
    three_jolt_diff = 0
    while adapters:
        next_adapter = min(adapters)
        jolt_diff = next_adapter - current_adapter
        if jolt_diff == 1:
            one_jolt_diff += 1
        elif jolt_diff == 3:
            three_jolt_diff += 1
        else:
            pass
        adapters.remove(next_adapter)
        current_adapter = next_adapter
    return [one_jolt_diff, three_jolt_diff + 1]

def ReadPuzzleInput(my_file):
    with open(my_file, 'r') as f:
        return [int(line) for line in f]

if __name__ == "__main__":
    main()