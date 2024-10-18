from typing import List
import bisect

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key=lambda x: x[1])
        dp = [0] * (n + 1)
        rides = [(start, end, end - start + tip) for start, end, tip in rides]

        j = 0
        for i in range(1, n + 1):
            if j < len(rides) and rides[j][1] == i:
                while j < len(rides) and rides[j][1] == i:
                    start, end, earnings = rides[j]
                    dp[end] = max(dp[end], dp[start] + earnings)
                    j += 1
            dp[i] = max(dp[i], dp[i - 1])

        return dp[n]