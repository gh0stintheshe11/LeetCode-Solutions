class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0

        for i in range(n // 2):
            for j in range(m // 2):
                ones = 0

                if grid[i][j] == 1:
                    ones += 1
                if grid[n - i - 1][j] == 1:
                    ones += 1
                if grid[i][m - j - 1] == 1:
                    ones += 1
                if grid[n - i - 1][m - j - 1] == 1:
                    ones += 1

                if ones == 4 or ones == 0:
                    continue

                if ones >= 2:
                    ans += (4 - ones)
                else:
                    ans += ones

        if n % 2 == 0 and m % 2 == 0:
            return ans

        palones = 0
        notpalones = 0

        if n % 2 == 1:
            for i in range(m // 2):
                if grid[n // 2][i] == 1 and grid[n // 2][m - i - 1] == 1:
                    palones += 1
                if grid[n // 2][i] != grid[n // 2][m - i - 1]:
                    ans += 1
                    notpalones += 1

        if m % 2 == 1:
            for i in range(n // 2):
                if grid[i][m // 2] == 1 and grid[n - i - 1][m // 2] == 1:
                    palones += 1
                if grid[i][m // 2] != grid[n - i - 1][m // 2]:
                    ans += 1
                    notpalones += 1

        if palones % 2 == 1:
            if notpalones == 0:
                ans += 2

        if n % 2 == 1 and m % 2 == 1 and grid[n // 2][m // 2] == 1:
            ans += 1

        return ans