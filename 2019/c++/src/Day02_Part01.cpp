#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>


namespace computer_ns
{
    class computer
    {
    // public members
    public:
    std::vector<int> m_program;

    // constructor
    computer(const std::vector<int>& the_program);
    // public methods
    void run();

    // private members
    private:
    int m_opcode;

    int m_position_one;
    int m_position_two;
    int m_place;

    int m_step = 4;

    int m_index;

    // private methods
    void assign_code();
    void print() const;

    };
} // computer_ns

computer_ns::computer::computer(const std::vector<int>& the_program) : m_program(the_program)
{
    m_index = 0;
    assign_code();
}

void computer_ns::computer::print() const
{
    std::cout << m_program[0] << '\n';
}

void computer_ns::computer::assign_code()
{
    m_opcode       = m_program[m_index];
    m_position_one = m_program[m_index + 1];
    m_position_two = m_program[m_index + 2];
    m_place        = m_program[m_index + 3];
}

void computer_ns::computer::run()
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
    computer_ns::computer c(program);
    c.run();
}