
class Computer:

    # member:
    m_instruction_pointer = 0
    m_opcode              = 0
    m_mode_one            = 0
    m_mode_two            = 0
    m_mode_three          = 0
    m_instruction_step    = 0

    # constructor:
    def __init__(self, the_program):
        self.m_program = the_program
        self.assign_code()

    # methods:
    def assign_code(self):
        code = str(self.m_program[self.m_instruction_pointer])
        self.m_opcode     = int(code[-1])
        self.m_mode_one   = int(code[-3]) if len(code) > 2 else 0
        self.m_mode_two   = int(code[-4]) if len(code) > 3 else 0
        # m_mode_three = int(code[-5]) if len(code) > 3 else 0

    def read_parameter_one(self):
        if self.m_mode_one == 0:
            return self.m_program[ self.m_program[ self.m_instruction_pointer + 1 ] ]
        else:
            return self.m_program[ self.m_instruction_pointer + 1 ]

    def read_parameter_two(self):
        if self.m_mode_two == 0:
            return self.m_program[ self.m_program[ self.m_instruction_pointer + 2 ] ]
        else:
            return self.m_program[ self.m_instruction_pointer + 2 ]

    def run(self):
        while self.m_program[ self.m_instruction_pointer ] != 99:

            if self.m_opcode == 1:
                self.m_program[ self.m_program[ self.m_instruction_pointer + 3 ] ] = self.read_parameter_one() + self.read_parameter_two()
                self.m_instruction_step = 4

            if self.m_opcode == 2:
                self.m_program[ self.m_program[ self.m_instruction_pointer + 3 ] ] = self.read_parameter_one() * self.read_parameter_two()
                self.m_instruction_step = 4

            if self.m_opcode == 3:
                self.m_program[ self.m_program[ self.m_instruction_pointer + 1 ] ] = int( input( 'please enter your input:' ) )
                self.m_instruction_step = 2

            if self.m_opcode == 4:
                print( 'output:', self.read_parameter_one() )
                self.m_instruction_step = 2

            if self.m_opcode == 5:
                if self.read_parameter_one() != 0:
                    self.m_instruction_pointer = self.read_parameter_two()
                    self.m_instruction_step = 0
                else:
                    self.m_instruction_step = 3

            if self.m_opcode == 6:
                if self.read_parameter_one() == 0:
                    self.m_instruction_pointer = self.read_parameter_two()
                    self.m_instruction_step = 0
                else:
                    self.m_instruction_step = 3

            if self.m_opcode == 7:
                if self.read_parameter_one() < self.read_parameter_two():
                    self.m_program[ self.m_program[ self.m_instruction_pointer + 3 ] ] = 1
                else:
                    self.m_program[ self.m_program[ self.m_instruction_pointer + 3 ] ] = 0
                self.m_instruction_step = 4

            if self.m_opcode == 8:
                if self.read_parameter_one() == self.read_parameter_two():
                    self.m_program[ self.m_program[ self.m_instruction_pointer + 3 ] ] = 1
                else:
                    self.m_program[ self.m_program[ self.m_instruction_pointer + 3 ] ] = 0
                self.m_instruction_step = 4

            self.m_instruction_pointer += self.m_instruction_step
            self.assign_code()


def read_input(my_file):
    PuzzleInput = open(my_file, "r")
    for line in PuzzleInput:
        line = line.split(",")
        input = [ int(code) for code in line]
    return input

def main():
    PuzzleInput = read_input("PuzzleInput_Day05.txt")
    c = Computer(PuzzleInput)
    c.run()

if __name__ == "__main__":
    main()
