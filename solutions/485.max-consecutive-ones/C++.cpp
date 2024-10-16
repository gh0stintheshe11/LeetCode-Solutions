class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int maxCount = 0, count = 0;
        for (int num : nums) {
            if (num == 1) {
                count++;
            } else {
                maxCount = max(maxCount, count);
                count = 0;
            }
        }
        return max(maxCount, count);
    }
};