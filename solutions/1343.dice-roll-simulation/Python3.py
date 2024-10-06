class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7
        
        dp = [[0] * 6 for _ in range(n + 1)]
        sum_dp = [0] * (n + 1)
        
        for i in range(6):
            dp[1][i] = 1
        sum_dp[1] = 6
        
        for i in range(2, n + 1):
            for j in range(6):
                dp[i][j] = sum_dp[i - 1]
                
                if i - rollMax[j] == 1:
                    dp[i][j] -= 1
                elif i - rollMax[j] > 1:
                    dp[i][j] -= (sum_dp[i - rollMax[j] - 1] - dp[i - rollMax[j] - 1][j])
                
                dp[i][j] = (dp[i][j] + MOD) % MOD
            
            sum_dp[i] = sum(dp[i]) % MOD
        
        return sum_dp[n]