class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = ['-inf'] * (target + 1)
        dp[0] = ''
        
        for t in range(1, target + 1):
            for i in range(9):
                if t >= cost[i] and dp[t - cost[i]] != '-inf':
                    candidate = dp[t - cost[i]] + str(i + 1)
                    if dp[t] == '-inf' or len(candidate) > len(dp[t]) or (len(candidate) == len(dp[t]) and candidate > dp[t]):
                        dp[t] = candidate
        
        return dp[target] if dp[target] != '-inf' else '0'