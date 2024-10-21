from collections import deque
from typing import List, Tuple, Set

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def is_valid(x: int, y: int) -> bool:
            return 0 <= x < m and 0 <= y < n and grid[x][y] != '#'

        # Find initial positions of S, B, and T
        player, box, target = None, None, None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    player = (i, j)
                elif grid[i][j] == 'B':
                    box = (i, j)
                elif grid[i][j] == 'T':
                    target = (i, j)

        # BFS with state (box_x, box_y, player_x, player_y)
        # We will store the time when box is at (box_x, box_y) with (player_x, player_y)
        q = deque([(box[0], box[1], player[0], player[1], 0)])
        visited: Set[Tuple[int, int, int, int]] = set()
        visited.add((box[0], box[1], player[0], player[1]))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            bx, by, px, py, push_count = q.popleft()

            if (bx, by) == target:
                return push_count

            for dx, dy in directions:
                nbx, nby = bx + dx, by + dy
                npx, npy = bx - dx, by - dy

                # Check if the box is within bounds and the next cell is a floor
                if is_valid(nbx, nby) and is_valid(npx, npy):
                    # Check if it's possible to move the player to npx, npy to push the box to nbx, nby
                    if (nbx, nby, bx, by) not in visited:
                        if self.can_reach(px, py, npx, npy, bx, by, grid, m, n):
                            visited.add((nbx, nby, bx, by))
                            q.append((nbx, nby, bx, by, push_count + 1))
        
        return -1

    def can_reach(self, start_x: int, start_y: int, end_x: int, end_y: int, obs_x: int, obs_y: int, grid: List[List[str]], m: int, n: int) -> bool:
        if start_x == end_x and start_y == end_y:
            return True
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque([(start_x, start_y)])
        visited = [[False] * n for _ in range(m)]
        visited[start_x][start_y] = True

        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if (0 <= nx < m and 0 <= ny < n and grid[nx][ny] != '#'
                        and not visited[nx][ny] and (nx, ny) != (obs_x, obs_y)):
                    if (nx, ny) == (end_x, end_y):
                        return True
                    q.append((nx, ny))
                    visited[nx][ny] = True
        
        return False