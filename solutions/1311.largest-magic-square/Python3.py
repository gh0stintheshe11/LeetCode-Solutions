class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        # Function to check if k x k square starting at (r, c) is a magic square
        def is_magic(r, c, k):
            # Calculate row, column and diagonal sums
            target_sum = sum(grid[r][c:c + k])
            # Check all rows
            for i in range(r, r + k):
                if sum(grid[i][c:c + k]) != target_sum:
                    return False
            # Check all columns
            for j in range(c, c + k):
                if sum(grid[i][j] for i in range(r, r + k)) != target_sum:
                    return False
            # Check top-left to bottom-right diagonal
            if sum(grid[r + i][c + i] for i in range(k)) != target_sum:
                return False
            # Check top-right to bottom-left diagonal
            if sum(grid[r + i][c + k - 1 - i] for i in range(k)) != target_sum:
                return False
            return True

        m, n = len(grid), len(grid[0])
        max_k = min(m, n)
        
        for k in range(max_k, 1, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if is_magic(r, c, k):
                        return k
        return 1