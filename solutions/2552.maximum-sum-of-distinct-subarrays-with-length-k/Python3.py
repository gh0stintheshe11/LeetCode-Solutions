from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if k > len(nums):
            return 0
        
        num_count = {}
        current_sum = 0
        max_sum = 0
        distinct_count = 0
        
        for i in range(len(nums)):
            # Add the new element to the current window
            current_num = nums[i]
            num_count[current_num] = num_count.get(current_num, 0) + 1
            
            if num_count[current_num] == 1:
                distinct_count += 1
            current_sum += current_num
            
            # If window size exceeds k, remove the left-most element of the window
            if i >= k:
                left_num = nums[i - k]
                num_count[left_num] -= 1
                
                if num_count[left_num] == 0:
                    distinct_count -= 1
                current_sum -= left_num
            
            # Check if the window is valid and update max sum
            if i >= k - 1 and distinct_count == k:
                max_sum = max(max_sum, current_sum)
        
        return max_sum