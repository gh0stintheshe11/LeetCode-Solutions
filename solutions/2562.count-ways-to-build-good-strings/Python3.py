class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        
        # Initialize dp array where dp[i] will store the number of good strings of length i
        dp = [0] * (high + 1)
        # Base case: There's one way to have a string of length 0
        dp[0] = 1
        
        # Calculate the number of ways to create good strings for each length up to 'high'
        for length in range(1, high + 1):
            if length >= zero:
                dp[length] = (dp[length] + dp[length - zero]) % MOD
            if length >= one:
                dp[length] = (dp[length] + dp[length - one]) % MOD
        
        # Sum up the number of good strings whose lengths are between low and high
        result = 0
        for length in range(low, high + 1):
            result = (result + dp[length]) % MOD
        
        return result