from typing import List
from collections import defaultdict

class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        n = len(nums)
        positions = defaultdict(list)
        
        # Record the positions of each number in the circular extended (by doubling) array
        for i, num in enumerate(nums):
            positions[num].append(i)
        
        min_seconds = float('inf')
        
        for pos in positions.values():
            pos.append(pos[0] + n)  # simulate the circular part of the array
            
            max_gap = 0
            for j in range(1, len(pos)):
                max_gap = max(max_gap, (pos[j] - pos[j - 1]) // 2)
                
            min_seconds = min(min_seconds, max_gap)
        
        return min_seconds