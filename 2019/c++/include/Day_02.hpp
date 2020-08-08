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
} // namespace day_02