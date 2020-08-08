
#include <fstream>
#include <string>
#include <sstream>
#include <iostream>

#include "Day_02.hpp"

using namespace day_02;

computer::computer(const std::vector<int>& the_program) : m_program(the_program)
{
    m_index = 0;
    assign_code();
}

void computer::print() const
{
    std::cout << m_program[0] << '\n';
}

void computer::assign_code()
{
    m_opcode       = m_program[m_index];
    m_position_one = m_program[m_index + 1];
    m_position_two = m_program[m_index + 2];
    m_place        = m_program[m_index + 3];
}

void computer::run()
{
    while ( m_opcode != 99 )
    {
        if ( m_opcode == 1 )
        {
            m_program[m_place] = m_program[m_position_one] + m_program[m_position_two];
        }

        else if ( m_opcode == 2 )
        {
           m_program[m_place] = m_program[m_position_one] * m_program[m_position_two];
        }

        m_index += m_step;
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
    computer c(program);
    c.run();
}