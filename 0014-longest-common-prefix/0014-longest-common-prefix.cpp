#include <vector>
#include <string>

using namespace std;
class Solution
{
public:
    string longestCommonPrefix(vector<string> &strs)
    {
        if (strs.empty())
        {
            return "";
        }

        int minLength = strs[0].length();

        for (const string &s : strs)
        {
            if (s.length() < minLength)
            {
                minLength = s.length();
            }
        }

        string commonPrefix = "";

        for (int i = 0; i < minLength; i++)
        {
            char c= strs[0][i];
            bool match= true;

            for (int j=1; j<strs.size();j++){
                if( c!=strs[j][i]){
                    match= false;
                    return commonPrefix;

                }
                
            }

          if(match){
                commonPrefix+= c;
            
            }
              
           
            
        }
        
      return commonPrefix;
    }

    
};