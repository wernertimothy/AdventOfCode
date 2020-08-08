#pragma once

#include <vector>

namespace day_02
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
    void reset(const std::vector<int>& the_program);

    // private members
    private:
    int m_opcode;

    int m_parameter_one;
    int m_parameter_two;
    int m_parameter_three;

    int m_step = 4;

    int m_instruction_pointer;

    // private methods
    void assign_code();
    void print() const;

    };
} // namespace day_02