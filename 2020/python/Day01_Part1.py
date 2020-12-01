
def main():
    expense_report = ReadPuzzleInput("Day01.txt")
    ints = BruteForce(expense_report)
    print("the answer is:", ints[0]*ints[1])

def ReadPuzzleInput(my_file):
    with open(my_file, 'r') as f:
        return [int(line) for line in f]

def BruteForce(array):
    for a in array:
        for b in array:
            if (a + b == 2020):
                return [a,b]

if __name__ == "__main__":
    main()