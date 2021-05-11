#ifndef App_hpp
#define App_hpp

#include "AdditionalLib.hpp"
#include <string>
#include "RTZ.hpp"

class App
{
private:
    AdditionalLib* lib;
    RTZ* rtz;
    int n;          //Liczba bitów n - podstawowa zależność
    int d;          //Stały dzielnik d
    
public:
    App();
    ~App();
    void mainLoop();
    void showMessage();
};

#endif
