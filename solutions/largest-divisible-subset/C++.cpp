class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        if (nums.empty()) return {};
        
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<int> dp(n, 1), prev(n, -1);
        int max_size = 0, max_index = -1;
        
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (nums[i] % nums[j] == 0 && dp[i] < dp[j] + 1) {
                    dp[i] = dp[j] + 1;
                    prev[i] = j;
                }
            }
            if (dp[i] > max_size) {
                max_size = dp[i];
                max_index = i;
            }
        }
        
        vector<int> result;
        for (int i = max_index; i >= 0; i = prev[i]) {
            result.push_back(nums[i]);
        }
        return result;
    }
};