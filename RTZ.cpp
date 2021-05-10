#include "RTZ.hpp"
#include <iostream>
#include "math.h"

RTZ::RTZ(int n, int d){
    this->d = d;
    this->n = n;
    this->Xplus = 0;
    this->Xminus = 0;
    this->Yplus = 0;
    this->Yminus = 0;
}

RTZ::~RTZ(){

}

void RTZ::calc_Kplus(){

}

void RTZ::calc_Kminus(){

}

void RTZ::calc_Xplus(){
    int x;
    int power;
    power = pow(2,(float)this->n);
    x = (this->d * floor(power/this->d)) - 1; //Sprawdzić ten moment
    //Przypisanie wartości do pola obiektu
    this->Xplus = x;
}

void RTZ::calc_Xminus(){
    int x;
    int power;
    power = pow(2,(float)this->n);
    x = (this->d * floor(power/this->d)) - this->d + 1; //Sprawdzić ten moment
    //Przypisanie wartości do pola obiektu
    this->Xminus = x;
}

void RTZ::calc_Yplus(){

}

void RTZ::calc_Yminus(){

}

void RTZ::calc_Aplus(){

}

void RTZ::calc_Aminus(){

}