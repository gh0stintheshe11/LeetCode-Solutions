from typing import List

class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n < 3:
            return 0

        # Initialize dp array for first three elements
        dp = [0] * n
        for i in range(3):
            dp[i] = max(0, k - nums[i])

        # Populate dp array using the relation
        for i in range(3, n):
            dp[i] = max(0, k - nums[i]) + min(dp[i - 1], dp[i - 2], dp[i - 3])

        # The result is the minimum from the last three dp entries
        return min(dp[n - 1], dp[n - 2], dp[n - 3])