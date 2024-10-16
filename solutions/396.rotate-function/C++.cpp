class Solution {
public:
    int maxRotateFunction(vector<int>& nums) {
        long sum = 0, F = 0, maxF = INT_MIN;
        int n = nums.size();
        
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            F += i * nums[i];
        }
        
        maxF = F;
        
        for (int i = 1; i < n; i++) {
            F = F + sum - n * nums[n - i];
            maxF = max(maxF, F);
        }
        
        return maxF;
    }
};