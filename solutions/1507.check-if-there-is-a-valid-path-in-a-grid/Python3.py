class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        from collections import deque
        
        m, n = len(grid), len(grid[0])
        
        # Directions based on street type. (dx, dy) and the directions it connects.
        directions = {
            1: [(0, -1, 'l'), (0, 1, 'r')],
            2: [(-1, 0, 'u'), (1, 0, 'd')],
            3: [(0, -1, 'l'), (1, 0, 'd')],
            4: [(0, 1, 'r'), (1, 0, 'd')],
            5: [(0, -1, 'l'), (-1, 0, 'u')],
            6: [(0, 1, 'r'), (-1, 0, 'u')]
        }
        
        # Directions that can connect to each side
        can_connect = {
            'l': [1, 4, 6],
            'r': [1, 3, 5],
            'u': [2, 3, 4],
            'd': [2, 5, 6]
        }

        def isConnected(type1, type2, dir):
            # Check if the next type can connect in the given direction
            return type2 in can_connect[dir]

        queue = deque([(0, 0)])
        visited = set(queue)
        
        while queue:
            x, y = queue.popleft()
            
            if (x, y) == (m - 1, n - 1):
                return True
            
            current_type = grid[x][y]

            for dx, dy, dir in directions[current_type]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    neighbor_type = grid[nx][ny]
                    if isConnected(current_type, neighbor_type, dir):
                        visited.add((nx, ny))
                        queue.append((nx, ny))
        
        return False