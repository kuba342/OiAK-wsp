#ifndef RTZ_hpp
#define RTZ_hpp
class RTZ
{
private:
    int n;
    int d;
    int Xplus;
    int Xminus;
    int Yplus;
    int Yminus;
    int Kplus;
    int Kminus;
    int Aplus;
    int Aminus;
public:
    RTZ(int n, int d);
    ~RTZ();
    //Obliczenia parametrów
    void calc_Kplus();
    void calc_Kminus();
    void calc_Xplus();
    void calc_Xminus();
    void calc_Yplus();
    void calc_Yminus();
    void calc_Aplus();
    void calc_Aminus();
    //Część decyzyjna (Wybranie Kplus lub KMinus itd.) 
    /*Przemyśleć*/
};

#endif