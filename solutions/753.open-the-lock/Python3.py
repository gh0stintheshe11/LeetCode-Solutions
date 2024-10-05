from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0
            
        dead = set(deadends)
        if "0000" in dead:
            return -1
        
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i+1:]
                    
        queue = deque([("0000", 0)])
        visited = {"0000"}
        
        while queue:
            node, depth = queue.popleft()
            for nei in neighbors(node):
                if nei == target:
                    return depth + 1
                if nei not in visited and nei not in dead:
                    visited.add(nei)
                    queue.append((nei, depth + 1))
        
        return -1