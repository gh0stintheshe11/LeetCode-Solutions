from typing import List

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [float('-inf')] * n
        dp[0] = 0

        for i in range(n):
            for j in range(i + 1, n):
                if -target <= nums[j] - nums[i] <= target:
                    dp[j] = max(dp[j], dp[i] + 1)

        return dp[-1] if dp[-1] != float('-inf') else -1