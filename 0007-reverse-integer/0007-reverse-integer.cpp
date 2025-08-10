#include <string>
using namespace std;

class Solution
{
public:
    int reverse(int x)
    {
        string number = to_string(x);
        
        string reverse = "";
        char negative= ' ';
        if (number[0] == '-')
        {
            negative = '-';
            number.erase(0,1);
        }
        
        for (int i = number.size() - 1; i >= 0; i--)
        {
            reverse += number[i];
        }
        long long xReverse = stoll(negative + reverse);
        if( xReverse > INT_MAX || xReverse< INT_MIN){
            return 0;
        }
        else{
            return xReverse;
        }
    }
};
