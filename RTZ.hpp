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
    //Obliczenia parametrów
    void calc_Kplus();
    void calc_Kminus();
    void calc_Xplus();
    void calc_Xminus();
    void calc_Yplus();
    void calc_Yminus();
    void calc_Aplus();
    void calc_Aminus();
public:
    int max_int;
    RTZ(int n, int d);
    ~RTZ();
    void count_all();
    void show_param();
    //Część decyzyjna (Wybranie Kplus lub KMinus itd.) 
    /*Przemyśleć*/
};

#endif