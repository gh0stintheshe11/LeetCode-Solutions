#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> numIndices;
        
        for (int i = 0; i < nums.size(); ++i) {
            if (numIndices.find(nums[i]) != numIndices.end() && i - numIndices[nums[i]] <= k) {
                return true;
            }
            numIndices[nums[i]] = i;
        }
        
        return false;
    }
};