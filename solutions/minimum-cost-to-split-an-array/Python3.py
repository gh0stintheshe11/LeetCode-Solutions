from typing import List
from collections import defaultdict

class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for r in range(1, n + 1):
            current_importance_cost = 0
            freq = defaultdict(int)

            for l in range(r, 0, -1):
                num = nums[l - 1]
                
                if freq[num] == 0:
                    current_importance_cost += 0  # New unique, no change
                elif freq[num] == 1:
                    current_importance_cost += 2  # Was unique, now duplicated
                else:
                    current_importance_cost += 1  # Was already duplicated
                
                freq[num] += 1
                dp[r] = min(dp[r], dp[l - 1] + k + current_importance_cost)

        return dp[n]