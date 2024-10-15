from typing import List

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        from sortedcontainers import SortedList
        
        prefix_sum = 0
        prefix_sums = SortedList([0])
        count = 0
        
        for num in nums:
            prefix_sum += num
            count += prefix_sums.bisect_right(prefix_sum - lower) - prefix_sums.bisect_left(prefix_sum - upper)
            prefix_sums.add(prefix_sum)
            
        return count