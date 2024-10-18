class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        prefix_sum = [0] * (n + 1)

        # Calculate prefix sum of white tiles
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + (floor[i] == '1')

        dp = [[0] * (numCarpets + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(numCarpets + 1):
                # Case without using a carpet at position i
                dp[i][j] = dp[i + 1][j]
                if floor[i] == '1':
                    dp[i][j] += 1  # if it's white tile, add one
                
                # Case with using a carpet at position i
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[min(n, i + carpetLen)][j - 1])

        return dp[0][numCarpets]