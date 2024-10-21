from collections import defaultdict
from typing import List

class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        remainder_count = defaultdict(int)
        num_to_rem = {}
        
        for num in nums:
            remainder = num % space
            remainder_count[remainder] += 1
            if remainder not in num_to_rem or num_to_rem[remainder] > num:
                num_to_rem[remainder] = num
        
        max_destroy = max(remainder_count.values())
        min_seed = float('inf')
        
        for remainder in remainder_count:
            if remainder_count[remainder] == max_destroy:
                min_seed = min(min_seed, num_to_rem[remainder])
        
        return min_seed