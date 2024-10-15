from collections import deque

class Solution:
    def sumRemoteness(self, grid):
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        total_sum = 0

        def bfs(i, j):
            queue = deque([(i, j)])
            visited[i][j] = True
            component = []
            component_sum = 0

            while queue:
                x, y = queue.popleft()
                component.append((x, y))
                component_sum += grid[x][y]

                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != -1 and not visited[nx][ny]:
                        queue.append((nx, ny))
                        visited[nx][ny] = True

            return component, component_sum

        component_sums = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] != -1 and not visited[i][j]:
                    component, comp_sum = bfs(i, j)
                    component_sums.append((component, comp_sum))

        grid_sum = sum(grid[i][j] for i in range(n) for j in range(n) if grid[i][j] != -1)
        
        for component, comp_sum in component_sums:
            remoteness_value = grid_sum - comp_sum
            for x, y in component:
                total_sum += remoteness_value

        return total_sum