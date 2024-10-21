class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        int jumps = 0, current_end = 0, furthest = 0;
        
        for (int i = 0; i < n - 1; ++i) {
            furthest = max(furthest, i + nums[i]);
            if (i == current_end) {
                jumps++;
                current_end = furthest;
            }
        }
        return jumps;
    }
};