#include <vector>
#include <stack>
#include <climits>

class Solution {
public:
    bool find132pattern(std::vector<int>& nums) {
        int n = nums.size();
        int third = INT_MIN;
        std::stack<int> s;

        for (int i = n - 1; i >= 0; --i) {
            if (nums[i] < third) {
                return true;
            }
            while (!s.empty() && nums[i] > s.top()) {
                third = s.top();
                s.pop();
            }
            s.push(nums[i]);
        }

        return false;
    }
};