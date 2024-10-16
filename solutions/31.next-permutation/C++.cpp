class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size();
        int i = n - 2;
        
        // Step 1: Find the first decreasing element from the right
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }
        
        if (i >= 0) {
            // Step 2: Find the element just bigger than nums[i] to its right
            int j = n - 1;
            while (nums[j] <= nums[i]) {
                j--;
            }
            // Step 3: Swap the found elements
            swap(nums[i], nums[j]);
        }
        
        // Step 4: Reverse the elements to the right of i
        reverse(nums.begin() + i + 1, nums.end());
    }
};