from typing import List
from functools import lru_cache
import itertools

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        subset_size = n // k
        nums.sort()
        
        if any(nums.count(x) > k for x in nums):
            return -1

        @lru_cache(None)
        def dfs(used):
            if used == (1 << n) - 1:
                return 0
            result = float('inf')
            elements = [i for i in range(n) if not (used & (1 << i))]
            if len(elements) < subset_size:
                return float('inf')
            for combo in itertools.combinations(elements, subset_size):
                if len(set(nums[i] for i in combo)) == subset_size:
                    new_used = used
                    max_num, min_num = 0, float('inf')
                    for i in combo:
                        new_used |= 1 << i
                        max_num = max(max_num, nums[i])
                        min_num = min(min_num, nums[i])
                    result = min(result, max_num - min_num + dfs(new_used))
            return result
        
        result = dfs(0)
        return result if result < float('inf') else -1