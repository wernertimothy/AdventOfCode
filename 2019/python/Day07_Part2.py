# import Opcode Computer
from Day05_Part2 import Computer, read_input
# import depends
from itertools import permutations

# define new opcode procedure
def run_phase_setting(self, phase_setting, Amp_input):
    while self.m_program[ self.m_instruction_pointer ] != 99:
        if self.m_opcode == 1:
            self.m_program[ self.m_program[ self.m_instruction_pointer + 3 ] ] = self.read_parameter_one() + self.read_parameter_two()
            self.m_instruction_step = 4

        elif self.m_opcode == 2:
            self.m_program[ self.m_program[ self.m_instruction_pointer + 3 ] ] = self.read_parameter_one() * self.read_parameter_two()
            self.m_instruction_step = 4

        elif self.m_opcode == 3:
            self.m_program[ self.m_program[ self.m_instruction_pointer + 1 ] ] = phase_setting if self.count == 0 else Amp_input
            self.count += 1
            self.m_instruction_step = 2

        elif self.m_opcode == 4:
            out = self.read_parameter_one()
            self.m_instruction_step = 2
            self.m_instruction_pointer += self.m_instruction_step # see if this works
            return out

        elif self.m_opcode == 5:
            if self.read_parameter_one() != 0:
                self.m_instruction_pointer = self.read_parameter_two()
                self.m_instruction_step = 0
            else:
                self.m_instruction_step = 3

        elif self.m_opcode == 6:
            if self.read_parameter_one() == 0:
                self.m_instruction_pointer = self.read_parameter_two()
                self.m_instruction_step = 0
            else:
                self.m_instruction_step = 3

        elif self.m_opcode == 7:
            if self.read_parameter_one() < self.read_parameter_two():
                self.m_program[ self.m_program[ self.m_instruction_pointer + 3 ] ] = 1
            else:
                self.m_program[ self.m_program[ self.m_instruction_pointer + 3 ] ] = 0
            self.m_instruction_step = 4

        elif self.m_opcode == 8:
            if self.read_parameter_one() == self.read_parameter_two():
                self.m_program[ self.m_program[ self.m_instruction_pointer + 3 ] ] = 1
            else:
                self.m_program[ self.m_program[ self.m_instruction_pointer + 3 ] ] = 0
            self.m_instruction_step = 4

        else:
            raise Exception("Somthing went wrong..!")

        self.m_instruction_pointer += self.m_instruction_step
        self.assign_code()


class Amplifier:
    def __init__(
        self, 
        Controller_Software,
        ):
        # initialize Opcode Computer
        self.c       = Computer(Controller_Software)
        self.c.run   = run_phase_setting
        self.c.count = 0
    
    def run(self, phase_setting, AMP_input):
        return self.c.run(self.c, phase_setting, AMP_input)


if __name__ == "__main__":
    # read puzzle input
    ControllerSoftware = read_input("PuzzleInput_Day07.txt")

    # create phase setting permutations
    PhaseSettings = permutations([5, 6, 7, 8, 9])

    # bruteforce all phase settings
    thrusters = []
    for setting in list(PhaseSettings):

        Amp_A = Amplifier(ControllerSoftware)
        Amp_B = Amplifier(ControllerSoftware)
        Amp_C = Amplifier(ControllerSoftware)
        Amp_D = Amplifier(ControllerSoftware)
        Amp_E = Amplifier(ControllerSoftware)

        looping      = True
        last_output  = 0

        while looping:
            output = Amp_E.run(
                            setting[0],
                            Amp_D.run( 
                                setting[1],
                                Amp_C.run(
                                    setting[2],
                                    Amp_B.run(
                                        setting[3],
                                        Amp_A.run(
                                            setting[4],
                                            last_output
                                        )
                                    )
                                )
                            )
                        )
            # if (last_output - output) == 0: looping = False

            last_output = output

        thrusters += [last_output]

print("the maximum thrust is", max(thrusters))