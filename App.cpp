#include "App.hpp"
#include <iostream>
#include <unistd.h>

using namespace std;

App::App(){
    this->lib = new AdditionalLib();
}

App::~App(){

}

void App::showMessage(){
    std::cout << "Obliczanie wspolczynnikow potrzebnych do projektu\n"
              << "Organizacja i Architektura Komputerow - projekt";
}

void App::mainLoop(){
    system("cls");
    showMessage();
    sleep(2);
    system("cls");

    while(1){
        system("cls");
        std::cout << "Liczba bitow dzielenia n = ";
        std::string bufor;
        std::cin >> bufor;
        fflush(stdin);
        if(this->lib->isNum(bufor)){
            int number = std::stoi(bufor);
            this->n = number;
        }
        else{
            continue;
        }
        std::cout << "\n";

        std::cout << "Staly dzielnik d = ";
        std::cin >> bufor;
        fflush(stdin);
        if(this->lib->isNum(bufor)){
            int number = std::stoi(bufor);
            this->d = number;
        }
        else{
            continue;
        }

    }
}

