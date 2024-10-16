#include <vector>
#include <algorithm>

class Solution {
public:
    int minMoves2(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int median = nums[nums.size() / 2];
        int moves = 0;
        for (int num : nums) {
            moves += std::abs(num - median);
        }
        return moves;
    }
};