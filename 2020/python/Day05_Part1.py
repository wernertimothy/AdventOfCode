import math

def main():
    BoardingPasses = ReadPuzzleInput("PuzzleInput_Day05.txt")
    Seats = [EncodceBoardingPass(Pass) for Pass in BoardingPasses]
    IDs = [seat[0]*8+seat[1] for seat in Seats]
    print("The highest seat ID is", max(IDs))

def EncodceBoardingPass(Pass):
    return [binary_space_partitioning(Pass[0:7], 0, 127, 'F'), binary_space_partitioning(Pass[7:], 0, 7, 'L')]

def binary_space_partitioning(code, low, high, letter):
    for char in code[:-1]:
        if char == letter:
            high = math.floor(low + (high-low)/2)
        else:
            low = math.ceil(low + (high-low)/2)
    return low if code[-1] == letter else high

def ReadPuzzleInput(my_file):
    with open(my_file, 'r') as f:
        return [line for line in f]

if __name__ == "__main__":
    main()