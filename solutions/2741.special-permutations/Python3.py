from typing import List
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        @lru_cache(None)
        def dfs(mask, last_index):
            if mask == (1 << n) - 1:
                return 1
            
            count = 0
            for i in range(n):
                if not (mask & (1 << i)):
                    if last_index == -1 or nums[last_index] % nums[i] == 0 or nums[i] % nums[last_index] == 0:
                        count = (count + dfs(mask | (1 << i), i)) % MOD
            return count
        
        return dfs(0, -1)