#include <vector>
#include <cmath>
#include <climits>

using namespace std;
class Solution
{
public:
    int threeSumClosest(vector<int> &nums, int target)
    {

        int min_diff = INT_MAX;

        int result_sum = 0;

        for (int i = 0; i < nums.size(); i++)
        {
            for (int j = i + 1; j < nums.size(); j++)
            {
                for (int k = j + 1; k < nums.size(); k++)
                {
                    int current_sum = nums[i] + nums[j] + nums[k];

                    int current_diff = abs(target - current_sum);

                    if (current_diff < min_diff)
                    {
                        min_diff = current_diff;
                        result_sum = current_sum;
                    }
                }
            }
        }

        return result_sum;
    }
};