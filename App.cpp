#include "App.hpp"
#include <iostream>
#include <unistd.h>
#include "RTZ.hpp"

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
            system("cls");
            std::cout << "Niepoprawne dane!";
            sleep(3);
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
            system("cls");
            std::cout << "Niepoprawne dane!";
            sleep(3);
            continue;
        }

        this->rtz = new RTZ(this->n, this->d);
        this->rtz->count_all();
        this->rtz->show_param();
        std::cin.get();
        //Reszta operacji związanych z tworzeniem obiektów klas RTZ, FR i RTE
    }
}

