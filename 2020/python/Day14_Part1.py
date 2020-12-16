import numpy as np

def main():
    program = ReadPuzzleInput("PuzzleInput_Day14.txt")
    c = Computer(program)
    answer = c.run()
    print('The sum of the vlaues left in memory is', answer)

class Computer:
    def __init__(self, program):
        self.program = program
        self.bitmask = self.program[0][1]
        # Thow big is 36 bit space?
        self.memory = np.zeros(300000)
    def run(self):
        for instruction in self.program[1:]:
            if instruction[0] == 'mask':
                self.bitmask = instruction[1]
            else:
                self.writeToMemory(instruction)
        return int(np.sum(self.memory))

    def writeToMemory(self, instruction):
        dec = '{0:036b}'.format(instruction[1])
        for k, char in enumerate(self.bitmask):
            if char == 'X': continue
            else: dec = dec[:k]+ char + dec[k+1:]
        num = int(dec, 2)
        self.memory[instruction[0]] = num

def ReadPuzzleInput(my_file):
    program = []
    with open(my_file, 'r') as f:
        lines = [line.strip().split("=") for line in f]
        for line in lines:
            if line[0] == 'mask ':
                program.append(['mask', line[1].strip()])
            else:
                program.append([int(line[0].strip('mem[ ] ')), int(line[1])])
    return program

if __name__ == "__main__":
    main()