from typing import List

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        n = len(nums)
        
        # Looking for a subarray whose sum is equivalent to target % total_sum.
        subarray_target = target % total_sum
        
        # Special case if subarray_target is 0
        if subarray_target == 0:
            return (target // total_sum) * n
        
        # Dictionary to store prefix sum and their indices
        prefix_sum_indices = {0: -1}
        current_sum = 0
        min_len_inf = float('inf')

        for i in range(2 * n):  # Iterate over the array twice to mimic infinite array
            current_num = nums[i % n]
            current_sum += current_num
            
            if (current_sum - subarray_target) in prefix_sum_indices:
                length = i - prefix_sum_indices[current_sum - subarray_target]
                min_len_inf = min(min_len_inf, length)

            # Save the first appearance of the current sum
            if current_sum not in prefix_sum_indices:
                prefix_sum_indices[current_sum] = i

        # If the min_len_inf is still infinity, we have not found such subarray
        if min_len_inf == float('inf'):
            return -1
        
        full_repititions = target // total_sum
        return min_len_inf + (full_repititions * n)