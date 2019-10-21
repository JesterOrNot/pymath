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
            string base, result;
            cout << "What is the base number?: ";
            cin >> base;
            cout << "What is the result?: ";
            cin >> result;
            ofstream outfile;
            outfile.open("app/data/output.txt");
            outfile << base << endl << result << endl;
            system("python3 app/lib/logexe.py < app/output.txt");
        } else if (input1 == "quad") {
            string a,b,c;
            cout << "What is a?: ";
            cin >> a;
            cout << "What is b?: ";
            cin >> b;
            cout << "What is c?: ";
            cin >> c;
            ofstream outfile;
            outfile.open("app/data/output.txt");
            outfile << a << endl << b << endl << c << endl;
            system("python3 app/lib/quadexe.py < app/data/output.txt");
        }
    } else if (input == "geometry") {
        string input1;
        cout << "Welcome to the geometry part of pymath available calculators include circumfrence calculator(circ), pythagorean theorem calc(pythag), area calc(area)\nWhich do you want?: ";
        cin >> input1;
        if (input1 == "circ") {
            string circumfrence;
            cout << "What is the diameter?: ";
            cin >> circumfrence;
            ofstream outfile;
            outfile.open("app/data/output.txt");
            outfile << circumfrence << endl;
            system("python3 app/lib/circexe.py < app/data/output.txt");
        } else if (input1 == "pythag") {
            string a,b;
            cout << "What is a?: ";
            cin >> a;
            cout << "What is b?: ";
            cin >> b;
            ofstream outfile;
            outfile.open("app/data/output.txt");
            outfile << a << endl << b << endl;
            system("python3 app/lib/pythagexe.py < app/data/output.txt");
        }
    }
}