class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # Initialize the dp array with False values
        dp = [False] * (n + 1)
        
        # Iterate over each number of stones from 1 to n
        for i in range(1, n + 1):
            # Check all possible square numbers that can be removed
            j = 1
            while j * j <= i:
                if not dp[i - j * j]:
                    dp[i] = True
                    break
                j += 1
        
        # Return the result for n stones
        return dp[n]