class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        skip = [[0] * 10 for _ in range(10)]
        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[3][9] = skip[9][3] = 6
        skip[7][9] = skip[9][7] = 8
        skip[1][9] = skip[9][1] = skip[2][8] = skip[8][2] = skip[3][7] = skip[7][3] = skip[4][6] = skip[6][4] = 5

        def dfs(visited, cur, remain):
            if remain < 0: return 0
            if remain == 0: return 1
            visited[cur] = True
            count = 0
            for i in range(1, 10):
                if not visited[i] and (skip[cur][i] == 0 or visited[skip[cur][i]]):
                    count += dfs(visited, i, remain - 1)
            visited[cur] = False
            return count

        visited = [False] * 10
        result = 0
        for i in range(m, n + 1):
            result += dfs(visited, 1, i - 1) * 4  # 1, 3, 7, 9 are symmetric
            result += dfs(visited, 2, i - 1) * 4  # 2, 4, 6, 8 are symmetric
            result += dfs(visited, 5, i - 1)      # 5 is unique
        return result