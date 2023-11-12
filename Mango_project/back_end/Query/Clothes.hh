#ifndef _CLOTHES_HH_
#define _CLOTHES_HH_

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <map>
using namespace std;


class Clothes {
    private:
        
        string id;
        string color;
        string sex;
        string age;
        string aggregatedFamily;
        string prodFamily;
        vector<bool> kind; // kind[0] = true => type bottom
                           // kind[1] = true => type tops
                           // kind[2] = true => type outerwear 

    public:
    string cathegory;
        // Constructors
        Clothes();
        Clothes(string id, string color, string sex, string age, string cathegory, string aggregatedFamily, string prodFamily); 

        // Query methods
        string getId();
        string getColor();
        string getSex();
        string getAge();
        string getCathegory();
        string getAggregatedFamily();
        string getProdFamily();
        vector<bool> getType();
};

#endif