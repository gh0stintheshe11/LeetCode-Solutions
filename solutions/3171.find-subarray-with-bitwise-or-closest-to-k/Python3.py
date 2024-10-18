from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        min_diff = float('inf')
        
        # Represents the possible OR results with subarrays ending at the previous position.
        prev_or = set()
        
        for num in nums:
            cur_or = {num}
            
            for prev in prev_or:
                cur_or.add(prev | num)
            
            for value in cur_or:
                min_diff = min(min_diff, abs(k - value))
                
            prev_or = cur_or
        
        return min_diff