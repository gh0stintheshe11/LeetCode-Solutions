class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        # dp[a][b][c] = number of ways for arrays with a zeros, b ones, ending with c
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        
        dp[0][0][0] = 1
        dp[0][0][1] = 1

        for z in range(zero + 1):
            for o in range(one + 1):
                for l in range(1, limit + 1):
                    if z + l <= zero:
                        dp[z + l][o][0] = (dp[z + l][o][0] + dp[z][o][1]) % MOD
                    if o + l <= one:
                        dp[z][o + l][1] = (dp[z][o + l][1] + dp[z][o][0]) % MOD

        # Total number of arrays ending with either 0 or 1
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD