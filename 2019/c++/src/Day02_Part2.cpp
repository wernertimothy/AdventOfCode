#include <fstream>
#include <string>
#include <sstream>
#include <iostream>
#include <tuple>

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

void Computer::reset(const std::vector<int>& the_program)
{
    m_program = the_program;
    m_instruction_pointer = 0;
    assign_code();
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

    // print();
}

std::tuple<int, int> brute_force(std::vector<int>& the_program)
{
    Computer c(the_program);

    // bruteforce noun and verb
    for (int noun = 0; noun <= 99; noun++)
    {
        for (int verb = 0; verb <= 99; verb++)
        {
            std::vector<int> the_program_copy = the_program;
            // replace program[1] <- noun; program[2] <- verb
            the_program_copy[1] = noun;
            the_program_copy[2] = verb;
            c.reset(the_program_copy);
            c.run();

            if ( c.m_program[0] == 19690720)
            {
                return std::make_tuple(noun, verb);
            }           
        }
    }
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

    int noun{0};
    int verb{0};
    std::tie(noun, verb) = brute_force(program);

    std::cout << "noun:" << noun << '\n' << "verb:" << verb << '\n' << "reult:" << 100*noun + verb << '\n';
}