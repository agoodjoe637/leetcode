#include <vector>
using namespace std;
class Solution
{
public:
    int removeElement(vector<int> &nums, int val)
    {
        int end = nums.size() - 1;
        int i = 0;

        while (i <= end)
        {
            if (nums[i] == val)
            {
                nums[i] = nums[end];
                end--;
            }
            else
            {
                i++;
            }
        }

        return i;
    }
};