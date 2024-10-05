from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        
        n = len(costs)
        dp = costs[0][:]
        
        for i in range(1, n):
            dp_prev = dp[:]
            dp[0] = costs[i][0] + min(dp_prev[1], dp_prev[2])
            dp[1] = costs[i][1] + min(dp_prev[0], dp_prev[2])
            dp[2] = costs[i][2] + min(dp_prev[0], dp_prev[1])
        
        return min(dp)