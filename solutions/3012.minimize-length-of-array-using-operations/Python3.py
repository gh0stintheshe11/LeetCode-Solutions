from typing import List
from collections import defaultdict

class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        min_val = min(nums)
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        # If min_val occurs only once, the answer is 1.
        if count[min_val] == 1:
            return 1
        
        # Check if there is a y such that y % min_val != 0
        for num in nums:
            if num % min_val != 0:
                return 1
        
        # Otherwise, the answer is ceil(count[min_val] / 2)
        return (count[min_val] + 1) // 2