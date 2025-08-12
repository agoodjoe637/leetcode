#include <string>
#include <climits>
using namespace std;

class Solution
{
public:
    int myAtoi(string s)
    {
        int i = 0;

        while (i < s.size() && s[i] == ' ')
            i++;

        bool isNegative = false;
        if (i < s.size() && s[i] == '-')
        {
            isNegative = true;
            i++;
        }
        else if (i < s.size() && s[i] == '+')
        {
            i++;
        }

        long long number = 0;
        while (i < s.size() && isdigit(s[i]))
        {
            int digit = s[i] - '0';

            if (number > INT_MAX / 10 || (number == INT_MAX / 10 && digit > (isNegative ? 8 : 7)))
            {
                return isNegative ? INT_MIN : INT_MAX;
            }

            number = number * 10 + digit;
            i++;
        }

        if (isNegative)
            number = -number;

        return (int)number;
    }
};
