#include <vector>
#include <math.h>

using namespace std;
class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        int left = 0;
        int right = height.size() - 1;
        int mostWater = min(height[left], height[right]) * (right - left);
        while (left < right)
        {
            if (height[left] < height[right])
            {
                left++;
            }
            else
            {
                right--;
            }
            int currentWater= min(height[left], height[right]) * (right - left);
            mostWater= max(mostWater,currentWater);
        }
        return mostWater;
    }
};