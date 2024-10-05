from typing import List

class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid) - 1):
            for j in range(i + 1, len(grid)):
                lineCount = 0
                for k in range(len(grid[0])):
                    if grid[i][k] == 1 and grid[j][k] == 1:
                        lineCount += 1
                count += lineCount * (lineCount - 1) // 2
        return count