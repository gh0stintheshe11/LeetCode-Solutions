from typing import List
import sys

class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[sys.maxsize] * (k + 2) for _ in range(n)]
        
        for i in range(n):
            max_val = nums[i]
            total_sum = 0
            for j in range(i, n):
                max_val = max(max_val, nums[j])
                total_sum += nums[j]
                waste = max_val * (j - i + 1) - total_sum
                if i == 0:
                    dp[j][1] = waste
                else:
                    for r in range(1, k + 2):
                        dp[j][r] = min(dp[j][r], dp[i - 1][r - 1] + waste)
        
        return min(dp[n - 1][r] for r in range(1, k + 2))