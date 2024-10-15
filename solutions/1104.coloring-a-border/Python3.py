class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        from collections import deque
        
        m, n = len(grid), len(grid[0])
        original_color = grid[row][col]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def is_border(i, j):
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                return True
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if not (0 <= ni < m and 0 <= nj < n) or abs(grid[ni][nj]) != original_color:
                    return True
            return False
        
        # Using BFS for traversal and marking borders
        queue = deque([(row, col)])
        visited = set([(row, col)])
        borders = []

        while queue:
            x, y = queue.popleft()
            if is_border(x, y):
                borders.append((x, y))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and grid[nx][ny] == original_color:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

        for x, y in borders:
            grid[x][y] = color

        return grid