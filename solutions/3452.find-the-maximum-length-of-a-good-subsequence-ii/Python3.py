from collections import defaultdict
from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [defaultdict(int) for _ in range(k+1)]
        res = [0]*(k+1)
        for a in nums:
            for j in range(k, -1, -1):
                dp[j][a] = max(dp[j][a]+1, res[j-1]+1 if j else 1)
                res[j] = max(res[j], dp[j][a])
        return res[k]