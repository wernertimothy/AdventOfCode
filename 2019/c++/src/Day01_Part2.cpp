#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

int fuel_mass(const int& the_mass)
{   
    const int tmp_mass = std::floor( the_mass / 3 ) - 2;
    // base case
    if ( tmp_mass <= 0) { return 0; };
    // recursion
    return tmp_mass + fuel_mass( tmp_mass );
}

int main()
{
    int fuel_requirement = 0;
    int mass;
    std::ifstream PuzzleInput("include/Day_01_Input.txt");

    while (PuzzleInput >> mass)
    {
        fuel_requirement += fuel_mass(mass);
    }

    std::cout << fuel_requirement << std::endl;
}