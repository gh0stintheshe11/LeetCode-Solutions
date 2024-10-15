from typing import List

class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Calculate initial total value
        total_value = sum(abs(nums[i] - nums[i + 1]) for i in range(n - 1))
        
        # Store max gain from possible bounds reversals
        max_gain = 0
        
        # Consider the gain when reversing subarray within entire array
        # The potential gain from each reversal and maintain a track of global boundaries max values
        max1 = float('-inf')
        min1 = float('inf')

        for i in range(n - 1):
            max1 = max(max1, min(nums[i], nums[i + 1]))
            min1 = min(min1, max(nums[i], nums[i + 1]))
        
        max_gain = max(max_gain, (max1 - min1) * 2)

        # Consider the gain when reversing at start or end
        for i in range(1, n - 1):
            max_gain = max(max_gain,
                           abs(nums[0] - nums[i + 1]) - abs(nums[i] - nums[i + 1]),
                           abs(nums[n - 1] - nums[i - 1]) - abs(nums[i] - nums[i - 1]))

        return total_value + max_gain