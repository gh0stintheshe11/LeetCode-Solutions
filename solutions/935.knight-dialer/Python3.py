class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        
        dp = [1] * 10
        
        for _ in range(n - 1):
            next_dp = [0] * 10
            for j in range(10):
                for move in moves[j]:
                    next_dp[move] = (next_dp[move] + dp[j]) % MOD
            dp = next_dp
        
        return sum(dp) % MOD