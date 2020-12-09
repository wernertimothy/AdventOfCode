
def main():
    XMAS = ReadPuzzleInput("PuzzleInput_Day09.txt")
    c = Computer(XMAS, 25)
    number = c.run()
    print("The first number that doesn't follow the rule is", number)

def ReadPuzzleInput(my_file):
    with open(my_file, 'r') as f:
        return [int(line) for line in f]

class Computer():
    def __init__(self, XMAS, preamble_length):
        self.XMAS = XMAS
        self.preamble_length = preamble_length
        self.pointer = preamble_length
        self.getPreamble()
    
    def run(self):
        while self.isSumOfTwo():
            self.pointer += 1
            self.getPreamble()
        return self.XMAS[self.pointer]

    def isSumOfTwo(self):
        for a in self.Preamble:
            for b in self.Preamble:
                if a + b == self.XMAS[self.pointer]: return True
        return False

    def getPreamble(self):
        self.Preamble = self.XMAS[self.pointer-self.preamble_length:self.pointer]

if __name__ == "__main__":
    main()