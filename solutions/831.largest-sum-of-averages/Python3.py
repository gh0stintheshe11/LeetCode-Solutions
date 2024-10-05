from typing import List

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        def average(i, j):
            return (prefix_sum[j + 1] - prefix_sum[i]) / (j - i + 1)
        
        dp = [[0] * (k + 1) for _ in range(n)]
        
        for i in range(n):
            dp[i][1] = average(0, i)
        
        for m in range(2, k + 1):
            for i in range(n):
                for j in range(i):
                    dp[i][m] = max(dp[i][m], dp[j][m - 1] + average(j + 1, i))
        
        return dp[n - 1][k]