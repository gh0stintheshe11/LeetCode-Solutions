from typing import List, Set, Tuple, Deque
from collections import deque

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        BLOCKED = {-1}  # a set to keep track of cells that are blocked
        BOUNDARY = 10**6  # boundary of the grid
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # possible directions: right, down, left, up
        
        blocked_set = set(map(tuple, blocked))
        
        def bfs(start: List[int], finish: List[int]) -> bool:
            queue: Deque[Tuple[int, int]] = deque([tuple(start)])
            seen: Set[Tuple[int, int]] = {tuple(start)}
            while queue:
                if len(seen) > 20000:
                    return True
                x, y = queue.popleft()
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < BOUNDARY and 0 <= ny < BOUNDARY and (nx, ny) not in seen and (nx, ny) not in blocked_set:
                        if [nx, ny] == finish:
                            return True
                        queue.append((nx, ny))
                        seen.add((nx, ny))
            return False
        
        return bfs(source, target) and bfs(target, source)