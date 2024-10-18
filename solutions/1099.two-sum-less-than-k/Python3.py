from typing import List

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        # Sort the array
        nums.sort()
        
        # Initialize pointers
        left, right = 0, len(nums) - 1
        max_sum = -1
        
        # Iterate with two pointers
        while left < right:
            current_sum = nums[left] + nums[right]
            
            # Check if the current sum is less than k
            if current_sum < k:
                # Update max_sum if the current sum is greater than the previous max_sum
                max_sum = max(max_sum, current_sum)
                # Move the left pointer to the right to try to increase the sum
                left += 1
            else:
                # Move the right pointer to the left to try to decrease the sum
                right -= 1
        
        return max_sum
