class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i]: number of strings of length n ending with vowels a, e, i, o, u
        dp = [1] * 5
        
        for _ in range(1, n):
            a, e, i, o, u = dp
            dp[0] = (e + i + u) % MOD  # a can be followed by e, i, u
            dp[1] = (a + i) % MOD      # e can be followed by a, i
            dp[2] = (e + o) % MOD      # i can be followed by e, o
            dp[3] = i % MOD            # o can be followed by i
            dp[4] = (i + o) % MOD      # u can be followed by i, o
            
        return sum(dp) % MOD