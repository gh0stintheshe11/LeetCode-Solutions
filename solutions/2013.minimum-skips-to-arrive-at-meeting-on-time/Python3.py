class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        n = len(dist)
        
        # DP array: dp[i][j] is the minimum total time to complete first i roads with j skips
        dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
        
        dp[0][0] = 0
        
        for i in range(1, n + 1):
            t = dist[i - 1] / speed
            
            for j in range(i + 1):
                # If no skip is used at this road
                if j < i:
                    dp[i][j] = min(dp[i][j], math.ceil(dp[i - 1][j] + t - 1e-9))
                
                # If a skip is used to avoid waiting
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + t)
        
        for j in range(n + 1):
            if dp[n][j] <= hoursBefore:
                return j
        
        return -1