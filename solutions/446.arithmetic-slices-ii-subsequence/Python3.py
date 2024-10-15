from collections import defaultdict
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        result = 0
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                count_at_j = dp[j][diff]
                dp[i][diff] += count_at_j + 1
                result += count_at_j
                
        return result