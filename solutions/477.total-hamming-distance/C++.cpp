class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        int total = 0;
        int n = nums.size();
        
        for (int i = 0; i < 32; i++) {
            int bitCount = 0;
            for (int num : nums) {
                if (num & (1 << i)) {
                    bitCount++;
                }
            }
            total += bitCount * (n - bitCount);
        }
        
        return total;
    }
};