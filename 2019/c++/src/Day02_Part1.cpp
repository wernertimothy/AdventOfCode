
#include <fstream>
#include <string>
#include <sstream>
#include <iostream>

#include "Day_02.hpp"

using namespace day_02;

Computer::Computer(const std::vector<int>& the_program) : m_program(the_program)
{
    m_instruction_pointer = 0;
    assign_code();
}

void Computer::print() const
{
    std::cout << m_program[0] << '\n';
}

void Computer::assign_code()
{
    m_opcode          = m_program[m_instruction_pointer];
    m_parameter_one   = m_program[m_instruction_pointer + 1];
    m_parameter_two   = m_program[m_instruction_pointer + 2];
    m_parameter_three = m_program[m_instruction_pointer + 3];
}

void Computer::run()
{
    while ( m_opcode != 99 )
    {
        if ( m_opcode == 1 )
        {
            m_program[m_parameter_three] = m_program[m_parameter_one] + m_program[m_parameter_two];
        }

        else if ( m_opcode == 2 )
        {
           m_program[m_parameter_three] = m_program[m_parameter_one] * m_program[m_parameter_two];
        }

        m_instruction_pointer += m_step;
        assign_code();
    }

    print();
}

int main()
{
    // read puzzle input
    std::ifstream PuzzleInput("include/Day_02_Input.txt");
    std::string line;
    std::vector<int> program;
    std::string code;

    while ( PuzzleInput >> line )
    {
        std::stringstream ss(line);
        while( ss.good() )
        {
            std::getline( ss, code, ',' );
            program.push_back( std::stoi(code) );
        }
    }

    // replace program[1] <- 12; program[2] <- 2
    program[1] = 12;
    program[2] = 2;

    // run the program
    Computer c(program);
    c.run();
}