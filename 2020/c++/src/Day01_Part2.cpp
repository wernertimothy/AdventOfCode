#include <iostream>
#include <deque>
#include <fstream>

int main(void) {

    std::deque<int> expense_report;
    int expense;

    std::ifstream PuzzleInput("include/Day01.txt");

    while (PuzzleInput >> expense) {
        expense_report.push_back(expense);
    }

    for(int a: expense_report) {
        for (int b: expense_report) {
            for (int c: expense_report) {
                if (a + b + c == 2020) {
                std::cout << "the solution is: " << a << "*" << b << "*" << c << "=" << a*b*c << std::endl;
                goto exit;
                }
            }
        }
    }
    exit: return 0;
}