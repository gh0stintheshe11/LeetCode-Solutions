class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        min_sum = float('inf')
        current_max = 0
        current_min = 0
        
        for num in nums:
            current_max += num
            current_min += num
            max_sum = max(max_sum, current_max)
            min_sum = min(min_sum, current_min)
            if current_max < 0:
                current_max = 0
            if current_min > 0:
                current_min = 0
        
        return max(max_sum, -min_sum)