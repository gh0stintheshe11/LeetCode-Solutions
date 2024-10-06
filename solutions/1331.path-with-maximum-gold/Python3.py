class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
                return 0
            
            original_value = grid[row][col]
            grid[row][col] = 0  # Mark the cell as visited
            max_gold = 0
            
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                max_gold = max(max_gold, dfs(row + dr, col + dc))
            
            grid[row][col] = original_value  # Restore the cell's gold value
            return max_gold + original_value

        max_gold = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] > 0:
                    max_gold = max(max_gold, dfs(r, c))
        
        return max_gold