class Solution {
public:
    int minSubarray(vector<int>& nums, int p) {
        int n = nums.size();
        long long total_sum = 0;
        for (int num : nums) {
            total_sum += num;
        }
        int target_modulo = total_sum % p;
        if (target_modulo == 0) return 0; // Already divisible
        
        unordered_map<int, int> prefix_mod_index;
        prefix_mod_index[0] = -1; // To handle the case when subarray starts from index 0
        int min_len = n;
        long long current_prefix_sum = 0;
        
        for (int i = 0; i < n; ++i) {
            current_prefix_sum += nums[i];
            int current_mod = current_prefix_sum % p;
            int desired_mod = (current_mod - target_modulo + p) % p;
            
            if (prefix_mod_index.find(desired_mod) != prefix_mod_index.end()) {
                min_len = min(min_len, i - prefix_mod_index[desired_mod]);
            }
            
            // Save the current prefix modulo with the current index
            prefix_mod_index[current_mod] = i;
        }
        
        return min_len < n ? min_len : -1; // If min_len is still n, we could not find any valid subarray
    }
};