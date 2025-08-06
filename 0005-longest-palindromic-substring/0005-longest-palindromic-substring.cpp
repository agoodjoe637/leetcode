#include <string>

#include <vector>

using namespace std;

class Solution
{
public:
    string longestPalindrome(string s)
    {
        int finalMaxLength = 0;
        int finalStart = 0;
        for (int i = 0; i < s.size(); i++)
        {
            int anlikEnUzun = 0;

            int kaydir = 1;
            while ((0 <= i - kaydir && i + kaydir < s.size()) && s[i - kaydir] == s[i + kaydir])
            {

                kaydir++;
            }
            int uzunluk1 = 2 * (kaydir - 1) + 1;
            int start1 = i - (kaydir - 1);

            if (uzunluk1 > finalMaxLength)
            {
                finalMaxLength = uzunluk1;
                finalStart = start1;
            }

            int left = i;
            int right = i + 1;
            while (0 <= left && right < s.size() && s[left] == s[right])
            {
                left--;
                right++;
            }
            int uzunluk2 = (right - left - 1);
            int start2 = left + 1;

            if (uzunluk2 > finalMaxLength)
            {
                finalMaxLength = uzunluk2;
                finalStart = start2;
            }
        }

        return s.substr(finalStart, finalMaxLength);
    }
};