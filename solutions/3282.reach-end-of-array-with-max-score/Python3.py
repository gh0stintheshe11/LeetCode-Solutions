from typing import List

class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        max_so_far = 0
        total_score = 0
        
        for num in nums[:-1]: 
            max_so_far = max(max_so_far, num)
            total_score += max_so_far
        
        return total_score