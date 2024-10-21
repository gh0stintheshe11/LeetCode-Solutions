class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        from collections import deque
        
        def bfs(x0, y0):
            queue = deque([(x0, y0)])
            island = [(x0, y0)]
            grid[x0][y0] = 0
            
            while queue:
                x, y = queue.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                        grid[nx][ny] = 0
                        queue.append((nx, ny))
                        island.append((nx, ny))
            return island
        
        def rotate(x, y, k):
            if k == 0: return x, y
            if k == 1: return y, -x
            if k == 2: return -x, -y
            if k == 3: return -y, x
        
        def reflect(x, y, k):
            if k == 0: return x, y
            if k == 1: return -x, y
            if k == 2: return x, -y
            if k == 3: return -x, -y
        
        def transform(island):
            shapes = set()
            for k in range(4):
                for l in range(4):
                    shape = sorted([rotate(*reflect(x, y, l), k) for x, y in island])
                    offset_x, offset_y = shape[0]
                    norm_shape = tuple((x - offset_x, y - offset_y) for x, y in shape)
                    shapes.add(norm_shape)
            return min(shapes)
        
        unique_islands = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    island = bfs(i, j)
                    unique_islands.add(transform(island))
        
        return len(unique_islands)