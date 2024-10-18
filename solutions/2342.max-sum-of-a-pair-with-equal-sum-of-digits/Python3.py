from typing import List
from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digit_sum(n):
            return sum(int(d) for d in str(n))
        
        sums = defaultdict(list)
        
        for num in nums:
            d_sum = digit_sum(num)
            sums[d_sum].append(num)
        
        max_sum = -1
        for val in sums.values():
            if len(val) > 1:
                val.sort(reverse=True)
                max_sum = max(max_sum, val[0] + val[1])
        
        return max_sum