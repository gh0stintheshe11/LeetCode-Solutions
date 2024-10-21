class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # Possible moves for a knight
        moves = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]
        
        # Initialize the DP table
        dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(k + 1)]
        
        # Base case: probability of being at the starting position with 0 moves is 1
        dp[0][row][column] = 1
        
        # Fill the DP table
        for m in range(1, k + 1):
            for i in range(n):
                for j in range(n):
                    for move in moves:
                        ni, nj = i + move[0], j + move[1]
                        if 0 <= ni < n and 0 <= nj < n:
                            dp[m][i][j] += dp[m - 1][ni][nj] / 8
        
        # Sum up the probabilities of all positions on the board after k moves
        result = 0
        for i in range(n):
            for j in range(n):
                result += dp[k][i][j]
        
        return result