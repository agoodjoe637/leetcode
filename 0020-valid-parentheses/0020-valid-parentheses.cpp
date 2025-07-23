#include <vector>
#include <string>
#include <stack>

using namespace std;
class Solution
{
public:
    bool isValid(string s)
    {
        stack<char> brackets;
        for (char c : s)
        {
            if (c == '(' || c == '[' || c == '{')
            {
                brackets.push(c);
            }
            else if (c == ')' || c == ']' || c == '}')
            {
                if (brackets.empty())
                {
                    return false;
                }

                char topChar = brackets.top();
                if (c == ']' && topChar == '[' || c == ')' && topChar == '(' || c == '}' && topChar == '{'){
                    brackets.pop();
                }
                else{
                    return false;
                }
            }
        }

        return brackets.empty();

    }
};