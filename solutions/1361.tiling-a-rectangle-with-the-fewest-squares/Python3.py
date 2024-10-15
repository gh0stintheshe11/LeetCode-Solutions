class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        def dfs(heights, steps):
            nonlocal min_steps
            if all(height == n for height in heights):
                min_steps = min(min_steps, steps)
                return
            if steps >= min_steps:
                return

            min_height = min(heights)
            idx = heights.index(min_height)

            for size in range(min(m - idx, n - min_height), 0, -1):
                if all(heights[idx + i] == min_height for i in range(size)):
                    new_heights = heights[:]
                    for i in range(size):
                        new_heights[idx + i] += size

                    dfs(new_heights, steps + 1)

        if n > m:
            n, m = m, n

        min_steps = n * m
        dfs([0] * m, 0)
        return min_steps