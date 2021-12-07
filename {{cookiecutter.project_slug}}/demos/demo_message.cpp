#include <{{cookiecutter.library_name}}/{{cookiecutter.library_name}}.hpp>
#include <iostream>
#include <string>

using namespace std;

int main()
{
    string demo_msg;
    demo_msg = {{cookiecutter.cpp_namespace}}::message("World");
    cout << demo_msg << endl;
    return 0;
}
