#include <string>
#include <vector>
using namespace std;
class Solution
{
public:
    string convert(string s, int numRows)
    {
        if (numRows == 1)
        {
            return s;
        }
        vector<string> satirlar(numRows);
        bool yon = false;
        int currentRow = 0;
        string finalString;

        for( char c : s){
            satirlar[currentRow] += c;
            if(currentRow== 0 || currentRow== numRows -1){
                yon = !yon;
            }
            if(yon){
                currentRow++;
            }
            else{
                currentRow--;
            }
        }
        for(string ss : satirlar){
            finalString += ss;
        }
        return finalString;
    }
};