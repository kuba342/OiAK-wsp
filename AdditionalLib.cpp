#include "AdditionalLib.hpp"
#include <string>

using namespace std;

bool AdditionalLib::isNum(std::string str){
    for(int a = 0; a < str.length(); a++) {
        if(str[a] > '0' + 9 || str[a] < '0') return false;
    }
    return true;
}

AdditionalLib::AdditionalLib(){}

AdditionalLib::~AdditionalLib(){}

