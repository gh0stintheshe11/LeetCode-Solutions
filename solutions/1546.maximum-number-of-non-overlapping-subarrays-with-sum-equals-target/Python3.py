from typing import List

class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        prefix_sum = 0
        seen_sums = set()
        seen_sums.add(0)
        count = 0
        
        for num in nums:
            prefix_sum += num
            if prefix_sum - target in seen_sums:
                count += 1
                seen_sums.clear()
                seen_sums.add(0)
                prefix_sum = 0
            else:
                seen_sums.add(prefix_sum)
        
        return count