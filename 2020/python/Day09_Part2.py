
def main():
    XMAS = ReadPuzzleInput("PuzzleInput_Day09.txt")
    c = Computer(XMAS, 1398413738)
    number = c.run()
    print("The answer is", number)

def ReadPuzzleInput(my_file):
    with open(my_file, 'r') as f:
        return [int(line) for line in f]

class Computer():
    def __init__(self, XMAS, number):
        self.XMAS = XMAS
        self.number = number
        self.pointer = 0
        self.contiguous = 2
        self.length = len(self.XMAS)
    
    def run(self):
        while self.contiguousSum() != self.number:
            if self.pointer + self.contiguous > self.length - 1:
                self.pointer = 0
                self.contiguous += 1
            else:
                self.pointer += 1
        contiguousNumbers = self.XMAS[self.pointer:self.pointer+self.contiguous]
        return min(contiguousNumbers) + max(contiguousNumbers)

    def contiguousSum(self):
        return sum(self.XMAS[self.pointer:self.pointer+self.contiguous])

if __name__ == "__main__":
    main()