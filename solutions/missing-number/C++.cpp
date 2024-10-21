class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int total_sum = n * (n + 1) / 2;
        int array_sum = 0;
        for (int num : nums) {
            array_sum += num;
        }
        return total_sum - array_sum;
    }
};