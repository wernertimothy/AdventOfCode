from string import ascii_lowercase

def main():
    groups = ReadPuzzleInput("PuzzleInput_Day06.txt")
    counts = [CountAnswers(group) for group in groups]
    print("The sum of counts is", sum(counts))

def CountAnswers(group):
    count = 0
    for char in ascii_lowercase:
        if char in group: count += 1
    return count
        
def ReadPuzzleInput(my_file):
    # file needs two empty lines at the end for this to work
    groups = []
    with open(my_file, 'r') as f:
        answers = []
        for line in f:
            if line == '\n':
                groups.append(answers)
                answers = []
            else:
                answers.append(line.rstrip())
    return [''.join(group) for group in groups]

if __name__ == "__main__":
    main()