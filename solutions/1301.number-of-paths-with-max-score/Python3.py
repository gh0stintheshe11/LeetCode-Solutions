from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)
        
        # dp[i][j] will store (max_score, number_of_paths) to reach from (i, j) to (n-1, n-1).
        dp = [[(0, 0) for _ in range(n)] for _ in range(n)]
        dp[n-1][n-1] = (0, 1)  # Starting at 'S' with score 0 and 1 path.

        for i in reversed(range(n)):
            for j in reversed(range(n)):
                if board[i][j] in 'XS':
                    continue
                max_score, num_paths = 0, 0
                for di, dj in [(1, 0), (0, 1), (1, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        score, paths = dp[ni][nj]
                        if score > max_score:
                            max_score, num_paths = score, paths
                        elif score == max_score:
                            num_paths = (num_paths + paths) % MOD
                if board[i][j] != 'E':
                    max_score += int(board[i][j])
                dp[i][j] = (max_score, num_paths)

        return list(dp[0][0]) if dp[0][0][1] > 0 else [0, 0]