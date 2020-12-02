
def main():
    expense_report = ReadPuzzleInput("PuzzleInput_Day01.txt")
    ints = BruteForce(expense_report)
    print("the answer is:", ints[0], "*", ints[1], "*", ints[2], "=", ints[0]*ints[1]*ints[2])

def ReadPuzzleInput(my_file):
    with open(my_file, 'r') as f:
        return [int(line) for line in f]

def BruteForce(array):
    for a in array:
        for b in array:
            for c in array:
                if (a + b + c == 2020):
                    return [a,b,c]

if __name__ == "__main__":
    main()