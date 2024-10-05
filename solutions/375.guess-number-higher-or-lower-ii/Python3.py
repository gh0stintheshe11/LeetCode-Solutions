class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        def calculate(l, r):
            if l >= r:
                return 0
            if dp[l][r] != 0:
                return dp[l][r]
            globalMin = float('inf')
            for i in range((l + r) // 2, r + 1):
                localMax = i + max(calculate(l, i - 1), calculate(i + 1, r))
                globalMin = min(globalMin, localMax)
            dp[l][r] = globalMin
            return globalMin
        
        return calculate(1, n)