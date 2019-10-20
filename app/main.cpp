#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>
using namespace std;
int main() {
    string input;
    cout << "Welcome to pymath available calculators include algebra, chemistry, geometry, misc, physics\nWhich do you want?: ";
    cin >> input;
    if (input == "algebra") {
        string input1;
        cout << "Welcome to the algebra part of pymath available calculators include logorithm calc(log), and quadratic equation calc(quad)!\nWhich do you want?: ";
        cin >> input1;
        if (input1 == "log") {
            string base;
            string result;
            cout << "What is the base number?: ";
            cin >> base;
            cout << "What is the result?: ";
            cin >> result;
            ofstream outfile;
            outfile.open("output.txt");
            outfile << base << endl << result << endl;
            system("python3 app/logexe.py < output.txt");
        }
    }
}