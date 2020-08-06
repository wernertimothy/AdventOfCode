#include <iostream>
#include <fstream>
#include <deque>
#include <cmath>

int fuel_requirement(std::deque<int>& the_masses)
{
    int tmp_mass = std::floor(the_masses[0] / 3 - 2);

    // base case:
    if (the_masses.size() == 1)
    {
        return tmp_mass;
    }
    // recursion:
    the_masses.pop_front();
    return tmp_mass + fuel_requirement( the_masses );
}

int main()
{
    std::deque<int> mass_list;
    int mass;
    std::ifstream PuzzleInput("include/Day_01_Input.txt");

    while (PuzzleInput >> mass)
    {
        mass_list.push_back(mass);
    }
    
    int fuel = fuel_requirement(mass_list);
    std::cout << "the fuel required is:" << fuel << std::endl;
}