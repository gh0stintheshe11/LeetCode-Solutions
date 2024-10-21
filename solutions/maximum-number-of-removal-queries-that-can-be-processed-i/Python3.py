class Solution:
    def dfs(self, v: List[int], q: List[int], x: int, y: int, dp: List[List[int]]):
        if dp[x][y] >= 0:
            return dp[x][y]

        t1 = self.dfs(v, q, x - 1, y, dp) if x > 0 else -1
        t2 = self.dfs(v, q, x, y + 1, dp) if y < len(v) else -1

        dp[x][y] = max(max(t1, t2), 0)

        if t1 >= 0 and t1 < len(q) and v[x - 1] >= q[t1]:
            dp[x][y] = max(dp[x][y], t1 + 1)

        if t2 >= 0 and t2 < len(q) and v[y] >= q[t2]:
            dp[x][y] = max(dp[x][y], t2 + 1)

        return dp[x][y]

    def maximumProcessableQueries(self, nums: List[int], queries: List[int]) -> int:
        n = len(nums)
        dp = [[-1] * (n + 1) for _ in range(n)]
        dp[0][n] = 0
        result = 0

        for i in range(n):
            result = max(result, self.dfs(nums, queries, i, i, dp))

        return result