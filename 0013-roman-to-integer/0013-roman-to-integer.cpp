#include <string>

using namespace std;

class Solution
{
public:
    int romanToInt(string s)
    {
        int previousValue = 0;
        int result = 0;
        for (int i = s.length() - 1; i >= 0; i--)
        {
            int currentValue = getValue(s[i]);

            if (currentValue < previousValue)
            {
                result -= currentValue;
            }
            else
            {
                result += currentValue;
            }

            previousValue = currentValue;
        }

        return result;
    }

private:
    int getValue(char c)
    {
        switch (c)
        {
        case 'I':
            return 1;
        case 'V':
            return 5;
        case 'X':
            return 10;
        case 'L':
            return 50;
        case 'C':
            return 100;
        case 'D':
            return 500;
        case 'M':
            return 1000;
        default:
            return 0;
        }
    }
};