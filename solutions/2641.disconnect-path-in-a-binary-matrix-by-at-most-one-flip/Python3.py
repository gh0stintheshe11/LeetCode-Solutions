class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Helper to find if a path exists from (r, c) to (m - 1, n - 1)
        def hasPath(r, c):
            if r == m - 1 and c == n - 1:
                return True
            if r >= m or c >= n or grid[r][c] == 0:
                return False
            
            grid[r][c] = 0  # Mark as visited to prevent revisiting
            if hasPath(r + 1, c) or hasPath(r, c + 1):
                return True
            return False
        
        # Check if there's an initial path
        if not hasPath(0, 0):
            return True
        
        # Reset the visited marks
        grid[0][0] = grid[m - 1][n - 1] = 1
        
        # Check again for a path
        return not hasPath(0, 0)