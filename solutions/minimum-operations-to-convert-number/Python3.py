from typing import List
from collections import deque

class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        visited = set()
        queue = deque([(start, 0)])

        while queue:
            current, steps = queue.popleft()

            if current == goal:
                return steps
            
            if current < 0 or current > 1000 or current in visited:
                continue

            visited.add(current)

            for num in nums:
                queue.append((current + num, steps + 1))
                queue.append((current - num, steps + 1))
                queue.append((current ^ num, steps + 1))
        
        return -1