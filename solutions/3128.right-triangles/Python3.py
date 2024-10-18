class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        row_count = [0] * rows
        col_count = [0] * cols
        
        # Count the number of 1s in each row and each column
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row_count[r] += 1
                    col_count[c] += 1
        
        total_triangles = 0
        
        # Calculate the number of right triangles
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    total_triangles += (row_count[r] - 1) * (col_count[c] - 1)
        
        return total_triangles