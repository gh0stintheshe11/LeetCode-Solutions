class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD = 10**9 + 7
        # Initialize the number of ways for n = 1
        prev_prev = 1  # Only empty plot
        prev = 2       # Plot empty or house placed
        
        # If n is 1, directly return
        if n == 1:
            return (prev * prev) % MOD  # Each side has 2 ways, total 2*2 = 4
        
        # Compute number of ways for one side using a bottom-up DP approach
        for i in range(2, n + 1):
            curr = (prev + prev_prev) % MOD
            prev_prev = prev
            prev = curr
        
        # Square the result to account for both sides and apply modulo
        return (prev * prev) % MOD