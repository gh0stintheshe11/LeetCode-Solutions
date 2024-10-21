from typing import List
from functools import lru_cache

class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(i, is_val):
            if i >= n:
                return 0

            max_val = float("-inf")

            if is_val:
                max_val = max(max_val, nums[i] + dfs(i + 1, False), nums[i])
            else:
                max_val = max(max_val, -nums[i] + dfs(i + 1, True), -nums[i])

            return max_val

        return max(dfs(i, True) for i in range(n))