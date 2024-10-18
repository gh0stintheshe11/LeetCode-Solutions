from typing import List

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = len(nums)
        min_average = float('inf')
        
        for i in range(n // 2):
            current_average = (nums[i] + nums[n - i - 1]) / 2
            min_average = min(min_average, current_average)
        
        return min_average