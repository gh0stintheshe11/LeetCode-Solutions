from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        # Calculate ones and zeros in each row
        onesRow = [sum(row) for row in grid]
        zerosRow = [n - ones for ones in onesRow]
        
        # Calculate ones and zeros in each column
        onesCol = [sum(grid[i][j] for i in range(m)) for j in range(n)]
        zerosCol = [m - ones for ones in onesCol]
        
        # Calculate the difference matrix
        diff = [
            [
                onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]
                for j in range(n)
            ]
            for i in range(m)
        ]

        return diff