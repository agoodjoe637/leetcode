#include <vector>
using namespace std;

class Solution
{
public:
  int removeDuplicates(vector<int> &nums)
  {
    if (nums.size() < 2)
    {
      return nums.size();
    }

    int yazma_indeksi = 1;

    for (int okuma_indeksi = 1; okuma_indeksi < nums.size(); okuma_indeksi++)
    {
      if (nums[okuma_indeksi] != nums[yazma_indeksi-1]){
        nums[yazma_indeksi]=nums[okuma_indeksi];
        yazma_indeksi++;
      }
    }
    return yazma_indeksi;
  }
};