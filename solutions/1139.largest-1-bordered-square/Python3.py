class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[(0, 0) for _ in range(m)] for _ in range(n)]

        # Fill the dp table with the number of consecutive 1s to the left and up
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    left = dp[i][j-1][0] + 1 if j > 0 else 1
                    up = dp[i-1][j][1] + 1 if i > 0 else 1
                    dp[i][j] = (left, up)

        max_side = 0

        # Check for the largest possible square for each bottom-right point
        for i in range(n):
            for j in range(m):
                side = min(dp[i][j])
                while side > max_side:
                    if dp[i][j-side+1][1] >= side and dp[i-side+1][j][0] >= side:
                        max_side = side
                    side -= 1

        return max_side * max_side