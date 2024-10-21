class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7

        if n == 1:
            return 3
        if n == 2:
            return 8
        
        dp = [[0] * 3 for _ in range(2)]
        dp[0] = [1, 1, 0]
        dp[1] = [1, 0, 0]
        
        for i in range(2, n + 1):
            dp_new = [[0] * 3 for _ in range(2)]
            
            dp_new[0][0] = (dp[0][0] + dp[0][1] + dp[0][2]) % MOD
            dp_new[0][1] = dp[0][0]
            dp_new[0][2] = dp[0][1]

            dp_new[1][0] = (dp[1][0] + dp[1][1] + dp[1][2] + dp[0][0] + dp[0][1] + dp[0][2]) % MOD
            dp_new[1][1] = dp[1][0]
            dp_new[1][2] = dp[1][1]
            
            dp = dp_new
        
        return (dp[1][0] + dp[1][1] + dp[1][2] + dp[0][0] + dp[0][1] + dp[0][2]) % MOD