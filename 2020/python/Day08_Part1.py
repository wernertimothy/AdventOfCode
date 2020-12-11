
def main():
    program = ReadPuzzleInput("PuzzleInput_Day08.txt")
    c = Computer(program)
    accumulator = c.run()
    print('The accumulator value is', accumulator)

class Computer():
    def __init__(self, program):
        self.accumulator   = 0
        self.pointer       = 0
        self.program       = program
        self.pointer_count = []

    def run(self):
        while self.pointer not in self.pointer_count:
            key, value = [self.program[self.pointer][i] for i in (0,1)]
            if key == 'acc':
                self.accumulator += value
                self.pointer_update(1)
            elif key == 'jmp':
                self.pointer_update(value)
            elif key == 'nop':
                self.pointer_update(1)
        return self.accumulator
    
    def pointer_update(self, val):
        self.pointer_count.append(self.pointer)
        self.pointer += val

def ReadPuzzleInput(my_file):
    program = []
    with open(my_file, 'r') as f:
        for line in f:
            tmp = line.rstrip()
            tmp = tmp.split(' ')
            program.append([
                tmp[0],
                int(tmp[1])
            ])
        return program

if __name__ == "__main__":
    main()