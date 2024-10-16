class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if (nums.empty()) return 0;
        
        int maxProduct = nums[0];
        int currentMax = nums[0];
        int currentMin = nums[0];
        
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] < 0) {
                std::swap(currentMax, currentMin);
            }
            
            currentMax = std::max(nums[i], currentMax * nums[i]);
            currentMin = std::min(nums[i], currentMin * nums[i]);
            
            maxProduct = std::max(maxProduct, currentMax);
        }
        
        return maxProduct;
    }
};