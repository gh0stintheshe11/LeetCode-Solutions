from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(1, n):
            for j in range(n):
                min_above = matrix[i-1][j] 
                if j > 0:
                    min_above = min(min_above, matrix[i-1][j-1])
                if j < n - 1:
                    min_above = min(min_above, matrix[i-1][j+1])
                matrix[i][j] += min_above
        return min(matrix[-1])