class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i] will store the number of ways to arrange handshakes for 2*i people
        dp = [0] * (numPeople // 2 + 1)
        
        # Base case: 0 people, 1 way (doing nothing)
        dp[0] = 1
        
        # Fill the dp array
        for i in range(1, numPeople // 2 + 1):
            dp[i] = 0
            for j in range(i):
                dp[i] = (dp[i] + dp[j] * dp[i - 1 - j]) % MOD
        
        return dp[numPeople // 2]

# Example usage:
# sol = Solution()
# print(sol.numberOfWays(4))  # Output: 2
# print(sol.numberOfWays(6))  # Output: 5
