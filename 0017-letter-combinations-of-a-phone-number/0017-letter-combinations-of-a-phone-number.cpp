#include <vector>
#include <string>
#include <map>

using namespace std;

class Solution
{
private:
    const map<char, string> numbers = {
        {'2', "abc"}, {'3', "def"}, {'4', "ghi"}, {'5', "jkl"}, {'6', "mno"}, {'7', "pqrs"}, {'8', "tuv"}, {'9', "wxyz"}};

    void findCombinations(const string &digits, int i, string current, vector<string> &result)
    {

        if (i == digits.length())
        {
            result.push_back(current);
            return;
        }

        string letters = numbers.at(digits[i]);

        for (char c : letters)
        {

            findCombinations(digits, i + 1, current + c, result);
        }
    }

public:
    vector<string> letterCombinations(string digits)
    {

        vector<string> result;

        if (digits.empty())
        {
            return result;
        }

        findCombinations(digits, 0, "", result);

        return result;
    }
};