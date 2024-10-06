from typing import List

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        
        for length in range(1, n):
            for i in range(n - length):
                j = i + length
                min_cost = float('inf')
                for k in range(i, j):
                    max_left = max(arr[i:k+1])
                    max_right = max(arr[k+1:j+1])
                    cost = max_left * max_right + dp[i][k] + dp[k+1][j]
                    if cost < min_cost:
                        min_cost = cost
                dp[i][j] = min_cost
        
        return dp[0][n-1]