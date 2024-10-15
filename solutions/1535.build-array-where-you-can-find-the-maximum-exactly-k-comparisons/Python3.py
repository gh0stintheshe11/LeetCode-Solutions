class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        if k == 0:
            return 0
        
        # dp[i][j][c]: number of ways to fill the first `i` numbers with maximum `j` and cost `c`
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]
        
        # Base case
        for j in range(1, m + 1):
            dp[1][j][1] = 1  # Initializing first element with any number j with cost 1
        
        # Fill the dp array
        for i in range(2, n + 1):  # i: length of array being considered
            for j in range(1, m + 1):  # j: maximum number allowed
                for c in range(1, k + 1):  # c: number of increases
                    # Case 1: current value is <= previous max (j)
                    dp[i][j][c] = dp[i-1][j][c] * j % MOD
                    
                    # Case 2: current value becomes the new maximum
                    for x in range(1, j):
                        dp[i][j][c] = (dp[i][j][c] + dp[i-1][x][c-1]) % MOD
        
        # Sum all the ways with n numbers and exactly k comparisons
        return sum(dp[n][j][k] for j in range(1, m + 1)) % MOD