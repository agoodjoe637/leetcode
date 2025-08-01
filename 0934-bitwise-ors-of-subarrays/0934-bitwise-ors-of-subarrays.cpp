#include <vector>
#include <unordered_set>

using namespace std;

class Solution
{
public:
    int subarrayBitwiseORs(vector<int> &arr)
    {
        unordered_set<int> total_results;

        unordered_set<int> previous_results;

        for (int x : arr)
        {

            unordered_set<int> current_results;

            current_results.insert(x);

            for (int prev_res : previous_results)
            {
                current_results.insert(prev_res | x);
            }

            for (int res : current_results)
            {
                total_results.insert(res);
            }

            previous_results = current_results;
        }

        return total_results.size();
    }
};