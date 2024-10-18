from typing import List

class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        
        for length in range(1, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                if length == 1:
                    dp[i][j] = 1
                elif length == 2:
                    dp[i][j] = 1 if arr[i] == arr[j] else 2
                else:
                    dp[i][j] = dp[i+1][j] + 1
                    if arr[i] == arr[j]:
                        dp[i][j] = min(dp[i][j], dp[i+1][j-1])
                    for k in range(i+1, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])
                        
        return dp[0][n-1]