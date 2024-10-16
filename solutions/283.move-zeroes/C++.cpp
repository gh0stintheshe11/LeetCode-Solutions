class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int lastNonZeroIndex = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] != 0) {
                nums[lastNonZeroIndex++] = nums[i];
            }
        }
        for (int i = lastNonZeroIndex; i < nums.size(); ++i) {
            nums[i] = 0;
        }
    }
};