class Solution:
    def numberOfCombinations(self, num: str) -> int:
        n = len(num)
        lcs = [[0]*(n+1) for _ in range(n)]
        for i in reversed(range(n)): 
            for j in reversed(range(i+1, n)): 
                if num[i] == num[j]: lcs[i][j] = 1 + lcs[i+1][j+1]
        
        def cmp(i, j, d): 
            m = lcs[i][j]
            if m >= d: return True 
            return num[i+m] <= num[j+m]
        
        dp = [[0]*(n+1) for _ in range(n)]
        for i in range(n): 
            if num[i] != "0": 
                for j in range(i+1, n+1): 
                    if i == 0: dp[i][j] = 1
                    else: 
                        dp[i][j] = dp[i][j-1]
                        if 2*i-j >= 0 and cmp(2*i-j, i, j-i): dp[i][j] += dp[2*i-j][i]
                        if 2*i-j+1 >= 0 and not cmp(2*i-j+1, i, j-i-1): dp[i][j] += dp[2*i-j+1][i]
        return sum(dp[i][n] for i in range(n)) % 1_000_000_007