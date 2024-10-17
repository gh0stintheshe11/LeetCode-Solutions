class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        large_int = 10**9
        dp = [0] * 10
        for c in range(C):
            prev = dp
            dp = [large_int] * 10
            count_map = [0] * 10
            for r in range(R):
                count_map[grid[r][c]] += 1
            for num in range(10):
                for prev_num in range(10):
                    if prev_num != num:
                        ops = prev[prev_num] + (R - count_map[num])
                        dp[num] = min(dp[num], ops)
        return min(dp)