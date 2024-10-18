class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        @cache
        def dp(i, j):
            if i >= len(grid) or j >= len(grid[0]):
                return [-float('inf'), -float('inf')]
            left, right = dp(i+1, j), dp(i, j+1)
            score = max(left[0], right[0], left[1] - grid[i][j], right[1] - grid[i][j])
            max_num = max(left[1], right[1], grid[i][j])
            return [score, max_num]
        return dp(0, 0)[0]