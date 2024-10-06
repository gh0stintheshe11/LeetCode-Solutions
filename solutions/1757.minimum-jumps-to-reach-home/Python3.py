from collections import deque
from typing import List

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden_set = set(forbidden)
        upper_limit = 6000  # Define an upper_limit less than a + 2 * b or max(x, max(forbidden)) + a + b
        queue = deque([(0, 0, False)])  # (position, steps, back_jumped)
        visited = set((0, False))
        
        while queue:
            pos, steps, back_jumped = queue.popleft()
            
            if pos == x:
                return steps
            
            # Jump forward
            forward_position = pos + a
            if forward_position <= upper_limit and forward_position not in forbidden_set and (forward_position, False) not in visited:
                visited.add((forward_position, False))
                queue.append((forward_position, steps + 1, False))
            
            # Jump backward only if the last jump wasn't back
            if not back_jumped:
                backward_position = pos - b
                if backward_position >= 0 and backward_position not in forbidden_set and (backward_position, True) not in visited:
                    visited.add((backward_position, True))
                    queue.append((backward_position, steps + 1, True))
        
        return -1