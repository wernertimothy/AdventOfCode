
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
        self.pointer_count = {}

    def run(self):
        updated = []
        while self.pointer not in updated:
            key, value = [self.program[self.pointer][i] for i in (0,1)]
            if key == 'acc':
                self.accumulator += value
                self.pointer += 1
            elif key == 'jmp':
                updated.append(self.pointer)
                self.pointer_update(value)
            elif key == 'nop':
                self.pointer += 1
        return self.accumulator
    
    def pointer_update(self, val):
        if self.pointer in self.pointer_count:
            self.pointer_count[self.pointer] += 1
        else:
            self.pointer_count[self.pointer] = 1
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