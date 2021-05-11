#include "RTZ.hpp"
#include <iostream>
#include "math.h"

RTZ::RTZ(int n, int d){
    this->max_int = 2147483647;
    this->d = d;
    this->n = n;
    this->Xplus = 0;
    this->Xminus = 0;
    this->Yplus = 0;
    this->Yminus = 0;
    this->Kplus = 0;
    this->Kminus = 0;
    this->Aplus = 0;
    this->Aminus = 0;
}

RTZ::~RTZ(){

}

void RTZ::count_all(){
    //Zgodnie z algorytmem obliczania:
    calc_Xminus();
    calc_Xplus();
    calc_Kminus();
    calc_Kplus();
    calc_Aminus();
    calc_Aplus();
}

void RTZ::show_param(){
    std::cout << "Xminus = " << this->Xminus << "\n";
    std::cout << "Xplus = " << this->Xplus << "\n";
    std::cout << "Kminus = " << this->Kminus << "\n";
    std::cout << "Kplus = " << this->Kplus << "\n";
    std::cout << "Aminus = " << this->Aminus << "\n";
    std::cout << "Aplus = " << this->Aplus << "\n";
}

void RTZ::calc_Kplus(){
    int k;
    for(int i=0; this->max_int ;i++){
        k = ((int)pow(2,i) / (-(int)(pow(2,i)) % this->d));
        if(k > this->Xplus){
            this->Kplus = k;
            break;
        }
    }
}

void RTZ::calc_Kminus(){
    int k;
    for(int i=0; i<this->max_int; i++){
        k = ((int)pow(2,i)) / ( ((int)pow(2,i)) % this->d );
        if(k > this->Xminus){
            this->Kminus = k;
            break;
        }
    }
}

void RTZ::calc_Xplus(){
    int x;
    int power;
    power = (int)pow(2,this->n);
    x = (this->d * (int)floor(power/this->d)) - 1; //Sprawdzić ten moment
    //Przypisanie wartości do pola obiektu
    this->Xplus = x;
}

void RTZ::calc_Xminus(){
    int x;
    int power;
    power = (int)pow(2,this->n);
    x = (this->d * (int)floor(power/this->d)) - this->d + 1; //Sprawdzić ten moment
    //Przypisanie wartości do pola obiektu
    this->Xminus = x;
}

void RTZ::calc_Yplus(){

}

void RTZ::calc_Yminus(){

}

void RTZ::calc_Aplus(){
    int a;
    a = ceil(pow(2,this->Kplus)/this->d);
    this->Aplus = a;
}

void RTZ::calc_Aminus(){
    int a;
    a = floor(pow(2,this->Kminus)/this->d);
    this->Aminus = a;
}