class Solution:
    def distinctSequences(self, n: int) -> int:
        MOD = 10**9 + 7

        if n == 1:
            return 6
        
        # 3D DP table: dp[i][j][k] represents the number of ways to achieve a sequence of length i,
        # where the last number is j and the second to last number is k.
        dp = [[[0] * 7 for _ in range(7)] for _ in range(n + 1)]
        
        # Initialize base case: for sequences of length 2
        for i in range(1, 7):
            for j in range(1, 7):
                if i != j and gcd(i, j) == 1:
                    dp[2][i][j] = 1

        # Fill the DP table
        for i in range(3, n + 1):
            for j in range(1, 7):
                for k in range(1, 7):
                    if j != k and gcd(j, k) == 1:
                        # For each possible first number of the previous sequence
                        for l in range(1, 7):
                            if l != j:
                                dp[i][j][k] = (dp[i][j][k] + dp[i - 1][k][l]) % MOD
        
        # Calculate the result for sequences of length n
        result = 0
        for j in range(1, 7):
            for k in range(1, 7):
                result = (result + dp[n][j][k]) % MOD

        return result

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a