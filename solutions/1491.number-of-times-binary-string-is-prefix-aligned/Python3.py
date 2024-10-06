from typing import List

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max_flipped = 0
        count_aligned = 0
        
        for i, flip in enumerate(flips, start=1):
            max_flipped = max(max_flipped, flip)
            if max_flipped == i:
                count_aligned += 1
        
        return count_aligned