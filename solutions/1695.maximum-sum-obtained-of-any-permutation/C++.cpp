class Solution {
public:
    int maxSumRangeQuery(vector<int>& nums, vector<vector<int>>& requests) {
        int n = nums.size();
        vector<int> count(n, 0);
        
        for (const auto& req : requests) {
            count[req[0]]++;
            if (req[1] + 1 < n) {
                count[req[1] + 1]--;
            }
        }
        
        for (int i = 1; i < n; ++i) {
            count[i] += count[i - 1];
        }
        
        sort(count.begin(), count.end());
        sort(nums.begin(), nums.end());
        
        long long result = 0;
        int mod = 1e9 + 7;

        for (int i = 0; i < n; ++i) {
            result = (result + ((long long)count[i] * nums[i]) % mod) % mod;
        }

        return (int)result;
    }
};