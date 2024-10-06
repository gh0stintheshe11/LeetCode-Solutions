from typing import List

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        num_rows, num_cols = len(rowSum), len(colSum)
        matrix = [[0] * num_cols for _ in range(num_rows)]
        
        for i in range(num_rows):
            for j in range(num_cols):
                min_value = min(rowSum[i], colSum[j])
                matrix[i][j] = min_value
                rowSum[i] -= min_value
                colSum[j] -= min_value
                
        return matrix