class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_sum = 0
        
        for _ in range(n):
            max_in_column = 0
            for row in grid:
                max_value = max(row)
                row.remove(max_value)
                max_in_column = max(max_in_column, max_value)
            max_sum += max_in_column
        
        return max_sum