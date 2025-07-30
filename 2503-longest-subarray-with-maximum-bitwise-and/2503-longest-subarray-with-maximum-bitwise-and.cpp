#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int longestSubarray(vector<int> &nums)
    {
        int enBuyuk = nums[0];
        vector<int> subArrays;

        for (int current : nums)
        {
            if (current > enBuyuk)
            {
                enBuyuk = current;
            }
        }

        int count = 0;

        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] == enBuyuk)
            {
                count++;
            }
            else
            {
                subArrays.push_back(count);
                count = 0;
            }
        }
        subArrays.push_back(count);

        return *max_element(subArrays.begin(), subArrays.end());
    }
};